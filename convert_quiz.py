import pdfplumber
import json
import re
from collections import Counter

# --- CẤU HÌNH ---
INPUT_PDF = "data.pdf"  # Tên file PDF của bạn
OUTPUT_JS = "questions.js"

def solve_by_anomaly(options_meta, question_id):
    """
    Thuật toán tìm kẻ khác biệt.
    Input: Danh sách thông tin font của [a, b, c, d]
    Ví dụ: ['Arial', 'Arial', 'Times-Italic', 'Arial'] -> 'Times-Italic' là đáp án.
    """
    fonts = [m['font'] for m in options_meta]
    
    # Đếm số lần xuất hiện của từng font
    counts = Counter(fonts)
    
    # Tìm font nào chỉ xuất hiện ĐÚNG 1 LẦN (Unique)
    unique_font = None
    for font, count in counts.items():
        if count == 1:
            unique_font = font
            break
    
    # In ra để kiểm tra (Debug)
    print(f"   🔎 [Soi dữ liệu câu {question_id}]: {fonts}")
    
    if unique_font:
        # Tìm index của font đó
        idx = fonts.index(unique_font)
        print(f"      => PHÁT HIỆN KHÁC BIỆT: Vị trí {['a','b','c','d'][idx]} (Font: {unique_font})")
        return idx
    else:
        print("      => ⚠️ Tất cả các font giống nhau hoặc không có sự khác biệt rõ ràng.")
        return None

def extract_quiz_debug(pdf_path):
    questions = []
    current_q = None
    
    print(f"🚀 Bắt đầu quét file: {pdf_path}")
    print("="*60)
    
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            rows = page.extract_text_lines(return_chars=True, x_tolerance=2)
            
            for row in rows:
                text = row['text'].strip()
                chars = row['chars']
                
                # 1. BẮT CÂU HỎI
                q_match = re.match(r"^Câu\s+(\d+)[\.:]\s*(.*)", text, re.IGNORECASE)
                if q_match:
                    # Xử lý câu cũ
                    if current_q:
                        # Logic tìm đáp án cho câu cũ
                        if len(current_q["meta_temp"]) == 4:
                            ans_idx = solve_by_anomaly(current_q["meta_temp"], current_q['id'])
                            current_q["correctAnswer"] = ans_idx
                        # Xóa biến tạm
                        del current_q["meta_temp"]
                        questions.append(current_q)
                    
                    # Tạo câu mới
                    current_q = {
                        "id": int(q_match.group(1)),
                        "question": q_match.group(2).strip(),
                        "options": [],
                        "correctAnswer": None,
                        "meta_temp": [] # Biến tạm lưu font chữ của a,b,c,d
                    }
                    continue
                
                # 2. BẮT ĐÁP ÁN (a., b., c., d.)
                opt_match = re.match(r"^([a-d])([\.\)\s])\s*(.*)", text, re.IGNORECASE)
                if current_q and opt_match:
                    label = opt_match.group(1).lower() # a, b, c, d
                    content = opt_match.group(3).strip()
                    
                    current_q["options"].append(f"{label}. {content}")
                    
                    # --- LẤY FONT CỦA KÝ TỰ ĐẦU DÒNG (LABEL) ---
                    # Tìm ký tự a/b/c/d trong danh sách chars
                    found_font = "Unknown"
                    for char in chars:
                        if char['text'].lower() == label:
                            found_font = char.get("fontname", "Unknown")
                            break
                    
                    # Lưu vào biến tạm để tí nữa so sánh
                    current_q["meta_temp"].append({"label": label, "font": found_font})

    # Xử lý câu cuối cùng
    if current_q:
        if len(current_q["meta_temp"]) == 4:
            ans_idx = solve_by_anomaly(current_q["meta_temp"], current_q['id'])
            current_q["correctAnswer"] = ans_idx
        if "meta_temp" in current_q: del current_q["meta_temp"]
        questions.append(current_q)
        
    return questions

# --- THỰC THI ---
try:
    data = extract_quiz_debug(INPUT_PDF)
    
    # Thống kê
    detected = sum(1 for q in data if q['correctAnswer'] is not None)
    print("="*60)
    print(f"📊 KẾT QUẢ: Quét được {len(data)} câu. Tìm ra đáp án cho {detected} câu.")
    
    if detected == 0:
        print("❌ CẤP BÁO: Vẫn không tìm thấy sự khác biệt nào về tên Font.")
        print("👉 HÃY COPY ĐOẠN LOG Ở TRÊN (PHẦN [Soi dữ liệu...]) GỬI CHO TÔI.")
        print("Tôi cần biết máy tính đang 'nhìn thấy' tên font là gì (VD: ArialMT, TimesNewRomanPSMT...).")
    
    # Xuất file
    js_content = f"const questions = {json.dumps(data, ensure_ascii=False, indent=2)};"
    with open(OUTPUT_JS, "w", encoding="utf-8") as f:
        f.write(js_content)

except Exception as e:
    print(f"❌ Lỗi: {e}")
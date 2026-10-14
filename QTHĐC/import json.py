import json
import re
from bs4 import BeautifulSoup

def is_bold_or_highlighted(tag):
    """
    Hàm heuristic để kiểm tra xem một thẻ có được định dạng là đáp án đúng không.
    Kiểm tra: Thẻ <b>, <strong>, hoặc style font-weight:700 (in đậm), hoặc có màu sắc khác biệt.
    """
    if not tag:
        return False
        
    # 1. Kiểm tra thẻ in đậm trực tiếp
    if tag.name in ['b', 'strong']:
        return True

    # 2. Kiểm tra CSS inline (Google Docs thường dùng cách này)
    style = tag.get('style', '')
    if not style:
        return False
    
    style = style.lower()
    # Kiểm tra in đậm
    if 'font-weight:700' in style or 'font-weight: bold' in style:
        return True
    
    # Kiểm tra màu sắc (Nếu file dùng màu đỏ để đánh dấu đáp án)
    # color: #000000 là màu đen, nếu khác đen có thể là đáp án
    if 'color' in style and '#000000' not in style and 'color' in style: 
        return True
        
    return False

def parse_html_to_js(file_path, output_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        html_content = f.read()

    soup = BeautifulSoup(html_content, 'html.parser')
    
    questions = []
    current_q = None
    
    # Lấy tất cả các thẻ p (paragraph) vì Google Docs xuất mỗi dòng là một thẻ p
    paragraphs = soup.find_all('p')

    # Regex nhận diện câu hỏi (Bắt đầu bằng số và dấu chấm/hai chấm. VD: "1.", "Câu 1:")
    question_pattern = re.compile(r'^(Câu\s*)?\d+[\.:]\s*')
    # Regex nhận diện đáp án (Bắt đầu bằng a,b,c,d. VD: "a.", "A.")
    option_pattern = re.compile(r'^[a-dA-D][\.:]\s*')

    for p in paragraphs:
        text = p.get_text().strip()
        if not text:
            continue

        # --- XỬ LÝ CÂU HỎI ---
        if question_pattern.match(text):
            # Lưu câu hỏi trước đó nếu có
            if current_q:
                questions.append(current_q)
            
            # Tạo câu hỏi mới
            clean_text = question_pattern.sub('', text).strip() # Loại bỏ "Câu 1:"
            current_q = {
                "id": len(questions) + 1,
                "type": "single",
                "text": clean_text,
                "code": "",
                "options": [],
                "correctAnswers": [],
                "explanation": "", 
                "slideRef": ""
            }

        # --- XỬ LÝ ĐÁP ÁN ---
        elif current_q and option_pattern.match(text):
            current_q['options'].append(text)
            
            # Logic tìm đáp án đúng:
            # Kiểm tra xem trong dòng này (thẻ p) có thẻ con nào được in đậm/tô màu không
            is_correct = False
            
            # Cách 1: Kiểm tra chính thẻ p (ít gặp)
            if is_bold_or_highlighted(p):
                is_correct = True
            
            # Cách 2: Kiểm tra các thẻ con (span, b, strong) bên trong
            else:
                for child in p.find_all(['span', 'b', 'strong']):
                    if is_bold_or_highlighted(child):
                        is_correct = True
                        break
            
            if is_correct:
                current_q['correctAnswers'].append(text)

        # --- XỬ LÝ GIẢI THÍCH / SLIDE (Nếu có) ---
        elif current_q:
            lower_text = text.lower()
            if "giải thích" in lower_text or "lời giải" in lower_text:
                current_q['explanation'] = text
            elif "chương" in lower_text or "slide" in lower_text:
                current_q['slideRef'] = text

    # Lưu câu hỏi cuối cùng
    if current_q:
        questions.append(current_q)

    # --- XUẤT FILE .JS ---
    js_content = "export const questions = " + json.dumps(questions, ensure_ascii=False, indent=2) + ";"
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(js_content)
    
    print(f"Đã chuyển đổi thành công {len(questions)} câu hỏi sang {output_path}")

# Chạy chương trình
# Lưu ý: Đổi tên file bên dưới thành tên file thực tế của bạn
parse_html_to_js('Quntrhc.html', 'questions.js')
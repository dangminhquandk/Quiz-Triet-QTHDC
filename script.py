import re
import json
import csv

def clean_and_parse_data(file_path):
    """
    Hàm đọc file thô, làm sạch nhiễu và trích xuất cấu trúc câu hỏi/đáp án.
    Áp dụng tư duy xử lý ngôn ngữ tự nhiên (NLP) cơ bản.
    """
    
    # 1. ĐỌC DỮ LIỆU (EXTRACT)
    with open(file_path, 'r', encoding='utf-8') as f:
        raw_content = f.read()

    # 2. LÀM SẠCH DỮ LIỆU (TRANSFORM - STEP 1: CLEANING)
    # Loại bỏ các thẻ và đánh dấu trang
    content = re.sub(r'\\', '', raw_content)
    content = re.sub(r'--- PAGE \d+ ---', '', content)
    
    # Loại bỏ các dòng trắng thừa và khoảng trắng đầu/cuối dòng
    lines = [line.strip() for line in content.split('\n') if line.strip()]

    # 3. PHÂN TÍCH CÚ PHÁP (TRANSFORM - STEP 2: PARSING)
    # Sử dụng logic Máy trạng thái (State Machine) đơn giản
    questions = []
    current_question = None
    current_key = None # 'question_text' hoặc 'a', 'b', 'c', 'd'

    # Regex patterns
    # Pattern nhận diện câu hỏi: "Câu 1.", "Câu 1:", "Câu 01"
    question_pattern = re.compile(r'^Câu\s+(\d+)[\.:]?\s*(.*)', re.IGNORECASE)
    # Pattern nhận diện đáp án: "a.", "b)", "c."
    option_pattern = re.compile(r'^([a-d])[\.:\)]\s*(.*)', re.IGNORECASE)

    for line in lines:
        # Kiểm tra xem dòng có phải bắt đầu một câu hỏi mới không
        q_match = question_pattern.match(line)
        if q_match:
            # Nếu đang có câu hỏi cũ, lưu lại trước khi qua câu mới
            if current_question:
                questions.append(current_question)
            
            # Khởi tạo câu hỏi mới
            q_number = q_match.group(1)
            q_content = q_match.group(2)
            current_question = {
                "id": q_number,
                "question": q_content,
                "a": "", "b": "", "c": "", "d": ""
            }
            current_key = "question"
            continue

        # Kiểm tra xem dòng có phải là một đáp án (a, b, c, d) không
        o_match = option_pattern.match(line)
        if o_match and current_question:
            opt_label = o_match.group(1).lower() # a, b, c, d
            opt_content = o_match.group(2)
            
            current_question[opt_label] = opt_content
            current_key = opt_label
            continue

        # Xử lý trường hợp nội dung bị ngắt dòng (Mult-line content)
        # Nếu dòng không phải câu hỏi, không phải đáp án, thì nó là phần tiếp theo của nội dung trước đó
        if current_question and current_key:
            # Nối thêm vào nội dung đang xét (xử lý việc xuống dòng giữa câu trong PDF)
            if current_key == "question":
                current_question["question"] += " " + line
            else:
                current_question[current_key] += " " + line

    # Lưu câu hỏi cuối cùng
    if current_question:
        questions.append(current_question)

    return questions

def save_to_json(data, output_file):
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    print(f"-> Đã xuất dữ liệu ra JSON: {output_file}")

def save_to_csv(data, output_file):
    if not data: return
    keys = ["id", "question", "a", "b", "c", "d"]
    with open(output_file, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(data)
    print(f"-> Đã xuất dữ liệu ra CSV (Excel): {output_file}")

# --- MAIN EXECUTION ---
if __name__ == "__main__":
    # Giả lập input từ dữ liệu bạn cung cấp (bạn hãy lưu nội dung PDF vào file này)
    input_filename = 'raw_data.txt' 
    
    # Để test ngay, bạn có thể tạo file raw_data.txt và paste nội dung vào, 
    # hoặc script sẽ báo lỗi nếu không tìm thấy file.
    try:
        print("Đang xử lý dữ liệu...")
        parsed_data = clean_and_parse_data(input_filename)
        
        print(f"Đã trích xuất thành công {len(parsed_data)} câu hỏi.")
        
        # Xuất ra 2 định dạng phổ biến
        save_to_json(parsed_data, 'output_data.json')
        save_to_csv(parsed_data, 'output_data.csv')
        
    except FileNotFoundError:
        print(f"Lỗi: Không tìm thấy file '{input_filename}'. Hãy copy nội dung text từ PDF vào file này.")
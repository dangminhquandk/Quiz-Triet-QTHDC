import re
import json

SOURCE_FILE = 'question_QTHĐC.js'
DUPLICATE_FILE = 'duplicates_QTHĐC.js'

def extract_duplicates(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # Sử dụng Regex để bắt trọn vẹn từng block đối tượng {}
    # Lưu ý: Pattern này giả định cấu trúc file của bạn đồng nhất như trong ảnh
    pattern = re.compile(r'\{\s*id:.*?\s*question:.*?\s*options:\{.*?\s*\}.*?\s*answer:.*?\s*\},', re.DOTALL)
    blocks = pattern.findall(content)

    question_map = {}
    duplicates = []

    for block in blocks:
        # Trích xuất nội dung câu hỏi để làm khóa (Key) so sánh
        q_match = re.search(r'question:\s*"(.*?)",', block)
        if q_match:
            question_text = q_match.group(1).strip()
            
            if question_text in question_map:
                # Nếu đã tồn tại, đây là câu bị trùng
                duplicates.append(block)
                # Bạn có thể chọn lưu cả câu đầu tiên bị trùng nếu muốn
                if question_map[question_text] is not None:
                    duplicates.append(question_map[question_text])
                    question_map[question_text] = None # Đánh dấu để không thêm lại câu gốc
            else:
                # Lưu block lại để đối chiếu sau này
                question_map[question_text] = block

    # Ghi ra file mới
    with open(DUPLICATE_FILE, 'w', encoding='utf-8') as f:
        f.write("const duplicates = [\n")
        f.write("\n".join(duplicates))
        f.write("\n];")
    
    print(f"✅ Đã tìm thấy {len(duplicates)} block trùng lặp và lưu vào {DUPLICATE_FILE}")

if __name__ == "__main__":
    extract_duplicates(SOURCE_FILE)
import re

# Tên file cần sửa (theo ảnh của bạn)
# FILE_NAME = 'question_QTHĐC.js'
FILE_NAME = 'question_QTHĐC.js'

def reindex_ids(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        new_lines = []
        current_id = 1
        
        # Regex tìm pattern "id: <số>," - linh hoạt với khoảng trắng
        id_pattern = re.compile(r'(id:\s*)\d+(,?)')

        for line in lines:
            # Kiểm tra xem dòng đó có chứa từ khoá id không
            if 'id:' in line:
                # Thay thế số cũ bằng current_id, giữ nguyên phần tiền tố và dấu phẩy
                new_line = id_pattern.sub(rf'\g<1>{current_id}\g<2>', line)
                new_lines.append(new_line)
                current_id += 1
            else:
                new_lines.append(line)

        with open(filename, 'w', encoding='utf-8') as f:
            f.writelines(new_lines)
            
        print(f"✅ Đã chuẩn hoá xong {current_id - 1} IDs từ 1 đến cuối!")
    except Exception as e:
        print(f"❌ Lỗi: {e}")

if __name__ == "__main__":
    reindex_ids(FILE_NAME)
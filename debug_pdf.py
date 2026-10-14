import pdfplumber

# Đổi tên file cho đúng với file của bạn
INPUT_PDF = "data.pdf" 

print(f"🕵️‍♂️ Đang soi dữ liệu bên trong file: {INPUT_PDF}...\n")

with pdfplumber.open(INPUT_PDF) as pdf:
    # Chỉ lấy trang đầu tiên để test
    page = pdf.pages[0]
    
    # Lấy 15 dòng đầu tiên
    rows = page.extract_text_lines(return_chars=True, x_tolerance=2)[:15]
    
    for i, row in enumerate(rows):
        text = row['text'].strip()
        print(f"--- Dòng {i+1}: {text} ---")
        
        # Chỉ soi kỹ những dòng là đáp án (bắt đầu bằng a, b, c, d)
        if len(text) > 0:
            # Lấy mẫu 3 ký tự đầu tiên của dòng để xem thuộc tính
            chars = row['chars'][:3] 
            for char in chars:
                print(f"   [Ký tự '{char['text']}'] -> Font: {char.get('fontname')} | Màu (Color): {char.get('non_stroking_color')}")
        print("-" * 50)
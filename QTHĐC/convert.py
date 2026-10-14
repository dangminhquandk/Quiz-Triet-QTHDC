import pdfplumber
import re
import json

def parse_pdf_to_js(pdf_path, start_q=4, end_q=20):
    questions = []
    
    # Text mapping for options (to add a. b. c. d.)
    option_labels = ['a.', 'b.', 'c.', 'd.', 'e.', 'f.']

    with pdfplumber.open(pdf_path) as pdf:
        full_text = ""
        # Loop through pages that likely contain Q4-Q20. 
        # Based on the text dump, Q4 is on page 2, Q20 is on page 9.
        # We'll read a safe range, e.g., pages 1 to 12.
        for i in range(1, 13): 
            try:
                page = pdf.pages[i]
                text = page.extract_text()
                if text:
                    full_text += text + "\n"
            except IndexError:
                break

    # Regex to split questions. 
    # Questions start with a number followed by a dot (e.g., "4.").
    # We look for a newline, then digits, then a dot.
    # Note: Sometimes extracted text might not have a newline before the number if it's the start of a page.
    # We will assume standard formatting from the dump.
    
    # Pattern explanation:
    # \n\s*(\d+)\.\s+ : Matches newline, optional space, capturing group for number, dot, space.
    split_pattern = r'\n(?=\d+\.\s)'
    raw_blocks = re.split(split_pattern, full_text)

    # Filter for blocks that actually start with a number and fall in range
    for block in raw_blocks:
        block = block.strip()
        if not block:
            continue
            
        # Extract ID
        match_id = re.match(r'^(\d+)\.', block)
        if not match_id:
            continue
            
        q_id = int(match_id.group(1))
        
        if start_q <= q_id <= end_q:
            lines = block.split('\n')
            
            # 1. Extract Question Text
            # Usually the first line (minus the id) and maybe subsequent lines until options start
            q_text_lines = []
            option_start_index = -1
            
            # Common checkbox characters in PDF: ☐, ☑, or sometimes just box characters
            # We look for lines starting with these symbols to identify options
            box_chars = ['☐', '☑', '☒', 'O', 'o'] 
            
            for idx, line in enumerate(lines):
                clean_line = line.strip()
                # Check if this line looks like an option
                is_option = False
                for char in box_chars:
                    if clean_line.startswith(char):
                        is_option = True
                        break
                
                # Also check for "Correct" or "Incorrect" markers which might appear before options
                if "Đúng" in clean_line or "Không chính xác" in clean_line or "Điểm" in clean_line:
                    continue # Skip score/status lines for the text
                    
                if is_option:
                    option_start_index = idx
                    break
                
                # If line is just the ID line
                if idx == 0:
                    # Remove "4. " from "4. Question text..."
                    content = re.sub(r'^\d+\.\s*', '', clean_line)
                    q_text_lines.append(content)
                else:
                    q_text_lines.append(clean_line)
            
            question_text = " ".join(q_text_lines).strip()
            
            # 2. Extract Options and Answer
            options_raw = []
            correct_answer_text = []
            
            if option_start_index != -1:
                # Identify if the question was answered correctly or incorrectly by looking at the block text
                # Note: This is tricky because the status might be *above* or *below* the options in the text stream.
                # In the provided dump, status often appears *before* the next question or interleaved.
                # Example: "X Không chính xác" or "✓ Đúng".
                
                # Check for "Checked" box symbol
                checked_marker = '☑' 
                correct_status_marker = 'Đúng'
                
                # Find all lines that are options
                current_option_idx = 0
                for line in lines[option_start_index:]:
                    clean_line = line.strip()
                    # Skip empty or status lines
                    if not clean_line or "Điểm" in clean_line or re.match(r'^\d+:\d+', clean_line): # Skip timestamps
                        continue
                        
                    # Check if it starts with a box char
                    is_opt = False
                    for char in box_chars:
                        if clean_line.startswith(char):
                            is_opt = True
                            # Remove the box char
                            opt_text = clean_line[1:].strip()
                            
                            # Add label (a., b., etc.)
                            label = option_labels[current_option_idx] if current_option_idx < len(option_labels) else ""
                            formatted_opt = f"{label} {opt_text}"
                            options_raw.append(formatted_opt)
                            
                            # Determine if this is the correct answer
                            # Logic: If the box is CHECKED (☑) AND the question status is CORRECT ("Đúng"), then this is the answer.
                            # If the question status is INCORRECT, the checked box is WRONG.
                            # Limitation: We might not know the correct answer if the user got it wrong.
                            
                            if clean_line.startswith(checked_marker):
                                # Check if the block contains "Đúng" (Success)
                                if "✓ Đúng" in block or "☑ Đúng" in block or ( "Đúng" in block and "Không chính xác" not in block):
                                    correct_answer_text.append(formatted_opt)
                            
                            current_option_idx += 1
                            break
            
            # Construct the object
            q_obj = {
                "id": q_id,
                "type": "single",
                "text": question_text,
                "code": "",
                "options": options_raw,
                "correctAnswers": correct_answer_text 
            }
            questions.append(q_obj)

    return questions

# Execute parsing
quiz_data = parse_pdf_to_js("copy.pdf")

# Generate JS file content
js_content = "export const quizData = [\n"
for q in quiz_data:
    js_content += "  {\n"
    js_content += f"    id: {q['id']},\n"
    js_content += f"    type: \"{q['type']}\",\n"
    js_content += f"    text: {json.dumps(q['text'], ensure_ascii=False)},\n"
    js_content += f"    code: \"\",\n"
    js_content += "    options: [\n"
    for opt in q['options']:
        js_content += f"      {json.dumps(opt, ensure_ascii=False)},\n"
    js_content += "    ],\n"
    js_content += "    correctAnswers: [\n"
    for ans in q['correctAnswers']:
        js_content += f"      {json.dumps(ans, ensure_ascii=False)},\n"
    js_content += "    ]\n"
    js_content += "  },\n"
js_content += "];"

print(js_content)
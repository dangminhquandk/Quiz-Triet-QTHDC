const fs = require('fs');

// Tên file của bạn
const FILENAME = 'question_QTHĐC.js';

try {
    // 1. Đọc nội dung file
    let content = fs.readFileSync(FILENAME, 'utf8');

    // Mẹo: Cắt bỏ phần "window.QUESTIONS =" để lấy mảng dữ liệu thô
    // Chúng ta dùng eval() vì đây là file dữ liệu tin cậy của chính bạn
    // Điều này giúp parse được cả object key không có ngoặc kép (id: 1 vs "id": 1)
    const rawDataString = content.replace(/window\.QUESTIONS\s*=\s*/, '').replace(/;\s*$/, '');
    let data = eval(rawDataString);

    console.log(`🔍 Đã tìm thấy ${data.length} câu hỏi. Đang tiến hành chuẩn hoá...`);

    // 2. Vòng lặp Transform (Chuyển đổi dữ liệu)
    const normalizedData = data.map((item, index) => {
        let newItem = { ...item }; // Copy item để tránh mutate trực tiếp

        // --- NHIỆM VỤ 1: CHUẨN HOÁ ID ---
        newItem.id = index + 1;

        // --- NHIỆM VỤ 2: CHUẨN HOÁ OPTIONS TỪ OBJECT -> ARRAY ---
        // Phát hiện nếu options đang là Object {a: "...", b: "..."}
        if (newItem.options && !Array.isArray(newItem.options) && typeof newItem.options === 'object') {
            
            // Chuyển đổi {a: "val"} -> ["a. val"]
            const newOptionsArray = [];
            const keyMap = {}; // Lưu mapping để tí nữa sửa đáp án (vd: 'a' -> 'a. Nội dung')

            Object.entries(newItem.options).forEach(([key, value]) => {
                const fullString = `${key}. ${value}`; // Tạo chuỗi chuẩn "a. Nội dung"
                newOptionsArray.push(fullString);
                keyMap[key] = fullString;
            });

            newItem.options = newOptionsArray;

            // --- NHIỆM VỤ 3: CHUẨN HOÁ ĐÁP ÁN ---
            // Nếu đáp án cũ là "a", "b"... thì map sang text đầy đủ
            if (newItem.answer && typeof newItem.answer === 'string') {
                const correctKey = newItem.answer.trim().toLowerCase();
                if (keyMap[correctKey]) {
                    newItem.correctAnswers = [keyMap[correctKey]];
                } else {
                    newItem.correctAnswers = []; // Fallback nếu không tìm thấy
                }
                // Xóa trường 'answer' cũ đi cho sạch
                delete newItem.answer;
            }
        }

        // --- NHIỆM VỤ 4: ĐỔI TÊN TRƯỜNG QUESTION -> TEXT (Nếu cần) ---
        if (newItem.question && !newItem.text) {
            newItem.text = newItem.question;
            delete newItem.question;
        }
        
        // Đảm bảo type luôn có
        if (!newItem.type) newItem.type = "single";

        return newItem;
    });

    // 3. Ghi lại file (Format lại cho đẹp)
    // JSON.stringify sẽ tự động thêm ngoặc kép vào key ("id": 1), điều này vẫn đúng cú pháp JS
    const outputContent = `window.QUESTIONS = ${JSON.stringify(normalizedData, null, 2)};`;

    fs.writeFileSync(FILENAME, outputContent, 'utf8');

    console.log(`✅ Đã chuẩn hoá thành công ${normalizedData.length} câu hỏi!`);
    console.log(`   - Toàn bộ options đã chuyển về mảng [].`);
    console.log(`   - Toàn bộ ID đã được đánh số lại từ 1.`);
    console.log(`   - Dữ liệu cũ đã được nâng cấp lên cấu trúc mới.`);

} catch (err) {
    console.error("❌ Có lỗi xảy ra:", err.message);
    console.log("👉 Gợi ý: Kiểm tra xem file gốc có đúng cú pháp JS object không.");
}
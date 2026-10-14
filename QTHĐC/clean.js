const fs = require('fs');
const path = require('path');

// Tên file của bạn
const targetFileName = 'question_QTHĐC.js';
const filePath = path.join(__dirname, targetFileName);

console.log(`[System] Đang xử lý file: ${targetFileName}...`);

fs.readFile(filePath, 'utf8', (err, data) => {
    if (err) {
        console.error("Lỗi đọc file:", err);
        return;
    }

    // --- CẢI TIẾN KỸ THUẬT ---
    // (explanation|slideRef) : Tìm key
    // \s*:\s* : Dấu hai chấm
    // (['"`])                : Bắt dấu mở chuỗi (ngoặc đơn, kép, hoặc backtick)
    // [\s\S]*?               : QUAN TRỌNG NHẤT - Lấy tất cả ký tự bao gồm cả xuống dòng (non-greedy)
    // \2                     : Dấu đóng chuỗi tương ứng
    // ,?                     : Dấu phẩy (nếu có)
    // \s*(\r?\n)?            : Khoảng trắng và dấu xuống dòng thừa
    
    const regex = /(explanation|slideRef)\s*:\s*(['"`])[\s\S]*?\2,?\s*(\r?\n)?/g;

    // Thay thế bằng chuỗi rỗng
    const result = data.replace(regex, '');

    fs.writeFile(filePath, result, 'utf8', (err) => {
        if (err) console.error("Lỗi ghi file:", err);
        else console.log("Done. Đã xoá sạch explanation và slideRef bất chấp xuống dòng.");
    });
});
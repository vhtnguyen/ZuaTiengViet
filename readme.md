# Zua Tiếng Việt

Đây là một ứng dụng đơn giản mình viết để dùng làm mini game cho phần thuyết trình của nhóm mình trong các môn chính trị. Ý tưởng lấy từ các câu hỏi đoán từ bị xáo trộn kí tự trong game show Vua Tiếng Việt. Xử lý chính của chương trình là đọc file, xử lý câu hỏi, đưa ra gợi ý và kiểm tra đáp án. Ứng dụng được viết bằng `python 3.8` với `PyQt5` cho phần UI (kinh nghiệm: muốn làm mấy mini app kiểu này nên làm bằng wpf gọn và đẹp hơn).

## Chuẩn bị câu hỏi

Các bạn lưu câu hỏi vào file `ques.txt` với format :

- Dòng đầu tiên là 1 số nguyên tổng số câu hỏi trong trò chơi. eg: Trò chơi có tất cả 3 câu hỏi thì dòng 1 bạn ghi số `3`.

- Mỗi 2 dòng tiếp theo sẽ tương ứng với input cho 1 câu hỏi:
  - Dòng thứ nhất : Một câu chứa keyword muốn hỏi (có thể là full đáp án cũng được).
  - Dòng thứ 2: keyword cần phải đoán.

- Chương trình sẽ tự xử lý đếm kí tự, ẩn và xáo trộn các kí tự trong keyword.

eg: với input:

    Tôi có một con gà mái đẻ trứng vàng
    con gà mái
Ta sẽ được 1 câu hỏi như thế này:

![demo question](screenshots/Screenshot%202023-01-30%20232159.png)

## Usage

1. Chạy file `ZuaTiengViet.py` để khởi động trò chơi.
2. Đọc qua `Luật chơi` để xem hướng dẫn.
3. Mỗi câu hỏi sẽ được gợi ý 2 lần. Nhập đáp án vào ô `Đáp án` (không phân biệt hoa thường) và nhấn phím `enter` để kiểm tra đáp án.

## Demo

![main menu](screenshots/Screenshot%202023-01-30%20235015.png)

![introduction](screenshots/Screenshot%202023-01-30%20235111.png)

![playing](screenshots/Screenshot%202023-01-30%20235409.png)

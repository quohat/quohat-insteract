# Quohat Insteract

Tương tác với bài viết trên **Instagram** theo *#hashtag*

### Tính năng

- Thích *ảnh* mới nhất.
- Theo dõi người đăng.
- Bình luận dựa trên mô tả ảnh của Instagram.
- Chuyển sang ảnh tiếp theo.

### Hướng dẫn sử dụng
- Mở tệp `quohat-insteract.py`.

- Chỉnh sửa `my_username` và `my_password` thành tài khoản Instagram của bạn.

- Chỉnh sửa `hashtag_list` và `n` (số lượng ảnh ở mỗi hashtag) theo ý của bạn.

- Tải `chromedriver` kèm theo trong repo và chỉnh sửa đường dẫn đến nó ở dòng `browser = webdriver.Chrome(executable_path='./chromedriver')`. (Chúng tôi đặt nó trong cùng thư mục với tệp `quohat-insteract.py` nên dễ dàng dùng *đường dẫn tương đối*.)

May thay, những cái cần sửa nhất nằm ở đầu tệp. Nhưng tiếng Anh và sự nhạy bén của bạn phải đủ tốt để tìm thấy những chỗ **bạn** cần sửa và sửa đúng cú pháp ;)

### Yêu cầu cài đặt

- [Python 3](https://www.python.org/)
- Package [selenium](https://pypi.org/project/selenium/) 3.141.0
- chromedriver kèm theo trong repo. (Xin cảm ơn Google và xin lỗi vì chúng tôi quên mất tên phiên bản.)

### Bản quyền

Tệp `quohat-insteract.py` được viết dưới bản quyền Mozilla Public License Version 2.0. Xem chi tiết ở tệp `LICENSE` trong repo.

<p align="center">
<img src="/quohat-logo.png" alt="Quohat Team Logo"
</p>

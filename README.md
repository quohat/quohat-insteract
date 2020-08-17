# Quohat Insteract

Tương tác với bài viết trên **Instagram** theo *#hashtag*

### Tính năng

- Thích *ảnh* mới nhất.
- Theo dõi người đăng.
- Bình luận dựa trên mô tả ảnh của Instagram.
- Chuyển sang ảnh tiếp theo.

### Hướng dẫn sử dụng
- Tải `quohat-insteract.py` và `chromedriver` (cho Linux) hoặc `chromedriver.exe` (cho Windows) hoặc `chromedriver_mac64.zip` (cho Mac, cần giải nén để có tệp `chromedriver`) trong repo xuống.

- Mở tệp `quohat-insteract.py`.

- Chỉnh sửa `my_username` và `my_password` thành tài khoản Instagram của bạn.

- Chỉnh sửa `hashtag_list` và `n` (số lượng ảnh ở mỗi hashtag) theo ý của bạn.

- Chỉnh sửa đường dẫn đến chromedriver ở dòng `browser = webdriver.Chrome(executable_path='./chromedriver')`. (Chúng tôi đặt nó trong cùng thư mục với tệp `quohat-insteract.py` nên dễ dàng dùng *đường dẫn tương đối*.)

May thay, những cái cần sửa nhất nằm ở đầu tệp. Nhưng tiếng Anh và sự nhạy bén của bạn phải đủ tốt để tìm thấy những chỗ **bạn** cần sửa và sửa đúng cú pháp ;)

- Dùng IDE hoặc editor ưa thích của bạn để chạy. Với console hoặc terminal, sử dụng lệnh `python /pathtofile/quohat-insteract.py`.

> Lưu ý rằng kích thước của sổ của `chromedriver` có thể ảnh hưởng đến thuật toán.

### Yêu cầu cài đặt

- [Python 3](https://www.python.org/)
- Package [selenium](https://pypi.org/project/selenium/) 3.141.0
- chromedriver (84.0.4147.125) kèm theo trong repo. (Xin cảm ơn Google.)

### Bản quyền

Chúng tôi không lưu lại và sử dụng *bất kỳ* thông tin nào của bạn.

Tệp `quohat-insteract.py` được viết dưới bản quyền Mozilla Public License Version 2.0. Xem chi tiết ở tệp `LICENSE` trong repo.

<p align="center">
<img src="/quohat-logo.png" alt="Quohat Team Logo"
</p>

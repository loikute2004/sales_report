
# NON-FUNCTIONAL REQUIREMENTS

## 1. Hiệu năng (Performance)

NFR-01:
95% request danh sách ticket phản hồi dưới 500 ms
với dữ liệu thử nghiệm 10.000 ticket.

NFR-02:
Danh sách ticket hiển thị tối đa 20 bản ghi mỗi trang.

## 2. Bảo mật (Security)

NFR-03:
Mật khẩu người dùng phải được băm trước khi lưu.

NFR-04:
Khách hàng chỉ được xem ticket do chính mình tạo.

NFR-05:
Các chức năng quản lý phải được kiểm soát theo vai trò.

NFR-06:
Hệ thống bắt buộc sử dụng HTTPS khi triển khai production.

## 3. Khả năng vận hành (Operations)

NFR-07:
Dữ liệu phải được sao lưu hằng ngày.

NFR-08:
Thời gian khôi phục dữ liệu mục tiêu không vượt quá 1 giờ.

## 4. Khả năng mở rộng (Scalability)

NFR-09:
Cấu trúc hệ thống cần hỗ trợ bổ sung chức năng
mà không ảnh hưởng đến các module hiện có.

## 5. Khả năng sử dụng (Usability)

NFR-10:
Người dùng mới có thể tạo ticket đầu tiên
trong dưới 2 phút mà không cần hướng dẫn.

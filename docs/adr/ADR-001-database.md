
# ADR-001: Sử dụng PostgreSQL thay vì MySQL

- Ngày: 2026-11-24
- Trạng thái: Accepted

## 1. Bối cảnh

Dự án TicketDesk cần một hệ quản trị cơ sở dữ liệu
để lưu trữ thông tin người dùng, ticket, bình luận
và file đính kèm.

Hệ thống cần đảm bảo tính toàn vẹn dữ liệu,
hỗ trợ truy vấn và có khả năng mở rộng.

## 2. Quyết định

Sử dụng PostgreSQL 16 làm hệ quản trị cơ sở dữ liệu.

PostgreSQL được chạy bằng Docker để đảm bảo
môi trường phát triển thống nhất.

## 3. Hệ quả

Ưu điểm:
- Hỗ trợ tốt Django ORM.
- Có JSONField và khả năng tìm kiếm toàn văn.
- Hỗ trợ transaction.
- Dễ triển khai bằng Docker.

Nhược điểm:
- Thành viên cần làm quen với PostgreSQL.
- Cần quản lý backup và cấu hình database.

## 4. Trạng thái

Đã chấp nhận.

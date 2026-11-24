
# TicketDesk REST API Specification

Base URL: /api

## 1. Authentication

| Method | Endpoint | Description | Status |
|---|---|---|---|
| POST | /auth/login/ | Đăng nhập | 200 |
| POST | /auth/logout/ | Đăng xuất | 204 |

## 2. Tickets

| Method | Endpoint | Description | Status |
|---|---|---|---|
| GET | /tickets/ | Lấy danh sách ticket | 200 |
| POST | /tickets/ | Tạo ticket | 201 |
| GET | /tickets/{id}/ | Xem chi tiết ticket | 200, 404 |
| PATCH | /tickets/{id}/ | Cập nhật ticket | 200, 400 |
| DELETE | /tickets/{id}/ | Xóa ticket | 204, 404 |
| POST | /tickets/{id}/assign/ | Gán nhân viên xử lý | 200, 409 |
| POST | /tickets/{id}/close/ | Đóng ticket | 200, 409 |

## 3. Comments

| Method | Endpoint | Description | Status |
|---|---|---|---|
| GET | /tickets/{id}/comments/ | Lấy bình luận | 200 |
| POST | /tickets/{id}/comments/ | Thêm bình luận | 201 |

## 4. Categories

| Method | Endpoint | Description | Status |
|---|---|---|---|
| GET | /categories/ | Lấy danh mục | 200 |

## 5. Attachments

| Method | Endpoint | Description | Status |
|---|---|---|---|
| POST | /tickets/{id}/attachments/ | Tải file lên | 201 |

## 6. Pagination

GET /tickets/?page=2&page_size=20

## 7. Filtering

GET /tickets/?status=new

GET /tickets/?priority=3

## 8. Error Response

{
  "detail": "Ticket đã đóng",
  "code": "ticket_closed"
}

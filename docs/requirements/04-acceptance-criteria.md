
Feature: TicketDesk

  # US-01: Đăng nhập

  Scenario: Đăng nhập thành công
    Given người dùng đã có tài khoản hợp lệ
    When người dùng nhập đúng username và password
    Then hệ thống cho phép đăng nhập
    And chuyển đến trang chính

  Scenario: Đăng nhập thất bại
    Given người dùng đang ở trang đăng nhập
    When người dùng nhập sai thông tin
    Then hệ thống hiển thị thông báo lỗi

  # US-02: Đăng xuất

  Scenario: Đăng xuất thành công
    Given người dùng đang đăng nhập
    When người dùng chọn đăng xuất
    Then hệ thống kết thúc phiên đăng nhập
    And chuyển về trang đăng nhập

  # US-03: Tạo ticket

  Scenario: Tạo ticket hợp lệ
    Given khách hàng đã đăng nhập
    When khách hàng nhập tiêu đề và mô tả hợp lệ
    And chọn danh mục ticket
    Then hệ thống tạo ticket mới
    And ticket có trạng thái "Mới"

  Scenario: Tạo ticket thiếu tiêu đề
    Given khách hàng đang tạo ticket
    When khách hàng không nhập tiêu đề
    Then hệ thống thông báo lỗi
    And không tạo ticket

  # US-04: Xem danh sách ticket

  Scenario: Xem danh sách ticket
    Given khách hàng đã đăng nhập
    When khách hàng truy cập danh sách ticket
    Then hệ thống hiển thị các ticket do khách hàng tạo

  # US-05: Xem chi tiết ticket

  Scenario: Xem ticket của mình
    Given khách hàng có ticket TD-01
    When khách hàng mở TD-01
    Then hệ thống hiển thị thông tin chi tiết

  Scenario: Xem ticket không thuộc quyền truy cập
    Given ticket không thuộc quyền truy cập của khách hàng
    When khách hàng cố mở ticket đó
    Then hệ thống từ chối truy cập

  # US-06: Lọc ticket

  Scenario: Lọc theo trạng thái
    Given nhân viên đang ở danh sách ticket
    When nhân viên chọn trạng thái "Mới"
    Then hệ thống chỉ hiển thị ticket phù hợp

  # US-07: Gán ticket

  Scenario: Gán ticket thành công
    Given ticket TD-42 đang ở trạng thái "Mới"
    When quản lý gán ticket cho nhanvien01
    Then người xử lý là nhanvien01
    And trạng thái chuyển thành "Đang xử lý"
    And nhân viên nhận email thông báo

  Scenario: Gán ticket đã đóng
    Given ticket TD-43 đang ở trạng thái "Đã đóng"
    When quản lý gán ticket cho nhanvien01
    Then hệ thống báo lỗi "Ticket đã đóng"
    And ticket không thay đổi

  # US-08: Cập nhật trạng thái

  Scenario: Cập nhật trạng thái hợp lệ
    Given nhân viên được phân công ticket
    When nhân viên cập nhật trạng thái
    Then hệ thống lưu trạng thái mới

  # US-09: Bình luận

  Scenario: Thêm bình luận
    Given người dùng có quyền truy cập ticket
    When người dùng nhập nội dung bình luận hợp lệ
    Then hệ thống lưu bình luận vào ticket

  # US-10: Đính kèm tệp

  Scenario: Upload tệp hợp lệ
    Given khách hàng đang tạo ticket
    When khách hàng tải lên tệp được hỗ trợ
    Then hệ thống lưu tệp đính kèm

  Scenario: Upload tệp không hợp lệ
    Given khách hàng đang tạo ticket
    When khách hàng tải lên tệp không được hỗ trợ
    Then hệ thống thông báo lỗi

  # US-11: Dashboard

  Scenario: Xem thống kê
    Given quản lý đã đăng nhập
    When quản lý mở Dashboard
    Then hệ thống hiển thị thống kê ticket

  # US-12: Xuất báo cáo

  Scenario: Xuất Excel
    Given quản lý có quyền xuất báo cáo
    When quản lý yêu cầu xuất dữ liệu
    Then hệ thống tạo báo cáo Excel

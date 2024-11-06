# Visa Management Platform

## Tổng quan
Visa Management Platform là một module quản lý quy trình xin visa end-to-end, tích hợp với các module có sẵn của Odoo để tạo ra một quy trình làm việc liền mạch từ lead đến việc hoàn thành hồ sơ visa.

## Tính năng chính

### 1. Quản lý Khách hàng (CRM)
- Tích hợp với module CRM của Odoo
- Chuyển đổi lead thành hồ sơ visa
- Theo dõi trạng thái khách hàng từ lead đến khi hoàn thành visa
- Lưu trữ thông tin cá nhân và hộ chiếu của khách hàng

### 2. Quản lý Loại Visa
- Cấu hình các loại visa khác nhau (du lịch, học tập, làm việc...)
- Định nghĩa thời hạn và phí cho từng loại visa
- Thiết lập quy trình chuẩn cho từng loại visa
- Quản lý template nhiệm vụ cho từng loại visa

### 3. Quy trình Xử lý Visa
- Workflow tự động từ draft → submitted → under review → approved/rejected
- Tích hợp checklist dựa trên Survey module
- Tự động tạo nhiệm vụ từ template cho nhân viên
- Theo dõi tiến độ xử lý hồ sơ

### 4. Quản lý Tài chính
- Tự động tạo đơn hàng (Sale Order)
- Tự động xuất hóa đơn (Invoice)
- Tích hợp với module Contract để quản lý hợp đồng
- Theo dõi thanh toán và doanh thu

### 5. Quản lý Công việc
- Template công việc cho từng loại visa
- Phân công nhiệm vụ cho nhân viên
- Theo dõi tiến độ công việc
- Báo cáo hiệu suất xử lý

## Cấu trúc Module

### Models
1. visa.application: Quản lý hồ sơ visa
2. visa.type: Định nghĩa loại visa
3. visa.category: Phân loại visa
4. visa.stage: Các giai đoạn xử lý
5. visa.visa: Thông tin visa đã cấp

### Tích hợp
- CRM Module
- Sales Management
- Invoicing
- Project Management
- Survey Module
- Contract Management

## Quy trình làm việc

### 1. Tiếp nhận khách hàng
- Tạo lead trong CRM
- Ghi nhận thông tin cơ bản
- Xác định loại visa phù hợp

### 2. Tạo hồ sơ visa
- Chuyển đổi lead thành hồ sơ visa
- Tự động tạo các nhiệm vụ từ template
- Gửi checklist cho khách hàng

### 3. Xử lý hồ sơ
- Nhân viên thực hiện các nhiệm vụ được giao
- Cập nhật tiến độ công việc
- Theo dõi checklist và yêu cầu bổ sung

### 4. Tài chính
- Tạo đơn hàng
- Xuất hóa đơn
- Theo dõi thanh toán

### 5. Hoàn thành
- Phê duyệt hồ sơ
- Tạo hợp đồng
- Lưu trữ thông tin visa

## Phân quyền

### 1. Visa Admin
- Quản lý toàn bộ module
- Cấu hình template và quy trình
- Phân quyền cho người dùng

### 2. Company Admin
- Quản lý hồ sơ công ty
- Xem báo cáo tổng hợp
- Phê duyệt hồ sơ

### 3. Sales
- Tạo và quản lý lead
- Tạo hồ sơ visa
- Theo dõi tiến độ

### 4. Advisor
- Tư vấn khách hàng
- Xem thông tin hồ sơ
- Cập nhật trạng thái

### 5. Assistant
- Thực hiện nhiệm vụ được giao
- Cập nhật tiến độ công việc
- Tương tác với khách hàng

## Báo cáo và Thống kê
- Số lượng hồ sơ theo trạng thái
- Thời gian xử lý trung bình
- Doanh thu theo loại visa
- Hiệu suất nhân viên
- Tỷ lệ thành công

## Cấu hình và Tùy chỉnh
- Tùy chỉnh các loại visa
- Thiết lập quy trình làm việc
- Cấu hình template nhiệm vụ
- Tùy chỉnh checklist
- Cấu hình email mẫu

## Yêu cầu hệ thống
- Odoo 16.0
- Các module phụ thuộc: CRM, Sales, Project, Survey, Contract

## Cài đặt và Nâng cấp
1. Cài đặt module và các phụ thuộc
2. Cấu hình các thông số cơ bản
3. Tạo template cho các loại visa
4. Thiết lập quy trình làm việc
5. Phân quyền người dùng 
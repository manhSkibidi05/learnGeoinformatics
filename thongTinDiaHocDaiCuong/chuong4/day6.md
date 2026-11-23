# Review 

1. Câu 1 : Sự khác biệt giữa việc khai báo tham số **Dimension = 3** khi dùng kiểu **POINT** (XYZ) và dùng kiểu **POINTM** (XYM) trong hàm `AddGeometryColumn()` là gì? Giá trị **M** thường dùng cho ứng dụng thực tế nào?

    - Khi khai báo tham số Dimension = 3 khi dùng kiểu POINT (XYZ) và kiểu POINT (XYM) là giá trị cuối cùng của kiểu POINT với XYZ và XY cặp tọa độ Z là giá trị độ cao với đơn vị mét với XYM và XY là cặp tọa độ M là giá trị đo lường 
    -> Giá trị M thường dùng trong ứng dụng : Dữ liệu hành trình GPS -> Giá trị M lưu mốc thời gian , Quản lý hạ tầng giao thông -> Giá trị M biểu diễn cọc cây số dọc theo tuyến đường quốc lộ 

2. Câu 2: Khi khởi tạo một hình đa giác có lỗ thủng (interior ring / hole) bằng `ST_GeomFromText('POLYGON(...)')`, thứ tự khai báo các vòng ranh giới và quy tắc đóng vòng tọa độ được quy định như thế nào?

    - Khi khởi tạo hình đa giác có lỗ thủng bằng bằng hàm ST_GeomFromText('POLYGON(...)') thì thứ tự khai báo vòng ranh giới rất quan trọng với vòng ranh giới bên ngoài được khai báo với ngoặc đầu tiên và vùng ranh giới bên trong nếu có thì sẽ khai báo với ngoặc số 2 không nằm trong ngoặc đầu
    -> Cú pháp : POLYGON((Vòng_bên_ngoài)(vòng_bên_trong1)(vòng_bên_trong2))

3.  Câu 3: Bảng hình học hỗn hợp (**Heterogeneous table** \- dùng kiểu cột `GEOMETRY`) mang lại ưu điểm và nhược điểm gì so với cách thiết kế bảng hình học đồng nhất (**Homogeneous table**)?

    - Bảng hình học hỗn hợp mang ưu điểm so với bảng hình học độc nhất là : 
        + Lưu nhiều loại hình học khác nhau trong 1 cột 
    - Nhược điểm là : 
        + Với các phép toán thực hiện lên toàn bộ 1 cột dữ liệu nhưng kiểu hình học khác nhau có thể gây lỗi 
        + Tương thích kém với các phần mềm GIS như QGIS yêu cầu lớp bản đồ phải đồng nhất một loại hình học 

# Chương 4 : Cơ sở dữ liệu - PostgreSQL + PostGIS

## Giai đoạn 5 : Quản lý khung nhìn (VIEWS) và Trực quan hóa dữ liệu POSTGIS trên QGIS

- Giai đoạn này giúp bạn kết nối toàn bộ hạ tầng CSDL không gian vừa tạo dựng trên PostGIS với phần mềm hiển thị bản đồ chuyên nghiệp QGIS 

1. Khung nhìn View 

- Định nghĩa : Là một bảng ảo được định nghĩa dựa trên kết quả truy vấn từ 1 câu lệnh select -> không lưu trữ dữ liệu trực tiếp mà chỉ lưu trữ câu lệnh truy vấn 
- Tác dụng chính của view : 
    + Đóng gọi các câu lệnh join nhiều bảng , tính toán hình học phức tạp (ST_Buffer , ST_Intersect...) thành bảng ảo gọn gàng để có thể dễ dàng gọi lại 

    + Giới hạn quyền truy cập chỉ cho phép người dùng xem một số cột hoặc hàng nhất định mà không cấp quyền vào bảng gốc 

    + Tạo lớp bản đồ độc lập hiển thị trên QGIS bằng cách tạo view lọc theo điều kiện rồi import vào QGIS

    + Khi cấu trúc bảng gốc thay đổi thì bạn chỉ cần cập nhật lại câu truy vấn của View mà không làm ảnh hưởng đến các phần mềm đang sử dụng nó 

- Phân biệt 2 loại View : 
    + View thông thường : Không lưu trữ dữ liệu , dữ liệu luôn cập nhật theo thời gian thực đổi lại tốc độ truy vấn chậm
    -> sử dụng câu lệnh CREATE VIEW 

    + Materialized View : Có lưu bảng ra ổ cứng thật , dữ liệu cập nhật lại khi chạy lệnh Refresh đổi lại tốc độ truy vấn nhanh và tạo được chỉ mục không gian 
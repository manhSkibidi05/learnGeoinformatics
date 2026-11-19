# Review : 

- Cơ sở dữ liệu : Là tập hợp các dữ liệu một cách có tổ chức , cấu trúc và được lưu trữ trên máy tính 
- Hệ quản trị cơ sở dữ liệu : Là các phầm mềm giúp người dùng quản lý các cơ sở dữ liệu trên máy tính và với các chức năng chính như : thêm , sửa , xóa , truy vấn , phân quyền , bảo mật ...

- PostgreSQL : Là 1 hệ quản trị cơ sở dữ liệu mã nguồn mở , miễn phí có thể mở rộng bằng cách thêm các extension vào nó 
- PostGIS : Là extension của PostgreSQL hỗ trợ cơ sở dữ liệu mở rộng sau : 
    + Thêm các kiểu dữ liệu mới geometry/geography hay raster 
    + Thêm các hàm toán học ST_Distance , ST_Buffer , ST_Area , ST_Intersects...
    + Thêm chỉ mục không gian GIST

# CHương 4 : Cơ sở dữ liệu - PostgreSQL , PostGIS

## Giai đoạn 1 : Khởi tạo CSDL không gian , quản lý SCHEMA và Import dữ liệu (Shapefile/csv)

- Giai đoạn 1 giúp thiết lập hoàn chỉnh môi trường làm việc trên PostgreSQL kết hợp PostGIS thông qua giao diện pgAdmin , đồng thời nắm vững quy trình nạp dữ liệu vào với 2 định dạng phổ biến nhất là shapefile (.shp) và văn bản phân tách dấu phảy (.csv)

### Bước 1 : Kết nối PostgreSQL tạo cơ sở dữ liệu và kích hoạt Extension PostGIS 

    1. Đăng nhập pgadmin sử dụng tài khoản : postgres và mật khẩu : tùy ý 
    2. Tạo database mới bằng lệnh create database
    3. Thêm extension ở chức năng extension nhập vào postgis

### Bước 2 : Khởi tạo Schema 

- Schema trong PostgreSQL đóng vai trò là 1 thùng chứa dùng để phân nhóm các bảng dữ liệu có liên quan đến nhau theo từng dự án 
-> Schema nhóm các bảng dữ liệu có liên quan đến nhau vào chung 1 chỗ 

    1. Tạo schema mới với chức năng schemas create
    2. Nhập tên schema đó

### Bước 3 : Nạp dữ liệu shapefile (.shp)

- Sử dụng công cụ có sẵn nằm trong folder postgreSQL để nạp dữ liệu Shapefile -> shp2pgsql-gui.exe

    1. Thiết lập kết nối tới database gồm nhập các thông tin username , password , database
    2. Chọn tệp với định dạng .shp và cấu hình thông số import là schema , table , geocolumn : geom , srid : 4269

-> Khi nạp dữ liệu từ shapefile bằng công cụ shp2pgsql-gui.exe thì cộng cụ này giúp tự động tạo bảng và tạo sẵn cột chứa dữ liệu không gian tên mặc định thường là geom -> Bản chất là phía bên dưới tự động thực thi câu lệnh SQL giúp tạo bảng dữ liệu rồi đẩy thẳng vào database

### Bước 4 : Nạp dữ liệu csv 

- Khác với shapefile các file .csv không phải định dạng dữ liệu không gian nên cần tạo khung bảng trước khi nạp dữ liệu 

    1. Tạo bảng trống mới 
    2. Tạo các cột dữ liệu tương ứng với số cột dữ liệu của .csv 
    3. Thêm các kiểu dữ liệu tương ứng với các cột đó 
    4. Nạp dữ liệu .csv bằng câu lệnh 'COPY usa.census2020 FROM 'D:\Downloads2\census2020.csv' WITH (FORMAT csv, HEADER True);'
        -> Giải thích thông số FORMAT csv : chỉ định tệp phân cách bằng dấu phảy , HEADER True : báo cho postgres bỏ qua dòng đầu vì nó là tiêu đề 

## Câu hỏi ôn tập 

1. Khi nhập tệp states.shp bằng shp2pgsql-gui , nếu bạn quên ấn enter sau khi điền 4269 thì chuyện gì xảy ra và nó ảnh hưởng thế nào tới khả năng phân tích không gian về sau . 
-> Không ấn enter sau khi điền 4269 thì tức là không chỉ định hệ tọa độ cho dữ liệu không gian được nhập vào , khi không có hệ tọa độ cụ thể thì không thể xác định được giá trị đang mang đơn vị nào 

2. Tùy chọn HEADER True trong câu lệnh COPY có tác dụng tự động ghép tên cột trong tệp CSV với tên cột tương ứng trong bảng PostgreSQL không 
-> Không có tác dụng đó câu lệnh HEADER True bỏ qua dòng đầu vì nó là tiêu đề còn dữ liệu sẽ thêm từ trái sang phải vào từng cột theo thứ tự đó nên cần phải tạo cột đúng so với cấu trúc dữ liệu file .csv 

3. Tại sao khi thiết lập `SET search_path TO usa, public;` ta vẫn phải giữ lại schema `public` thay vì chỉ ghi `SET search_path TO usa;`

-> Khi thêm extension PostGIS vào thì cơ sở dữ liệu sẽ có :
    + Kiểu dữ liệu không gian geometry/geography và raster
    + Các hàm tính toán không gian ST_Distance , ST_Buffer , ST_Area , ST_Intersects
    + Chỉ mục không gian GIST 
-> Muốn thêm bảng dữ liệu có chứa dữ liệu không gian cần thêm cột mang kiểu dữ liệu không gian tên cơ bản là geom 
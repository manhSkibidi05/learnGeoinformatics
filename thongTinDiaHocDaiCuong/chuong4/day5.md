# Review 

- Cơ sở dữ liệu : Là Tập hợp dữ liệu một cách có tổ chức , cấu trúc và được lưu trữ trên máy tính . 
-> Các kiểu dữ liệu thường được lưu trữ : text , số , ảnh , âm thanh ...

- Cơ sở dữ liệu không gian : Giống với cơ sở dữ liệu nhưng được mở rộng thêm với các kiểu dữ liệu mới geometry/geography , raster , ngoài ra còn có thêm các hàm xử lý không gian , chỉ mục không gian...
-> Sử dụng PostgreSQL + Extension PostGIS giúp tạo ra các cơ sở dữ liệu không gian 

- Các hàm cung cấp xử lý không gian cần biết : 

    + ST_AsText() : Sử dụng để chuyển đổi dữ liệu từ dạng hệ thập lục phân khó đọc sang dạng text dễ đọc với người dùng 
    -> Do các hàm tính toán trả về dữ liệu không gian hầu hết trả về dữ liệu dạng thập lục phân nên cần sử dụng hàm này

    + ST_Centroid() : Tính tâm của 1 vùng 

    + ST_Area() : Tính diện tích của 1 vùng 

    + ST_Transform() : Sử dụng để chuyển đổi hệ tọa độ của dữ liệu không gian hiện tại bằng cách nhập dữ liệu không gian đó và mã 
    -> Do các hàm tính toán không quan tâm đến hệ tọa độ của dữ liệu nên cần chuyển sang hệ tọa độ phẳng giúp tính toán 1 cách chính xác

    + ST_AddGeometryColumn() : Sử dụng để thêm 1 cột mang dữ liệu hình học , ngoài ra có thể định nghĩa thêm các tham số cần thiết như mã hệ tham chiếu không gian -> hệ tọa độ , chiều không gian -> 2 , 3, 4 , dạng hình học -> điểm , đường , vùng

    + ST_GeomFromText() : Sử dụng để nhập dữ liệu hình học dạng từ dạng text chuyển sang dạng thập lục phân giúp lưu trữ trong cột dữ liệu không gian của PostGIS 

# Chương 4 : Cơ sở dữ liệu - PostgreSQL + PostGIS 

## Giai đoạn 4 : Quản lý kiểu dữ liệu hình học 

- Định nghĩa dữ liệu không gian (Geodata) : Loại dữ liệu mô tả vị trí , hình dạng và mối quan hệ không gian của các đối tượng / hiện tượng trong không gian thường gắn với tọa độ trên bề mặt trái đất . 

- 3 phần tạo nên dữ liệu không gian = Dữ liệu hình học + Dữ liệu thuộc tính + Hệ quy chiếu địa lý (CRS)
    1. Dữ liệu hình học 
        - Định nghĩa : Là phần định nghĩa hình dạng và cấu trúc liên kết của đối tượng dưới dạng các con số tọa độ thuần thúy 
        -> Trả lời câu hỏi đối tượng trông như thế nào ? 

    2. Dữ liệu thuộc tính 
        - Định nghĩa : Là thông tin phi không gian như văn bản , con số , ngày tháng... được lưu trữ dưới dạng bảng và gắn liền với các đối tượng hình học 
        -> Trả lời câu hỏi đối tượng mang những đặc điểm gì ? 

    3. Hệ quy chiếu địa lý CRS 
        - Định nghĩa : Là bộ quy tắc toán học giúp đặt các con số tọa độ không có ý nghĩa vào một vị trí chính xác trên trái đất với bề mặt cong 
        -> Trả lời câu hỏi đối tượng nằm ở đâu trên trái đất ? 

    -> Từ 3 phần trên tạo nên dữ liệu không gian giúp cung cấp các thông tin về 1 đối tượng địa lý bao gồm hình dạng như thế nào , ở vị trí nào trên trái đất và các đặc điểm như tên gọi ...


3. Cú pháp hình học 3D / 4D và đối tượng đa phần 

    A. Dữ liệu 3D và 4D -> Khác với dữ liệu 2D chỉ xoay quanh X và Y thì dữ liệu 3D và 4D cung cấp thêm dữ liệu Z và M 
        + Giá trị Z : Mô tả độ cao 
            POINT(222 1111 190) -> 190 là độ cao 

        + Giá trị M : Mô tả giá trị đo lường 
            POINTM(232 211 9999) -> 9999 là giá trị đo lường

        + Cả Z và M : XYZM 
            POINT(-73.985744 40.748549 190 9999)

    B. Hình học đa phần - Multipart 
    - Là dữ liệu đại diện cho 1 đối tượng địa lý duy nhất nhưng gồm nhiều phần nằm tách rời nhau 
    -> 1 đối tượng địa lý có thể không phải 1 phần duy nhất mà kết hợp các phần nhỏ với nhau . vd : Đảo , cụm công trình...

    - Các Multipart cần biết : **MULTIPOINT** **,** **MULTILINESTRING** **,** **MULTIPOLYGON**

4. Bảng hình học hỗn hợp - Heterogeneous Geometries 
    - Với các ứng dụng GIS mặc định mang thiết kế đồng nhất là 1 bảng dữ liệu chỉ chứa dữ liệu hình học của 1 loại hình duy nhất như toàn POINT hoặc toàn LINESTRING , toàn POLYGON . Nhưng với PostGIS có hỗ trợ kiểu dữ liệu chung là GEOMETRY cho phép lưu trữ tất cả loại hình học chung 1 cột duy nhất . 

        create table mixed(gid integer PRIMARY KEY , name VARCHAR(50));
        select ST_AddGeometryColumn('nyc_poi' , 'mixed' , 'geom' , 4269 , 'GEOMETRY' , 2);

        insert into mixed(name , geom) 
        value('Empire State Building', ST_GeomFromText('POINT(-73.985744 40.748549)', 4269)),
        ('Holland Tunnel', ST_GeomFromText('LINESTRING(-74.036486 40.730121, -74.011123 40.725958)', 4269)), 
        ('Central Park', ST_GeomFromText('POLYGON((-73.973057 40.764356, -73.981898 40.768094, -73.949282 40.796853, -73.973057 40.764356))', 4269));

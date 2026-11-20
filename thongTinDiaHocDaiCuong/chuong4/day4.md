# Chương 4 : Cơ sở dữ liệu - PostgreSQL , PostGIS 

## Giai đoạn 3 : Phân tích và truy vấn không gian 

- Đây là chương cốt lõi giữa một cơ sở dữ liệu truyền thống và cơ sở dữ liệu không gian (spatial database)
- Ở bài học này chúng ta làm quen với các hàm xử lý không gian PostGIS để xác định tâm hìh học , tính diện tích và thực hiện chuyển độ hệ tọa độ trực tiếp 

1. Điểm khác biệt của CSDL không gian 

    - CSDL quan hệ thông thường chỉ xử lý các loại dữ liệu chữ , số , ảnh ...
    - CSDL không gian (PostgreSQL với extension PostGIS) cho phép lưu trữ trực tiếp các đối tượng hình học và cung cấp hàng trăm các hàm xử lý không gian (spatial functions) giúp trả lời các câu hỏi về hình học (geometric) và quan hệ vị trí (topological)

2. Giới thiệu một vài hàm xử lý không gian cần thiết (spatial functions)

    - ST_Centroid(geom) : Hàm nhận dữ liệu đầu vào là dữ liệu mang kiểu hình học dạng Polygon và trả về dữ liệu là tọa độ 1 điểm , nhưng lại biểu diễn dưới dạng hệ thập lục phân (khó đọc) 
    -> Hàm này giúp tạo ra 1 điểm và điểm đó là tâm của 1 vùng 

    - ST_AsText() : Hàm này sinh ra nhằm xử lý những dữ liệu dạng hệ thập lục phân chuyển thành về dạng giúp con người dễ đọc hơn 
    -> Hàm này sử dụng bằng cách bọc bên ngoài hàm ST_Centroid() từ đó dữ liệu trả về dạng điểm (kinh độ , vĩ độ) 

    - ST_Area(geom) : Hàm này nhận dữ liệu đầu vào là dữ liệu mang kiểu hình học dạng Polygon và trả về dữ liệu số thực , nhưng dữ liệu đầu vào ban đầu có thể đang mang hệ tọa độ địa lý không phù hợp với tính khoảng cách 
    -> Hàm này giúp tính diện tích của 1 vùng 

    - ST_Transform(geom , he_toa_do_moi) : Hàm này sinh ra nhằm thay đổi hệ tọa độ ban đầu dữ liệu đầu vào với một hệ tọa độ mới chỉ định bởi người dùng 
    -> Hàm này thường được bọc bên trong hàm ST_Area() nhằm chuyển đổi hệ tọa độ dữ liệu trước khi tính toán hình học 

3. Bài tập 

    1. Câu 1 : Tính tâm của các bang của usa với điều kiện lần lượt là dân số năm 2020 nhỏ hơn 10tr và hầu hết sử dụng 'Coke' 

        select s.name , s.sub_region , c.total , ST_AsText(ST_Centroid(s.geom)) as centroid from usa.states s join usa.census2020 c on s.name = c.state 
        where c.total < 10000000 and s.sub_region = 'Coke'

    2. Câu 2 : Tính diện tích các bang của usa với điều kiện các bang đó dân số nam > nữ 

        select s.name , c.male , c.female , ST_Area(ST_Transform(s.geom , 2163)) as dien_tich from usa.states s join usa.census2020 c on s.name = c.state 
        where c.male > c.female

## Giai đoạn 4 : Quản lý các kiểu dữ liệu hình học trong POSTGIS (Point , LineString , Polygon , 3D / 4D , Multipart & Heterogeneous geometries) 

- Giai đoạn 4 đi sâu vào bản chất quản trị kiến trúc CSDL không gian : Tự tay tạo bảng không gian trống , cấu hình cột hình học bằng hàm chuyên dụng 
AddGeometryColumn() , khởi tạo trực tiếp các đối tượng 2D , 3D , 4D , Đa phần (Multipart) và hỗn hợp (Heterogeneous)

1. Tạo Schema nyc_poi và cấu hình cột hình học 
- Khác với việc sử dụng shp2pgsql-gui vừa tạo bảng vừa nạp dữ liệu đồng thời , trong lập trình CSDL chuyên nghiệp chúng ta cần tạo bảng thuộc tính trước sau đó mới chèn cột hình học với các ràng buộc về SRID , kiểu đối tượng và số chiều 

    B1 : Tạo schema nyc_poi 
    B2 : Tạo bảng trống pts 
    B3 : Sử dụng hàm AddGeometryColumn() định nghĩa cột hình học vào bảng mới tạo trước đó 
    -> Giải thích các tham số cần truyền vào hàm AddGeometryColumn('nyc_poi' , 'pts' , 'geom' , 4269 , 'POINT' , 2);
        + nyc_poi : Tên Schema chứa bảng 
        + pts : Tên bảng chứa cột
        + geom : Tên cột khởi tạo 
        + 4269 : Mã hệ tham chiếu không gian -> quyết định cột dữ liệu mang hệ tọa độ nào
        + POINT : Kiểu hình học 
        + 2 : Tham số chiều (Dimension)
        
- Tham số chiều là : Các tham số có thể truyền vào là 2 , 3, 4 , dựa vào các tham số này quyết định đến cột dữ liệu có thể lưu trữ những dữ liệu nào 
    + Tham số = 2 : Không gian 2 chiều (XY) chỉ lưu trữ cặp tọa độ X , Y (kinh độ , vĩ độ) 
    + Tham số = 3 : Không gian 3 chiều (XYZ hoặc XYM) -> Với XYZ lưu trữ thêm dữ liệu Z độ cao -> Với XYM lưu trữ thêm dữ liệu M giá trị đo lường
    + Tham số = 4 : Không gian 4 chiều (XYZM) -> Lưu trữ trọn vẹn 4 thành phần 

2. Khởi tạo các kiểu hình học 2D cơ bản (Point , LineString , Polygon) 

    A. Kiểu điểm - POINT 
    -> Sử dụng Hàm ST_GeomFromText('dữ_liệu_dạng_text' , mã hệ tham chiếu) : Hàm này giúp chuyển các chuỗi văn bản mô tả hình dạng và tọa độ thành đối tượng hình học nhị phân mà PostGIS hiểu được 

        insert into pts(name , geom) 
        value('Empire State Building' , ST_GeomFromText('POINT(-73.985744 40.748549) , 4269) )

    B. Kiểu đường - LINESTRING 
    - Tạo bảng mới và cột chứa dữ liệu dạng LineString 

        create table lines ( gid integer PRIMARY KEY , name VARCHAR(50));
        select ST_AddGeometryColumn('nyc_poi' ,'lines' , 'geom' , 4269 ,'LINESTRING',2);

    - Sử dụng hàm ST_GeomFromText() để nhập dữ liệu dạng đường vào PostGIS 

        insert into lines(name , geom)
        value ('Holland Tunnel' , ST_GeomFromText('LINESTRING(-74.036486 40.730121, -74.03125 40.72882, -74.011123 40.725958)', 4269))

    C. Kiểu đa giác - POLYGON 
    - Tạo bảng mới và cột chứa dữ liệu dạng Polygon 

        create table polys(gid , name);
        select ST_AddGeometryColumn('nyc_poi' , 'polys' , 'geom' , 4269 , 'POLYGON' , 2) ;

    - Sử dụng hàm ST_GeomFromText() nhập dữ liệu dạng vùng vào PostGIS nhưng phải tuân thủ 2 quy tắc nhất định 
        + Điểm đầu và điểm cuối của vùng phải trùng nhau 
        + Hai cặp dấu ngoặc ((...)) : Cặp ngoặc thứ nhất định hình vòng ranh giới bên ngoài ; các cặp ngoặc tiếp theo (nếu có) định hình vòng ranh giới bên trong tạo thành lỗ thủng nếu có 

        INSERT INTO polys (name, geom) VALUES (
            'Central Park', 
            ST_GeomFromText(
                'POLYGON(
                    (-73.973057 40.764356, -73.981898 40.768094, -73.958209 40.800621, -73.949282 40.796853, -73.973057 40.764356), 
                    (-73.966681 40.785221, -73.966058 40.787674, -73.965586 40.788064, -73.957819 40.786569, -73.966681 40.785221)
                )', 
                4269
            )
        );

3. Cú pháp hình học 3D / 4D và đối tượng đa phần 

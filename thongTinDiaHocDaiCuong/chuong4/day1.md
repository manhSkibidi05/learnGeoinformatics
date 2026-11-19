# Ôn tập các chương đã học : 

## Chương 1 : 

- Hệ thống thông tin địa học dựa trên 3 công nghệ chính gồm : GPS/GNSS , Remote Sensing , GIS 

    + GPS/GNSS : Là hệ thống định vị vệ tinh toàn cầu giúp xác định vị trí của 1 đối tượng cụ thể trên trái đất 
    -> Ứng dụng : Hệ thống GPS trên điện thoại di động thu tín hiệu từ vệ tinh , công việc kĩ sư cntt địa học là giải mã tín hiệu làm sạch dữ liệu thu được từ đó tính toán ra được tọa độ của bản thân có thể tính được vận tốc , thời gian , dự đoán hướng di chuyển

    + Remote Sensing : Là hệ thống giúp thu thập thông tin của 1 đối tượng mà không cần tiếp xúc trực tiếp với đối tượng đó 
    -> Ứng dụng : Hệ thống vệ tinh landsat 8/9 thu thập thông tin bằng cảm biến lắp trên vệ tinh sau đó gửi dữ liệu ảnh viễn thám về máy chủ trên trái đất , công việc các kĩ sư cntt địa học là phân tích dữ liệu và đưa ra dự đoán nếu cần thiết

    + GIS : Là hệ thống giúp thu thập , lưu trữ , quản lý , phân tích và trực quan hóa các dữ liệu không gian có thể từ 2 hệ thống trêm hoặc từ các nguồn bản đồ số ...
    -> Ứng dụng : Phần mềm QGIS giúp nhập dữ liệu vector/raster , công việc kĩ sư cntt địa học là trực quan hóa dữ liệu đó sau đó có thể tiến hành phân tích hoặc sử dụng công cụ được cung cấp để giải quyết bài toán thực tế được đưa ra 

- Hệ tọa độ : Là hệ quy chiếu toán học giúp người dùng biết cách biểu diễn vị trí của 1 điểm trên bề mặt trái đất 
    + Hệ tọa độ địa lí : Đối tượng đơn vị độ , dùng để biểu diễn vị trí 1 điểm trên bề mặt trái đất và lưu trữ dữ liệu không gian 
    + Hệ tọa độ phẳng : Đối tượng đơn vị mét , dùng để biểu diễn tính toán hình học như khoảng cách 2 điểm , diện tích bề mặt...

- Mô hình dữ liệu : Là một cách tư duy về cách biểu diễn 1 đối tượng địa lý lên trên máy tính sao cho máy tính có thể đọc và hiểu 
    + Mô hình dữ liệu Vector : Các dữ liệu địa lý sẽ được biểu diễn dưới dạng hình học điểm , đường , vùng kèm thêm bảng thuộc tính -> Các dữ liệu phù hợp với mô hình vector là các dữ liệu có ranh giới rõ ràng (nhà , đường...)
    + Mô hình dữ liệu Raster : Các dữ liệu địa lý sẽ được biểu diễn dưới dạng lưới đều nhau mỗi ô đều chứa dữ liệu -> Các dữ liệu phù hợp với mô hình raster là các dữ liệu biến thiên liên tục (độ cao , nhiệt độ...)
- Định dạng dữ liệu : Là cách lưu trữ liệu một cách có tổ chức dựa trên các mô hình dữ liệu , máy tính dựa vào các định dạng dữ liệu này để đọc hiểu và phân tích 
    + Định dạng dữ liệu vector : Shapefile (.shp , .shx , .dbf , .prj) , geojson (.geojson) , geopackage (.gpkg) ,...
    + Định dạng dữ liệu raster : GeoTIFF , JPEG2000

## Chương 2 : 

- GNSS : Là tên gọi chung của các hệ thống định vị vệ tinh trên toàn thế giới 
- GPS : Là hệ thống định vị vệ tinh toàn cầu được phát triển bởi Mĩ -> 3 phân hệ của GPS : Không gian (vệ tinh) , điều khiển (trạm mặt đất) , người dùng (máy thu)
- Quy trình thu thập dữ liệu định vị GPS : 
    + B1 : Chuẩn bị thiết bị gồm điện thoại có hệ thống GPS hoặc các thiết bị chuyên dụng sau đó đứng ra những vị trí thoáng (tránh tầng hầm / rừng rậm...) giúp dễ dàng bắt tín hiệu vệ tinh
    + B2 : Thu tín hiệu từ ít nhất 4 vệ tính gồm các dữ liệu : tọa độ vệ tinh đó , thời gian phát tín hiệu từ vệ tinh 
    + B3 : Thực hiện tính toán vị trí tọa độ của đối  tượng dựa trên công thức chính : Khoảng cách = c x (thời gian thu - thời gian phát)
    + B4 : Thực hiện mã hóa dữ liệu tính toán được thành chuỗi văn bản theo chuẩn NMEA 0183 giúp dễ dàng chuyển dữ liệu sang các phần mềm khác
    + B5 : Các phần mềm thực hiệu giải mã dữ liệu sau đó tiến hành lọc , phân tích, trực quan hóa và đưa ra dự đoán 

-> Khi thu thập dữ liệu GPS cần để ý đến nguồn sai số gây ra sai vị trí : Tầng điện ly , tầng đối lưu , đa đường , sai đồng hồ / quỹ đạo , hình học vệ tính (chỉ số DOP)

## Chương 3 : 

- Remote Sensing : Là hệ thống giúp thu thập dữ liệu bằng các thiết bị như vệ tinh , flycam ... có tích hợp cảm biến không cần tiếp xúc trực tiếp các đối tượng đó 
- Phân loại viễn thám dựa trên nguồn năng lượng :
    + Bị động : Dùng năng lượng mặt trời (Landsat , sentinel-2)
    + Chủ động : Dùng cảm biến tự phát sóng (SAR , LiDAR)
- Quy trình thu thập dữ liệu viễn thám : 
    + B1 : Xác định đối tượng cần quan sát
    + B2 : Nguồn năng lượng từ sóng điện từ chiếu vào đối tượng có thể từ mặt trời hoặc từ cảm biến phát sóng
    + B3 : Sóng truyền qua khí quyển , tương tác với đối tượng rồi phản xạ / bức xạ lại sóng
    + B4 : Cảm biến thu nhận sóng đó truyền dữ liệu về trạm mặt đất
    + B5 : Tiền xử lý dữ liệu thu được (hiểu chỉnh bức xạ , khí quyển , hình học)
    + B6 : Sử dụng kĩ thuật tổ hợp màu (RGB) để trực quan hóa 
    + B7 : Phân tích , phân loại , tính chỉ số NDVI rồi đưa ra dự đoán 

## Chương 4 : 

- Cơ sở dữ liệu là : Tập hợp dữ liệu có tổ chức , có cấu trúc và lưu trữ trên máy tính phục vụ nhiều người dùng , ứng dụng dùng 

- Hệ quản trị cơ sở dữ liệu là : Các phần mềm giúp quản lý các cơ sở dữ liệu trên máy tính , giúp người dùng dễ dàng thao tác thêm , sửa , xóa , truy vấn , phân quyền , bảo mật dữ liệu được lưu trữ  

- PostgreSQL và PostGIS tại sao lựa chọn để lưu trữ dữ liệu không gian ? 
- PostgreSQL : Là hệ quản trị cơ sở dữ liệu mã nguồn mở , miễn phí , ổn định tuân thủ ACID , hỗ trợ nhiều người dùng và có khả năng mở rộng bằng extension 
- PostGIS : Là extension biến PostgreSQL thành hệ quản trị cơ sở dữ liệu có thể quản lý các cơ sở  dữ liệu không gian
    + Thêm kiểu dữ liệu geometry/geography (điểm , đường , vùng) và raster
    + Có sẵn nhiều hàm không gian : ST_Distance , ST_Area , ST_Buffer , ST_Intersects , ST_Transform...
    + Chỉ mục không gian (GiST) giúp truy vấn nhanh trên dữ liệu lớn 
    + Hỗ trợ SRID / EPSG quản lý và chuyển đổi hệ tọa độ 
    + Tuân thủ chuẩn OGC simple features
    + Tích hợp tốt với QGIS , GeoServer và các phần mềm GIS khác 
-> So sánh khi lưu dữ liệu bằng cơ sở dữ liệu PostgreSQL có tích hợp PostGIS với Shapefile : 
    + file hạn chế chỉ tối đa 2GB 
    + Tên 1 trường dữ liệu tối đa 10 kí tự
    + Khó dùng chung nhiều người
    + Không có truy vẫn SQL mạnh -> lấy dữ liệu dựa trên điều kiện nhất định 

# Học chi tiết Chương 4 :

## Giai đoạn 1 : Khởi tạo CSDL không gian , quản lý Schema và import dữ liệu (shapefile / csv)


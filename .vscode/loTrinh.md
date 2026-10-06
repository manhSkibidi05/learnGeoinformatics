________________Giai đoạn 1: Nền tảng GIS & Hiển thị Bản đồ (Frontend)________________
Thời gian dự kiến: 3 - 4 tuần
Mục tiêu: Hiểu các khái niệm cốt lõi của bản đồ và làm chủ việc hiển thị dữ liệu ở phía Client.
• Kiến thức GIS cơ bản:
	• Tìm hiểu về các loại dữ liệu địa lý: Vector (Point, Line, Polygon) và Raster (Ảnh vệ tinh, Pixel).
	• Hiểu về Hệ tọa độ (CRS): Phân biệt hệ tọa độ toàn cầu WGS84 (EPSG:4326) và hệ tọa độ phẳng Web Mercator (EPSG:3857).
	• Học cấu trúc định dạng dữ liệu GeoJSON (Tiêu chuẩn truyền tải file bản đồ trên Web).
• Tích hợp Bản đồ vào React:
	• Học cách cài đặt và cấu hình Leaflet và React-Leaflet kết hợp TypeScript.
	• Hiển thị bản đồ nền (Tile Layers) từ OpenStreetMap, Stamen, hoặc CartoDB.
	• Thao tác với Marker, Popup, Tooltip và tùy biến Icon bản đồ.
	• Sử dụng thư viện Turf.js để xử lý các phép toán hình học cơ bản ngay trên trình duyệt (tính khoảng cách, diện tích).
• -> Cột mốc 1: Xây dựng một trang Dashboard bằng React + Leaflet hiển thị danh sách các địa điểm du lịch từ một file data.geojson tĩnh, có tính năng lọc theo danh mục và tìm kiếm.


________________Giai đoạn 2: Quản trị Dữ liệu Không gian (Database)________________
Thời gian dự kiến: 3 tuần
Mục tiêu: Biết cách lưu trữ tọa độ và viết câu lệnh SQL để truy vấn không gian thay vì dùng code logic thông thường.
• Cơ sở dữ liệu PostgreSQL:
	• Học cách cài đặt PostgreSQL và kích hoạt extension PostGIS (CREATE EXTENSION postgis;).
	• Tìm hiểu các kiểu dữ liệu không gian trong PostGIS: GEOMETRY và GEOGRAPHY.
• Truy vấn SQL Không gian (Spatial SQL):
	• Học cách chuyển đổi dữ liệu từ văn bản sang tọa độ: ST_GeomFromText('POINT(105.85 21.02)', 4326).
	• Làm chủ các hàm đo đạc: ST_Distance, ST_Area, ST_Length.
	• Làm chủ các hàm quan hệ không gian: ST_Contains (vùng này có chứa điểm kia không), ST_Within, ST_Intersects (hai đường ống có giao nhau không).
	• Tìm hiểu về Spatial Indexing (GIST) để tối ưu hóa tốc độ truy vấn khi bảng dữ liệu lên đến hàng triệu dòng.
• -> Cột mốc 2: Cài đặt phần mềm QGIS (công cụ desktop), kết nối vào cơ sở dữ liệu PostgreSQL của bạn, thử vẽ một vài vùng đa giác (Polygon) trên QGIS rồi viết câu lệnh SQL trong pgAdmin để tìm xem có bao nhiêu điểm (Point) nằm bên trong vùng đó.


________________Giai đoạn 3: Phát triển Web API & Logic Nghiệp vụ (Backend)________________
Thời gian dự kiến: 3 - 4 tuần
Mục tiêu: Đóng vai trò cầu nối, viết API để React có thể tương tác (Thêm, Sửa, Xóa) dữ liệu trong PostGIS.
• Xây dựng API với Python (FastAPI hoặc Django):
	• Học cách kết nối Python với PostgreSQL bằng các thư viện ORM (như SQLAlchemy/GeoAlchemy2 hoặc GeoDjango).
	• Viết các API nhận tọa độ (X, Y) từ React gửi về, lưu vào Database.
	• Viết API truy vấn và trả dữ liệu về dưới dạng chuẩn GeoJSON (sử dụng thư viện Shapely hoặc GeoPandas để xử lý dữ liệu trên Python trước khi trả về).
• Xử lý bài toán thực tế:
	• Viết API Tìm kiếm lân cận (Spatial Query): Người dùng gửi vị trí hiện tại của họ, Python gọi PostGIS tìm các cửa hàng trong bán kính 2km.
• -> Cột mốc 3: Hoàn thiện ứng dụng Fullstack đầu tiên: Người dùng dùng chuột click lên bản đồ React để ghim một điểm (Marker), điền tên địa điểm. Thông tin được gửi qua API Python để lưu vào PostGIS. Trang web hiển thị lại danh sách điểm đó theo thời gian thực.


________________Giai đoạn 4: Xuất bản Bản đồ dung lượng lớn & Nâng cao (Map Server)________________
Thời gian dự kiến: 3 - 4 tuần
Mục tiêu: Tối ưu hiệu năng hệ thống khi đối mặt với dữ liệu bản đồ cực lớn (Hệ thống Enterprise).
• Làm chủ GeoServer:
	• Cài đặt GeoServer (chạy cục bộ hoặc qua Docker).
	• Kết nối GeoServer trực tiếp vào cơ sở dữ liệu PostgreSQL/PostGIS.
	• Tạo Workspace, Store và xuất bản một bảng dữ liệu thành một Layer bản đồ.
	• Học cách định kiểu bản đồ bằng SLD (Styled Layer Descriptor) hoặc CSS của GeoServer (đổi màu đường, tô màu vùng theo điều kiện zoom).
• Tích hợp nâng cao vào Frontend:
	• Gọi lớp bản đồ dạng ảnh WMS (Web Map Service) từ GeoServer vào React-Leaflet để tối ưu tốc độ load.
	• Tìm hiểu về Vector Tiles (MVT) nếu muốn bản đồ mượt mà như Google Maps (Sử dụng GeoServer hoặc công cụ Martin).
• -> Cột mốc 4 (Đồ án tốt nghiệp): Xây dựng một hệ thống Hạ tầng đô thị hoặc Quản lý đất đai. Hệ thống có lớp bản đồ quy hoạch (Polygon) nặng hàng trăm MB được tải qua GeoServer, có phân quyền đăng nhập, cho phép bật/tắt các lớp bản đồ và đo đạc khoảng cách giữa các đối tượng.
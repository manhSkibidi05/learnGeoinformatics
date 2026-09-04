Review day 2 :

    - Dữ liệu là các con số , chữ viết , hình ảnh chưa qua xử lí và không có ý nghĩa nào đối với người dùng
    -> Dữ liệu biểu diễn cho thông tin vì thông tin mang tính trừu tượng không có hình dạng cụ thể và để truyền thông tin đi cần chuyển thông tin đó thành dữ liệu

    - Thông tin là dữ liệu + ngữ cảnh từ các dữ liệu đã qua xử lí , khi đặt vào 1 ngữ cảnh sẽ tạo ra thông tin và có ý nghĩa với đối với người dùng nhận thông tin đó
    -> Tạo thành vòng lặp khi thông tin muốn lưu trữ và truyền đi cần chuyển hóa thành dữ liệu và khi lấy dữ liệu ra và đặt vào ngữ cảnh tạo ra thông tin mới

    - Dữ liệu không gian địa lý : là các dữ liệu bao gồm dữ liệu không gian và dữ liệu thuộc tính của 1 đối tượng địa lý
        + Dữ liệu không gian : Trả lời cho câu hỏi ở đâu ? -> dữ liệu này chứa tọa độ , hình dạng , vị trí địa lý của đối tượng địa lý
        + Dữ liệu thuộc tính : Trả lời cho câu hỏi như thế nào ? -> dữ liệu này chứa các thông tin phi vật lý đặc điểm của đối tượng

    - Quy trình lưu trữ đối tượng địa lý vào GIS :
        + B1 : Mô tả đối tượng địa lý
        -> Thu thập dữ liệu không gian và dữ liệu thuộc tính của đối tượng địa lý này

        + B2 : Mô hình hóa đối tượng địa lý
        -> Xác định loại mô hình dựa vào các yếu tố sau :
            - Đối tượng liên tục hay rời rạc -> liên tục : Mô hình raster , rời rạc : Mô hình vector
            - Tỷ lệ bản đồ so với đối tượng địa lý -> Cùng 1 đối tượng khi tỉ lệ bản đồ càng nhỏ thì đối tượng đơn giản hóa dạng điểm hoặc đường , khi tỷ lệ càng lớn nó được thể hiện chi tiết dưới dạng vùng
            - Dựa vào yêu cầu đối tượng đối với bài toán -> tìm đường ngắn nhất : Mô hình vector dạng đường
        -> Sau khi xác định loại mô hình chuyển hóa các dữ liệu từ bước 1 thành dữ liệu cho máy tính có thể đọc được

        + B3 : Thiết lập mối quan hệ không gian (Topology) -> Tạo quy tắc để máy tính hiểu mối liên hệ giữa các đối tượng

    - Mô hình Vector : Biểu diễn các đối tượng địa lý theo dạng hình học các đối tượng dùng cho mô hình này là các đối tượng rời rạc và có ranh giới rõ ràng , đối tượng được xác định nhờ đỉnh là tọa độ (X , Y)
    -> 3 loại hình vector :
        + Dạng điểm (Point) : Chỉ 1 đỉnh duy nhất dùng cho đối tượng duy nhất
        + Dạng đường (Line) : Từ 2 đỉnh trở lên nối với nhau tạo thành đường không khép kín (điểm đầu luôn khác điểm cuối) dùng cho đối tượng có chiều dài nhưng không có chiều rộng
        + Dạng vùng (Polygon) : Từ 4 đỉnh trở lên nối với nhau tạo thành vùng khép kín (điểm đầu luôn trùng điểm cuối) dùng cho đối tượng lớn cần nối với nhau tạo thành hình

Câu hỏi ôn tập giai đoạn 2

    Câu 1 : Giải thích khái niệm Spatial Resolution (độ phân giải không gian) của dữ liệu Raster . Khi độ phân giải tăng gấp 2 lần kích thước tệp dữ liệu thay đổi như thế nào ?
    - Độ phân giải không gian của dữ liệu Raster : Được xác định bằng kích thước thực địa của 1 ô lưới (cell/pixel) . vd : ảnh có độ phân giải 10m -> mỗi ô vuông trên ảnh đại diện cho một khu vực có diện tích 10m x 10m trên mặt đất thực tế
    - Khi độ phân giải tăng gấp 2 lần thì kích thước tệp dữ liệu tăng gấp 4 lần
    -> Giải thích :
        + Bản chất dữ liệu Raster là một ma trận 2 chiều (X , Y) . Khi độ phân giải tăng gấp 2 -> kích thước ô lưới giảm đi một nửa theo cả 2 chiều . vd : 20m -> 10m
            - số lượng ô lưới theo chiều ngang tăng gấp 2
            - số lượng ô lưới theo chiều dọc tăng gấp 2
            - tổng số ô lưới của toàn bộ bức ảnh tăng lên 4

    -> Quy luật biến thiên trong dữ liệu Raster :
        + Kích thước ô lưới càng lớn -> số lượng ô lưới ít -> độ phân giải càng thấp
        + Kích thước ô lưới càng nhỏ -> số lượng ô lưới nhiều -> độ phân giải càng cao

    Câu 2 : So sánh ưu và nhược điểm của chuẩn GeoJSON và ESRI Shapefile khi chúng ta xây dựng và phát triển một ứng dụng bản đồ trên nền web (web service)
    - GeoJSON :
        + Lưu trữ đối tượng địa lý trong 1 file duy nhất
        + Cho phép lưu vector mang loại hình khác nhau trong cùng 1 file
        + Không giới hạn kích thước file
        + Các thông tin phi vật lý của đối tượng được lưu trong 1 mảng thuộc tính của đối tượng đó có thể truy cập nhanh chóng và rõ ràng
    - ESRI Shapefile :
        + Phải chia làm 3 file nhỏ khác gây bất tiện
        + Chỉ cho phép vector mang 1 loại hình trong 1 file
        + Giới hạn kích thước file 2GB

    -> Bổ sung ưu nhược điểm góc nhìn Web GIS :
        + GeoJSON
        - ưu điểm : ĐỊnh đạng văn bản mở dựa trên JSON -> trình duyệt đọc và phân tích trực tiếp bằng js qua hàm JSON.parse()
        - nhược điểm : GeoJSON tệ khi xử lí dữ liệu lớn , do định dạng file text > 50MB tốc độ tải qua mạng rất chậm gây nghẽn bộ nhớ
        + ESRI Shapefile :
        - nhược điểm : trình duyệt web không đọc trực tiếp từ file

    Câu 3 : Phân biệt sự khác nhau giữa Point và MultiPoint , Polygon và MultiPolygon . Cho ví dụ
    - Point : Với 1 đối tượng đơn lẻ có 1 đỉnh tọa độ [X , Y] duy nhất . vd : 1 cây xăng , 1 bến xe bus
    - MultiPoint : Với 1 đối tượng mang nhiều tọa độ khác nhau nhưng vẫn chung 1 thuộc tính của đối tượng đó . vd : vị trí toàn bộ cột mốc chủ quyền biên giới
    - Polygon : Với 1 đối tượng là 1 vùng khép kín đơn lẻ các đỉnh tạo thành 1 hình duy nhất . vd : hồ hoàn kiếm
    - MultiPolygon : Với 1 đối tượng nhiều vùng khép kín rời rạc địa lý nhưng là một thực thể . vd : đất nước việt nam bao gồm phần đất liền và các đảo

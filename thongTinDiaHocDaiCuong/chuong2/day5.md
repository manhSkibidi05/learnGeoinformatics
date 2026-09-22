Review day4 : 

- Quy trình các bước thu thập dữ liệu vị trí bằng hệ thống GPS  (từ tín hiệu vệ tinh thành tọa độ biểu diễn trên các phần mềm GIS )

    + GIAI ĐOẠN 1 : Chuẩn bị thiết bị thu tín hiệu từ vệ tinh của GPS 
        -  Sử dụng các thiết bị thu / smartphone có tích hợp chip GPS bắt đầu thu tín hiệu 

    + GIAI ĐOẠN 2 : Vệ tinh trả về tín hiệu và tính toán ra tọa độ địa lý  
        - Các bước để tính toán ra tọa độ vị trí khi vệ tinh phát ra tín hiệu gồm T phát và tọa độ vệ tinh (X , Y , Z) tại thời điểm phát : 
            B1 : Máy thu phải thu tín hiệu từ ít nhất 4 vệ tinh 
            B2 : Sử dụng công thức tính khoảng cách từ tọa độ đối tượng đến tọa độ vệ tinh : Khoảng cách = vận tốc ánh sáng X (T thu - T phát)
            B3 : Từ công thức tổng quát trên lập phương trình 4 ẩn (x , y  , z ) và độ lệch thời gian đen ta T 
            B4 : Chuyển từ tọa độ (x , y , z) hệ tọa độ vuông góc với không gian 3D sang hệ tọa độ địa lý WGS-84 và thu được tọa độ địa lý (lon , lat , high)

    + GIAI ĐOẠN 3 : Mã hóa dữ liệu thành dữ liệu chuẩn NMEA 0183
        - Chip xử lý GPS trên phần cứng giúp đóng gói tọa độ đã được tính toán trước đó dưới dạng text theo chuẩn NMEA 0183 (như $GPGGA) , NMEA 0183 đóng vai trò như ngôn ngữ trung gian giúp chuyển dữ liệu đi 

    + GIAI ĐOẠN 4 : Truyền dữ liệu từ chip GPS đến phần mềm / máy tính 
        - Dữ liệu theo chuẩn NMEA 0183 được truyền đến phầm mềm / máy tính thông qua các hình thức :
            + Cổng kết nối vật lý : USB , COM
            + Cổng kết nối phi vật lý : bluetooth / wi-fi -> phổ biến ở các máy thu RTK hiện đại
            + Luồng dữ liệu nội bộ (internal bus / api) nếu là ứng dụng chạy ngay trên smartphone 

    + GIAI ĐOẠN 5 : Giải mã dữ liệu và trực quan hóa dữ liệu 
        - Giải mã : Phần mềm đọc chuỗi NMEA , tách các trường vị độ / kinh độ đang đơn vị độ phút chuyển sang độ thập phân 
        - Chuyển hệ tọa độ : Chuyển từ hệ tọa độ WGS-84 (độ) sang hệ tọa độ VN-2000 (mét) bằng phép chiếu UTM để tính toán khoảng cách / diện tích chính xác
        - Trực quan hóa và lưu trữ : Vẽ điểm (Point) lên bản đồ theo thời gian thực và đóng gói vào cơ sở dữ liệu GIS 

- Chuẩn NMEA là : Dạng text được chuẩn hóa sử dụng làm ngôn ngữ trung gian giúp truyền dữ liệu từ phần cứng (chip GPS ) sang phần mềm / máy tính 
-> Một số các câu lệnh NMEA 0183 phổ biến : 
    + $GPGGA : là Mã câu lệnh theo chuẩn NMEA , câu lệnh này chứa các dữ liệu như kinh độ , vĩ độ , độ cao , thời gian , trạng thái định vị và chỉ số HDOP 
    + $GPGLL : Chứa thông tin rút gọn về vị trí địa lý (kinh độ / vĩ độ) và thời gian
    + $GPVTG : Cung cấp thông tin về vận tốc di chuyển và hướng di chuyển 

- Giải mã kinh độ và vĩ độ đơn vị độ phút sang độ thập phân 
    + Vĩ độ : Định dạng là DDMM.MMMM sử dụng công thức sau : độ thập phân = DD + MM.MMMM / 60
    + Kinh độ : Định dạng là DDDMM.MMMM sử dụng công thức sau : độ thập phân = DDD + MM.MMMM / 60 

- Khoảng cách 2 điểm với 2 hệ tọa độ khác nhau : 
    + Với hệ tọa độ địa lý : Tính khoảng cách giữa 2 điểm gọi là khoảng cách đường chim bay -> Sử dụng công thức haversine
    + Với hệ tọa độ phẳng : Tính khoảng cách giữa 2 điểm gọi là khoảng cách đường chim bay -> Sử dụng công thức pi-ta-go
-> với hệ tọa độ địa lý sẽ trả về đường cong ngắn nhất trên bền mặt quả cầu và sẽ không chuẩn xác bằng hệ tọa độ phẳng khi tính khoảng cách giữa 2 điểm 

2. Cấu trúc JSON Location Object (Dành cho lập trình web / mobile)

    - Khi lập trình webGIS hoặc ứng dụng di động , hệ điều hành và trình duyệt tự động xử lý (parse) các câu lệnh NMEA thô từ chip GPS và cung cấp cho lập trình viên một đối tượng JSON rất gọn gàng 

    {
        "coords" : {
            "latitude" : 21.0221,  -> vĩ độ (độ thập phân)
            "longitude" : 105.2222, -> kinh độ (độ thập phân)
            "altitude" : 15.2,  -> độ cao (mét)
            "accuracy" : 4.5 ,  -> độ chính xác : bán kính sai số dựa trên chất lượng tín hiệu , loại bỏ các  tín hiệu nếu độ sai số này > 30 (mét)
            "heading" : 90, -> hướng di chuyển (0 - 350 độ)
            "speed" : 12.5 -> vận tốc di chuển (m / s)
        }
        "timestamp" : 1693821035000 -> nhãn thời gian 
    }

3. Các định dạng lưu trữ và trao đổi tệp tin GPS 
    - Ngoài NMEA và JSON ra dữ liệu định vị lưu trữ ra tệp tin thường tồn tại các định dạng : 
        + GPX
        + KML / KMZ
        + GeoJSON : Dựa trên JSON mô tả đối tượng hình học (Point , LineString , Polygon) kèm thuộc tính , rất phổ biến trên môi trường WebGIS -> chuẩn GeoJSON bắt buộc lưu tọa độ theo thứ tự [Kinh độ , Vĩ độ]
        + CSV / TXT
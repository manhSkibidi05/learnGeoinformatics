Chương 2 - Giai đoạn 3 : Chuẩn hóa và định dạng dữ liệu vị trí 

-> Quy trình thực tế khi thu thập vị trí tọa độ bằng hệ thống GPS 

    - GIAI ĐOẠN 1 : Thu tín hiệu vô tuyến
        + Sử dụng các máy thu tín hiệu GPS chuyên dụng / smartphone tích hợp hệ thống GPS/GNSS để thu tín hiệu vệ tinh từ GPS 

    - GIAI ĐOẠN 2 : Giải mã và tính toán khoảng cách
        + Thu thập tín hiệu từ ít nhất 4 vệ tinh để tính khoảng cách đến 4 vệ tinh đó bằng công thức : Khoảng cách = vận tốc as X (T nhận - T phát)
        -> T nhận là thời gian máy thu nhận tín hiệu , T phát là thời gian phát ra tín hiệu đó trên vệ tinh 

        + Từ công thức trên lập ra phương trình 4 ẩn để tính ra tọa độ không gian của 1 điểm gồm x , y , z và độ lệch thời gian đenta t
        -> Công thức chuẩn 1 phương trình trong hệ phương trình 4 ẩn :
            d1 = c X [(t1 + đenta t1) - T phát1] 
            <=> căn bậc 2 của (x - x1) mũ 2 + (y - y1) mũ 2 + (z - z1) mũ 2 = c X [(t1 + đenta t1) - T phát1]
            <=> (x - x1) mũ 2 + (y - y1) mũ 2 + (z - z1) mũ 2 = c mũ 2 X [(t1 + đenta t1) - T phát1] mũ 2 

        -> Vì khoảng cách (d) trong không gian 3 chiều từ vị trí máy thu (x , y , z) đến vệ tinh thứ 1 với vị trí đã biết (x1 , y1 , z1) được tính bằng công thức :
            d1 = căn bậc 2 của (x - x1) mũ 2 + (y - y1) mũ 2 + (z - z1) mũ 2

    - GIAI ĐOẠN 3 : Xuất dữ liệu thô dạng chuỗi NMEA 0183
        + Ngay sau khi tính xong tọa độ chip GPS mã hóa toàn bộ thông tin thành các dòng chữ chuẩn hóa theo định dạng NMEA 0183 và bắn qua cổng giao tiếp (UART / bluetooth / USB)

    - GIAI ĐOẠN 4 : Hiệu chỉnh và chuyển đổi hệ tọa độ 
        + Phần mềm quản lý (như QGIS , ArcGIS hoặc app GIS qua điện thoại) nhận chuỗi NMEA , áp dụng các bộ lọc làm mịn (như Kalman) và chuyển đổi hệ tọa độ quy chiếu WGS-84 (độ) sang hệ tọa độ phẳng quốc gia như VN-2000 (mét)

    - GIAI ĐOẠN 5 : Lưu trữ và biểu diễn 
        + Tọa độ đã được chuẩn hóa tự động ghi vào cột geometry trong bảng thuộc tính (GeoPackage , GeoJSON hoặc PostGIS) để vẽ điểm / đường / vùng lên bản đồ 

1. Chuẩn NMEA 0183 là gì ? 
    - NMEA 0183 (viết tắt của National Marine Electronics Association) là một chuẩn giao tiếp dữ liệu chuẩn hóa do hiệp hội thiết bị điện tử hàng hải quốc gia Mỹ phát triển 
        + Bản chất : Đây là chuỗi ký tự dạng văn bản thuần thúy (ASCII text) định dạng cho phép chip GPS phần cứng trò truyện với các phần mềm / máy tính 
        + Đặc điểm : Dữ liệu truyền dưới dạng văn bản thuần , được chia thành từng câu lệnh (Sentence / NMEA Message) bắt đầu bằng dấu $ và phân tách các trường thuộc tính bằng dấu phảy (,)

    - Tất cả các câu lệnh của chuẩn NMEA 0183 đều bắt đầu bằng $ theo sau là 2 ký tự định danh nguồn phát (GP cho GPS , GN cho GNSS) và 3 ký tự mã loại câu lệnh : 3 loại câu lệnh NMEA 0183 cốt lõi nhất cần nắm vững 

        + $GPGGA (global positioning system fix data) 
        -> Đây là câu lệnh quan trọng nhất , chứa đầy đủ thông tin về tọa độ 3D , độ cao , thời gian chuẩn và chất lượng định vị 

        vd : Chuỗi NMEA thô : $GPGGA,123519,4807.038,N,01131.000,E,1,08,0.9,545.4,M,46.9,M,,*47
        -> thứ tự thuộc tính cách nhau bằng dấu phảy : 
            + thự tự 0 : $GPGGA ->  mã câu lệnh
            + 1 : 123519 -> thời gian UTC 12h35m19s
            + 2 , 3 : 4807.036,N -> vĩ độ 
            + 4 , 5 : 01131.000,E -> kinh độ 
            + 6 : 1 -> trạng thấi định vị (0 = chưa bắt dc , 1 = GPS thường , 2 = DGPS/RTK Float , 4 = RTK fix)
            + 7 : 08 -> số lượng vệ tinh 
            + 8 : 0.9 -> chỉ số HDOP : chỉ số đo độ lệch hình học mặt phẳng càng nhỏ càng chuẩn 
            + 9 , 10 : 545.5,M -> độ cao so mực nước biển
            + 10 , 11 : 46.9,M -> độ cao ellipsoid tương ứng độ lệch mặt chuẩn Geoid so với ellipsoid
            + 13 : *47 -> check sum mã kiểm tra tính toàn ven của chuối dữ liệu 

        + $GPRMC (recommended minimum specific GPS data) 
        -> Đây là câu lệnh rút gọn tối thiểu nhất cho các thiết bị giám sát hành trình (hộp đen ô tô ,tracking) chứa thêm thông tin ngày tháng , vận tốc và hướng di chuyển 

        vd: chuỗi NMEA thô : $GPRMC,123519,A,4807.038,N,01131.000,E,022.4,084.4,230326,,,A*6A

        + $GPGSA (GPS DOP and Active satellites)
        -> Đây là câu lệnh cung cấp thông tin về độ chính xác hình học (DOP) và danh sách ID của các vệ tinh đang được máy thu sử dụng để tính toán 
        
        vd : chuỗi NMEA thô : $GPGSA,A,3,04,05,09,12,14,24,,,,,,,2.5,1.3,2.1*39

    - Thuật toán giải mã tọa độ NMEA : Cảm biến GPS phát tọa độ ở dạng phút thập phân , để đưa vào hệ thống phần mềm hoặc vẽ lên bản đồ cần dùng thuật toán chuyển đổi sang độ thập phân 
        + Vĩ độ : Định dạng chuỗi DDMM.MMMM -> với DD là số độ MM.MMMM là số phút 
            Độ thập phân = DD + (MM.MMMM / 60)

        + Kinh độ : Định dạng chuỗi DDDMM.MMMM -> với DDD là số độ MM.MMMM là số phút 
            Độ thập phân = DDD + (MM.MMMM / 60)
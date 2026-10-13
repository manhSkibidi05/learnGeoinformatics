# Review : 

## Giai đoạn 3 : 

5. Câu hỏi ôn tập cuối bài 

- Câu 1 : Viết công thức tổng quát tính chỉ số NDVI và công thức cụ thể khi áp dụng cho dải kênh của vệ tinh Landsat 8/9
-> Công thức tổng quát tính chỉ số NDVI : 

    Chỉ số NDVI =  NIR - RED / NIR + RED

-> Công thức khi áp dụng cho vệ tinh Landsat 8/9 : 

    Chỉ số NDVI = Kênh 5 - Kênh 4 / Kênh 5 + Kênh 4

- Câu 2 : Giải thích cơ sở vật lý tại sao chỉ số NDVI của thảm thực vật xanh tươi khỏe lại đạt giá trị cao (tiến đến gần +1.0) , trong khi đối tượng mặt nước sạch lại có giá trị NDVI âm ? 
    + Kênh 5 : tia hồng ngoại gần (NIR) thực vật phản xạ rất mạnh nên giá trị cảm biến thu được sẽ lớn , ngược lại nước hấp thụ rất mạnh đối với tia hồng ngoại gần (NIR)
    + Kênh 4 : màu đỏ thực vật và nước đều hấp thụ rất mạnh nên giá trị cảm biến thu được sẽ nhỏ 
-> Khi áp dụng chuẩn công thức trên để tính chỉ số NDVI thì giá trị thu được với thực vận sẽ xấp xỉ 1.0 còn với nước giá trị có thể âm hoặc xấp xỉ 0

- Câu 3 : Nêu 3 ứng dụng thực tế của chỉ số NDVI trong nghiên cứu địa lý và quản lý môi trường . Trong bài thực hành chương 3 việc so sánh ảnh NDVI giữa mùa đông và mùa hè giúp chúng ta kết luận gì về thảm thực vật ? 
-> 3 ứng dụng thực tế của chỉ số NDVI trong nghiên cứu : 
    + Đánh giá sức khỏe cây trồng : Giúp nhận biết sớm tình trạng sinh trưởng , phát hiện cây thiếu nước , sâu bệnh hay stress quang phổ trước khi mắt thường có thể thấy 
    + Ước tính năng suất và sản lượng : Dựa vào độ xanh và mật độ tán lá để dự báo năng suất lúa , cây lương thực và cây công nghiệp 
    + Theo dõi mức độ che phủ rừng 
-> Việc so sánh ảnh NDVI của thảm thực vật mùa đông và mùa hè giúp chúng ta : 
    + Thực vật mùa hè phát triển mạnh hơn mùa đông do mùa hè nhiều ánh sáng do mặt trời chiếu xuống thực vật phát triển mạnh chỉ số NDVI đạt giá trị rất cao , mùa động cây rụng hoặc suy giảm quang hợp do thời tiết lạnh và thiếu ánh sáng nên chỉ số NDVI giảm rõ rệt 

# Tổng ôn tập chương 2 : 

1. Nguyên lý GNSS (GPS , GLONASS , Galileo , BeiDou) và các nguồn sai số 
    - GNSS là tên gọi chung cho tất cả các hệ thống định vị vệ tinh trên toàn thế giới trong đó bao gồm các hệ thống như : GPS , GLONASS , Galileo , BeiDou
    - GPS là hệ thống định vị vệ tinh toàn cầu giúp xác định vị trí của bất kì đối tượng nào ở mọi thời điểm trên thế giới những nơi dễ dàng thu thập tín hiệu từ vệ tinh trừ những nơi che khuất tín hiều truyền về vệ tinh (tầng hầm , hẻm đô thị...)
    -> Nguyên lý giúp thu thập thông tin vị trí của đối tượng là : 
        Bước 1 : Chuẩn bị thiết bị thu tín hiệu các thiết bị chuyên dụng / smartphone tích hợp chip GPS
        Bước 2 : Thu tín hiệu từ ít nhất 4 vệ tinh sau đó thu được thông tin gồm thời gian truyền tín hiệu và tọa độ vệ tinh (x , y , z)  ->Dựa vào công thức tính khoảng cách giữa vệ tinh và đối tượng: d (khoảng cách) = c (vận tốc ánh sáng) X (T thu - T phát)   . Lập hệ phương trình 4 ẩn tính ra được tọa độ đối tượng và độ sai số về thời gian (do thiết bị đo thời gian máy thu không bằng thiết bị đo thời gian vệ tinh là đồng hồ nguyên tử)
        Bước 3 : Thu thập được tọa độ đối tượng ở thiết bị thu bây cần đưa về phần mềm GIS lúc này thông tin thu được ở định dạng NMEA 0183 giúp giao tiếp giữa phần cứng và phần mềm -> Mã hóa tọa độ thu được dạng text theo chuẩn NMEA 0183
        Bước 4 : Giải mã tọa độ đó sau đó trực quan hóa dữ liệu 

    - Các nguồn sai số : 
        1. Sai số từ vệ tinh 
            + Sai số đồng hồ vệ tinh : Đồng hồ nguyên tử sai số nhỏ
            + Sai số quỹ đạo vệ tinh : Vị trí vệ tinh báo về lệch nhỏ
        2. Sai từ môi trường 
            + Sai số tầng điện ly : Tín hiệu chậm khi đi qua tầng điện ly
            + Sai số tầng đối lưu : Tín hiệu chậm do hơi nước và không khí 
            + Mutipath (phản xạ tín hiệu) : Tín hiệu phản xạ do va đập vào nhà cao tầng , mặt nước 
        3. Sai số máy thu 
            + Sai số đồng hồ máy thu : ĐỒng hồ thạch anh kém chính xác so với đồng hồ nguyên tử
            + Nhiễu tín hiệu : Sai số do thiết bị điện tử
            + GDOP : Hình học của các vệ tinh so với máy thu phân bố tập trung 1 hướng -> sai số tăng
    
2. Đinh dạng dữ liệu định vị (NMEA 0183 sentences , JSON location object) 
    - NMEA là dữ liệu dạng text được quy định sẵn đễ lưu trữ dữ liệu định vị thu thập được giúp giao tiếp phần cứng thiết bị thu với phầm mềm GIS     
    - Câu lệnh của NMEA : $GPGGA -> Bắt đầu với dấu $ sau đó mã hệ thống định vị GP : GPS , GL : Galileo , GN : toàn cầu . Mỗi câu lệnh chứa thông tin nhất định thu thập được và phục vụ mục địch cụ thể , với $GPGGA chứa 14 trường thông tin cách nhau dấu phảy 
    -> Mỗi câu lệnh tương ứng 1 thông tin về đối tượng thu được 
    - JSON location object : là định dạng JSON chứa các trường dữ liệu sau khi giải mã được từ chuỗi NMEA -> định dạng hiện đại thường sử dụng trong web api / ứng dụng di động 


3. Lập trình thu thập dữ liệu vị trí trên thiết bị di động / web API 
    - Khi thu thập được dữ liệu định vị thông qua thiết bị chuyên dụng hoặc thiết bị di động những công việc  kỹ sư cntt địa học cần làm là : Hiện thị dữ liệu lên bản đồ 
    - Có 2 phương pháp sử dụng khi thu thập dữ liệu định vị : 
        1. Thu thập 1 lần duy nhất :
            + Dữ liệu tạo ra : 1 Điểm 
            + Tần suất : 1 lần duy nhất 
            + Tiêu thụ pin : Thấp
            + Ứng dụng : Xác định vị trí , tìm đường đi , check-in 
        
        2. Thu thâp dữ liệu liên tục :
            + Dữ liệu tạo ra : Chuỗi điểm 
            + Tần suất : 1-5s 
            + Tiêu thụ pin : Cao
            + Ứng dụng : Đị bộ , giao hàng , ghi lại hành trình 


4. Xử lý chuỗi dữ liệu GPS (Trajectory Data , Map matching , lọc nhiễu tọa độ) 
    
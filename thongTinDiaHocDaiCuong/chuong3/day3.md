# Review : 

## Chương 3 : Remote Sensing 

- Remote Sensing (viễn thám) : Là kỹ thuật thu nhận thông tin từ đối tượng tự nhiên hoặc hiện tượng trên trái đất / hành tinh mà không trực tiếp tiếp xúc với nó
-> Nguyên lý của RS mà không cần trực tiếp tiếp xúc với đối tượng mà vẫn có thể thu được thông tin là : Thu nhận thông tin thông qua cảm biến được đặt trên vật mang (vệ tinh , drone)
    - Cảm biến bị động : Thu nhận sóng phản xạ lại các đối tượng nhận sóng điện từ của mặt trời hấp thụ 1 phần rồi phản xạ lại , nhiệt lượng tỏa ra từ đối tượng
    - Cảm biến chủ động : Chiếu sóng tới các đối tượng sau đó thu lại sóng phản xạ
-> Khi thu nhận dữ liệu xong viễn thám sẽ trả về ảnh từ ảnh này ta sẽ tiến hành phân tích , ảnh thu được sẽ có độ phân giải của ảnh đó và 1 ảnh viễn thám sẽ được đo chất lượng và mục đích sử dụng tùy vào 4 độ phân giải của ảnh viễn thám
    1. Độ phân giải không gian 
        - Quyết định đến kích thước 1 pixel (điểm ảnh) tương ứng với 1 vị trí trên bề mặt trái đất sẽ có diện tích bn khi thể hiện trên ảnh 
        -> Độ phân giải không gian càng cao thì càng nhìn rõ càng đối tượng trong ảnh 

    2. Độ phân giải quang phổ 
        - Quyết định đến số màu sắc có thể có trong 1 pixel 
        -> Độ phân giải quang phổ càng cao thì số màu sắc càng nhiều nó sẽ giúp máy tính dễ dàng nhận dạng đối tượng trong ảnh 

    3. Độ phân giải bức xạ
        - Quyết định mức độ sáng - tối cùa màu sắc có trong 1 pixel
        -> Độ phân giải bức xạ càng cao thì  mức độ sáng - tối của màu sắc sẽ rõ nét giúp máy tính nhận dạng đối tượng trong ảnh kể cả trong các vùng cực sáng hoặc cực tối 

    4. Độ phân giải thời gian 
        - Quyết định chu kì gửi lại ảnh cùng 1 vị trí 
        -> Độ phân giải thời gian càng cao thì thời gian phải đợi để nhận lại ảnh cùng 1 vị trí sẽ nhanh hơn từ đó đưa ra quyết định cách nhanh và chính xác hơn
-> Trong thực tế 1 ảnh raster sẽ không thể đáp ứng đủ 4 độ phân giải đều ở mức tối đa mà sẽ phải đánh đổi để phù hợp với mục đích sử dụng của ảnh 

# Chương 3 : Remote sensing 

## Giai đoạn 2 : Cấu trúc dải phổ và kỹ thuật tổ hợp màu 

2. Cấu trúc dải phổ 
- Cấu trúc dải phổ là những kênh phổ được lựa chọn với mục đích cụ thể 
-> Viễn thám cắt dải sóng ra thành từng khúc cụ thể và mỗi khúc sẽ được thiết kế để nhìn đặc tính riêng biệt của bề mặt trái đất 

- Một ảnh viễn thám không thu nhận toàn bộ dải sóng có trong tự nhiên mà tùy vào mục đích sử dụng ảnh viễn thám đó mà chọn ra những dải sóng (kênh phổ) mang lại nhiều giá trị và thông tin nhất 
-> lý do không thu nhận toàn bộ dải sóng là : 
    1. Bức tường khí quyển trái đất : Nó sẽ hấp thụ hoàn toàn và chặn nhiều dải sóng (tia X , UV và phần lớn dải hồng ngoại xa)
    2. Tiết kiệm tài nguyên : Khối lượng khổng lồ và không thể truyền tải về trái đất và máy tính không xử lý được

- Ảnh viễn thám phổ thông : Vệ tinh sentinel-2 chọn ra 13 kênh phổ , landsat 9 chọn ra đúng 11 kênh phổ tốt nhất cho việc giám sát tài nguyên , nông nghiệp và môi trường 
-> Khi thu 1 ảnh viễn thám tùy vào số lượng kênh phổ quy định 11 -> 13 thì ảnh viễn thám trả về đủ số lượng kênh phổ đó nhưng tùy vào đối tượng mà ảnh ở dải sóng sẽ khác nhau (trăng sáng / đen kịt)

3. Kỹ thuật tổ hợp dải màu 
- Kỹ thuật tổ hợp dải màu : Cách chúng ta chọn 3 kênh phổ bất kỳ từ bộ ảnh viễn thám đen trắng xếp trồng lên 3 kênh màu cơ bản của màn hình máy tính gồm : 
R (red) - đỏ , G (green) - xanh lá , B (blue) - xanh dương
-> Do màn hình máy tính chỉ hiểu 3 kênh màu RGB này nên bằng cách gán cách kênh phổ từ ảnh viễn thám vào 3 vị trí R-G-B chúng tạo ra bức ảnh màu hoàn chỉnh 
-> Tùy vài việc gán kênh phổ nào vào vị trí nào chúng ta sẽ có kiểu tổ hợp màu khác nhau 

- Lấy hệ thống kênh phổ của vệ tinh landsat 8/9 làm chuẩn : 
    + Kênh 2 : Blue
    + Kênh 3 : Green
    + Kênh 4 : Red
    + Kênh 5 : NIR (cận hồng ngoại)
    + Kênh 6 : SWIR 1 (hồng ngoại sóng ngắn 1)
-> 3 kỹ thuật tổ hợp màu kinh điển mà kỹ sư viễn thám cần thuộc lòng : 
    1. Tổ hợp màu tự nhiên 
        - Công thức gán : R-G-B tương ứng kênh 4 - kênh 3 - kênh 2 
        - Nguyên lý : Gán kênh có màu giống với màu RGB 
        - Kết quả : Bức ảnh tạo ra được giống như nhìn từ máy bay xuống -> cây màu xanh lá, biển xanh dương , đô thị xám...
        - Ứng dụng : Dùng để quan sát trực quan , làm bản đồ địa hình hoặc cho người không chuyên dễ dàng hình dung . -> nhược điểm : dải màu dễ bị mờ bởi sương mù và bụi khí quyển

    2. Tổ hợp màu giả hồng ngoại 
        - Công thức gán : R-G-B tương ứng kênh 5 - kênh 4 - kênh 3
        - Nguyên lý : Đưa kênh NIR cận hồng ngoại là kênh 5 kênh mà cây xanh phản xạ mạnh nhất gán với ô màu đỏ (R) của màn hình , kênh 4 (red) gán ô màu xanh lá (G) , kênh 3 (green) gán ô màu xanh dương (B)
        - Kết quả : 
            + Toàn bộ cây xanh , rừng , lúa hiện lên đỏ rực rỡ -> cây càng khỏe màu đỏ đậm và tươi còn cây yếu màu đỏ xỉn hoặc chuyển sang màu nâu xám 
            + Nước hấp thụ hồng ngoại hoàn toàn nên hiện lên màu xanh đen / đen kịt
            + Đô thị / bê tông màu xanh xám / xanh lơ
        - ứng dụng : Đây tổ hợp màu mạnh nhất cho việc giám sát nông - lâm nghiệp -> giúp phát hiện cháy rừng , phân biệt loại cây , đánh giá mức phủ của rừng 

    3. Tổ hợp màu phân tích nông nghiệp và độ ẩm 
        - Công thức gán : R-G-B tương ứng kênh 6 - kênh 5 - kênh 3
        - Nguyên lý : Đưa kênh SWIR hồng ngoại sóng ngắn kênh 6 phản xạ mạnh nhất với nước / độ ẩm gán với ô màu đỏ (R) , kênh NIR cận hồng ngoại kênh 5 phản xạ mạnh với cây gán với ô màu xanh lá (G) , kênh cuối tùy chọn 3/2 gán cho màu xanh dương (B)
        - Kết quả : 
            + Cây trồng khỏe mạnh hiện thị màu xanh lá cây sáng đậm
            + Đất khô , đất chưa trồng trọt hiện lên màu hồng / nâu 
            + Nước hiện lên xanh đen đậm 
        - Ứng dụng : CHuyên dùng theo dõi chu kỳ phát triển cây trồng (biết ruộng nào vừa gieo / sắp thu hoạch) , giám sát hạn hán hoặc diện tích ngập lụt 

4. Câu hỏi ôn tập 

- Câu 1 : Phân biệt 4 loại độ phân giản viễn thám . Khi độ phân giải không gian tăng từ 30m -> 15m thì kích thước 1 pixel ngoài thực địa thay đổi ra sao ? 
- Câu 2 : Kể tên các dải phổ chính của cảm biến OLI trên Landsat 8/9 (từ band 2 -> band 5) . Dải nào có độ phân giải không gian cao nhất 
- Câu 3 : Kỹ thuật tổ hợp màu là gì ? So sánh sự khác nhau về màu sắc hiện thị của thảm thực vật giữa tổ hợp tự nhiện (4-3-2) và tổ hợp thực vật (5-4-3)

## Giai đoạn 3 : Phân tích chỉ số thực vật NDVI 
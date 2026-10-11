# Chương 3 : 

## Giai đoạn 3 : Phân tích chỉ số thực vật (NDVI - Normalized Difference Vegetation Index)

- Chỉ số viễn thám phổ biến nhất trên thế giới dùng để đánh giá độ phủ , mật độ và sức khỏe của thảm thực vật -> Chỉ số NDVI 

1. Khái niệm chỉ số thực vật NDVI 

- Định nghĩa : Chỉ số thực vật NDVI là chỉ số thực vật khác biệt chuẩn hóa và được sử dụng rộng rãi trong phân tích dữ liệu ảnh vệ tinh và ảnh hàng không 
-> Hiểu đơn giản chỉ số thực vật NDVI là công cụ giúp đo độ khỏe mạnh và mật độ cây cối từ trên cao xuống 

2. Nguyên lý và công thức tính toán 

- Nguyên lý cốt lõi : Cách cây xanh nhận ánh sáng mặt trời và phản xạ lại 
    + Kênh sóng đỏ (Red) : Cây cực kỳ thích và hấp thụ mạnh để quang hợp , cây càng khỏe hút càng nhiều ánh sáng đỏ -> khi cảm biến thu sóng phản xạ lại cực nhỏ
    + Kênh Hồng ngoại gần (NIR) : Cây cự kỳ ghét và phản xạ lại toàn bộ tránh bị nóng , cháy lá . Cây càng khỏe , cấu trúc lá càng dày thì phản xạ lại sóng hồnh ngoại gần càng mạnh -> Khi cảm biến thu sóng phản xạ lại cực lớn 

- Công thức toán học tổng quát : Vệ tinh nhìn vào 2 kênh sóng này tại 1 pixel và làm phép so sánh 

    NDVI = Hồng ngoại (NIR) - Đỏ (Red) / Hồng ngoại (NIR) + Đỏ (Red)

-> Từ chỉ số NDVI thu được từ 1 pixel ta suy ra được sức khỏe của thực vật : 
    + Cây rất khỏe : Phản xạ hồng ngoại cực cao + Hấp thụ đỏ -> kết quả số dương xấp xỉ = 1
    + Cây héo / khô : Phản xạ hồng ngoại thấp + Không hấp thụ đỏ -> Kết quả số dương xấp xỉ = 0 
    + Đất đá / đô thị : 2 dải sấp xỉ bằng nhau -> Kết quả quanh quẩn mức 0 
    + Nước / mây : Hấp thụ toàn bộ hồng ngoại -> kết quả ra số âm xấp xỉ = -1

3. Thang giá trị NDVI tính toán được từ đó phân loại các đối tượng 

    -1.0 <= NDVI <= 0 -> Loại đối tượng : Mây , nước , tuyết 
    0 <= NDVI <= 0.2 -> Loại đối tượng : Đất , cát , đối tượng nhân tạo (đô thị)
    0.2 < NDVI <= 0.33 -> Loại đối tượng : Thực vật yếu , cây héo / khô , cỏ thưa
    0.33 < NDVI <= 0.66 -> Loại đối tượng : Thực vật phát triển trung bình 
    0.66 < NDVI <= 1 -> Loại đối tượng : Thực vật phát triển mạnh 

4. Ứng dụng thực tế chỉ số NDVI 
    - Giám sát nông nghiệp và dự báo năng suất : Theo dõi sự phát triển của cây trồng theo mùa vụ và sớm phát hiện khu vực sâu bệnh 
    - Theo dõi hạn hán và cháy rừng : Phát hiện hiện tượng mất nước của thám thực vật để cảnh báo nguy cơ cháy rừng 
    - Theo dõi biến động thực phủ đa thời gian : So sánh ảnh NDVI ở 2 thời điểm khác nhau (vd : mùa đông vs mùa hè) để đánh giá biến động diện tích rừng 
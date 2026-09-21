Chương 2 : GPS_GNSS 

Giai đoạn 2 : Phân tích nguồn sai số và độ chính xác định vị 
-> Nối tiếp giai đoạn 1 về nguyên lý định vị , giai đoạn 2 giải mã lý do tại sao tọa độ GPS trên thực tế không bao giờ chính xác 100% mà luôn có độ lệch từ vài mét đến vài chục mét . Việc hiểu rõ bản chất các nguồn sai số giúp kỹ sư CNTT địa học thiết kế các thuật toán làm sạch dữ liệu (kalman filter , lọc bán kính accuracy) một cách chuẩn xác

    1. Phân biệt Độ chuẩn xác (Accuracy) và Sự tương đồng (Precision) 
        - Độ chuẩn xác (Accuracy) : Cho biết vị trí đo được cách với vị trí thực tế ngoài đời bao xa . Đây là mức độ tiệm cận với giá trị thực 
        -> Độ chuẩn xác càng cao thì vị trí đo được càng gần so với vị trị thực tế ngoài đời
        
        - Sự tương đồng (Precision) : Cho biết các lần đo liên tiếp tại cùng 1 vị trí có kết quả giống nhau / gần nhau đến mức nào , bất kể việc có gần với vị trí thực tế hay không 
        -> Sự tương đồng thể hiện qua nhiều lần đo liên tiếp tại cùng 1 vị trí 
            + Sự tương đồng cao + Độ chuẩn xác thấp : các lần đo trả về vị trí cụm 1 chỗ nhưng xa vị trí thực tế 
            + Sự tương đồng thấp + Độ chuẩn xác cao : các lần đo rải rác xung quanh vị trí thực tế , trung bình cộng đúng vị trí nhưng mỗi lần đo vị trí cách nhau
            + Sự tương đồng cao + Độ chuẩn xác cao : các lần đo trả về vị trí cụm 1 chỗ gần vị trí thực tế -> mục tiêu tối thượng đo đạc

        -> Với các thiết bị thu GPS dân sự (smart phone) khi thu tín hiệu trả về vị trí thường cho ra các vị trí có độ tương đồng cao nhưng độ chính xác không cao do chịu tác động của nhiều nguồn nhiễu xung quanh . 

    2. Các nguồn sai số ảnh hưởng đến độ chính xác GPS 
    - Sai số về độ chính xác không phải do ngẫu nhiên hay may mắn mà phần lớn xuất phát từ các sai số hệ thống , nó xảy ra một cách liên tục và có quy luật trong quá trình truyền / nhận tín hiệu . 
    -> Cần có các biện pháp hiệu chỉnh (trạm base , RTK ...) nếu không các yếu tố này sẽ làm cho tất cả lần đo đều bị lệch so với vị trí thực tế ngoài đời 

        2.1. Nhóm sai số từ không gian (vệ tinh và quỹ đạo)
        - Sai số từ đồng hồ vệ tinh : Dù là đồng hồ nguyên tử nhưng vẫn có độ lệch cực nhỏ , 1 nanosecond đã làm lệch 30 cm
        - Sai số do quỹ đạo vệ tinh : Quỹ đạo thực tế vệ tinh bị chệch một vài mét so với tọa độ dự báo gửi xuống máy thu 

        2.2. Nhóm sai số do môi trường truyền dẫn : Tín hiệu truyền từ vệ tinh xuống > 20.000 km đâm qua khí quyển để xuống mặt đất 
        - Trễ tầng điện thế : Tầng điện thế chứa các hạt mang điện tự do làm bẻ cong và thay đổi tốc độ truyền sóng , lệch 5m -> 15m 
        - Trễ tầng đối lưu : Hơi nước , nhiệt độ , áp xuất ở tầng khí quyển làm giảm tốc độ sóng radio , lệch 2m -> 4m

        2.3. Nhóm sai số hình học và thiết bị 
        - Độ phân bố hình học (GDOP / PDOP) : Phụ thuộc vào vị trí phân bố tương quan giữa các vệ tinh trên bầu trời
            + GDOP / PDOP thấp : Các vệ tinh phân bố rộng và đều trên bầu trời -> vùng giao thoa các mặt cầu nhỏ -> tọa độ chính xác cao 
            + GDOP / PDOP cao : Các vệ tinh tụ lại góc hẹp -> vùng giao thoa bị kéo giãn -> tọa độ bị sai số lớn 
            -> Ngưỡng PDOP yêu cầu trong thực tế : 
                + Thiết bị khảo sát trắc địa chuyên dụng : Yêu cầu PDOP < 4.0
                + Thiết bị thành lập bản đồ chuyên dụng : Yêu cầu PDOP < 6.0
                + Chỉ số PDOP > 7.0 tọa độ không đáng tin cậy / không chính xác

        - Nhiễu đa đường truyền (multipath error) : Tín hiệu dội vào tòa cao tầng , mái tôn , mặt nước trước khi chui vào ăng ten làm máu thu tính sai thời gian truyền sóng
        - Sai số trung tâm ăng- ten : Điểm thu sóng thực tế trên ăng-ten bị lệch vài milimét đến vài xentimét so với tâm vật lý của thiết bị.

    3. Các giải pháp phần cứng nâng cao độ chính xác định vị 
    - Dù máy thu độc lập thông thường bị giới hạn độ chính xác ở mức 5-10 m trong kỹ thuật chuyên dụng người ta dùng 2 công nghệ hiệu chỉnh phần cứng : 
    
        + DGPS (Differential GPS): Sử dụng một trạm Base đặt cố định tại tọa độ chuẩn để đo sai số thực tế, sau đó phát sóng hiệu chỉnh cho trạm Rover di động $\rightarrow$ Cải thiện độ chính xác xuống mức decimet (dm).

        + RTK (Real-Time Kinematic): Đo trực tiếp góc pha của sóng mang ($L_1/L_2$) thay vì chỉ đo mã tín hiệu thô $\rightarrow$ Đạt độ chính xác tuyệt đối ở mức centimet (cm) (dùng cho xe tự lái, máy bay drone trắc địa).

    4. Câu hỏi ôn tập cuối bài 

    Câu 1 : Phân biệt sự khác nhau giữa Accuracy (độ chính xác) và Precision (Sự tương đồng/ độ lặp) trong các lần đo đạc GPS . Các thiết bị smartphone dạo phố thông thường đạt được trạng thái nào tốt hơn ? 
    - Độ chính xác : Là vị trí của đối tượng đo được bằng thiết bị so với vị trí ngoài thực địa của đối tượng đó 
    -> độ chính xác càng cao vị trí đo bằng thiết bị càng tương đồng với vị trí ngoài thực địa 

    - Sự tương đồng : Là các vị trí của đối tượng đo được bằng thiết bị có tương đồng với nhau qua nhiều lần đo đạc GPS 
    -> nếu đo nhiều lại tại 1 điểm mà các kết quả thu được nằm tập trung sát nhau thì sự tương đồng cao  
    
    - Các thiết bị smartphone dạo phố phổ thông thường thu được vị trí của đối tượng có độ chính xác thấp và sự tương đồng cao do ảnh hưởng bởi nhiễu môi trường , đa đường dẫn và các giới hạn về chip ăng-ten thu tín hiệu thô dẫn đến độ chính xác thấp 

    Câu 2 : Giải thích nguyên nhân gây ra sai số đường dẫn (multipath). Tại sao hiện tượng này lại xảy ra phổ biến và khó khắc phục khi định vị trong các đô thị có nhà cao tầng 
    - Nguyên nhân dẫn đến sai số đường dẫn là khi tín hiệu từ vệ tinh đi thẳng tới máy thu bị va đập , phản xạ qua các bề mặt xung quanh , các bề mặt gây phản xạ gồm kính , tường bê tông ...
    -> Cơ chế gây ra sai số là sóng phản xạ đi đường vòng thay vì đi đường thẳng gây mất thời gian truyền hơn , khi đó máy tính lấy thông số này tính ra khoảng cách đến vệ tinh dài hơn thực tế , tạo ra các bóng ma tọa độ hoặc hiện tượng trôi tọa độ 

    - Hiện tượng này lại phổ biến và khó khắc phục định vị trong các đô thi có nhà cao tầng do ở đó có nhiều kính 

    Câu 3 : Chỉ số PDOP phản ảnh điều gì trong định vị vệ tinh ? So sánh độ chính xác tọa độ thu được khi vệ tinh tập trung ở đỉnh đầu với  phân bố góc mở rộng trên bầu trời . Ngưỡng PDOP tối đa phép khi thành lập bản đồ là bao nhiêu ? 
    - Chỉ số PDOP phản ánh sự phân bố về vị trí của các vệ tinh trên bầu trời tại 1 thời điểm 

    - Độ chính xác tọa độ thu được khi vệ tinh tập trung đỉnh đầu thì độ chính xác thấp , khi vệ tinh phân bố góc mở rộng trên bầu trời độ chính xác cao 

    - Ngưỡng PDOP tối đa phải nhỏ hơn 7.0 thì mới đủ điều kiện thành lập bản đồ 
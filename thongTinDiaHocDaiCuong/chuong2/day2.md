CHƯƠNG 2 : GNSS - GPS 

GIAI ĐOẠN 1 : Tổng quan hệ thống định vị vệ tinh GNSS và Nguyên lý định vị 

-> Mục tiêu : tìm hiểu hạ tầng định vị toàn cầu , phân biệt các khái niệm cốt lõi và giải mã nguyên lý toán học giúp máy tính xác định vị trí của bạn 

    1. Khái niệm và Phân biệt GNSS và GPS 
        - GNSS (global navigation satellite system) : Hệ thống vệ tinh dẫn đường toàn cầu 
        -> GNSS bản chất là thuật ngữ tổng quát dùng để chỉ tất cả hệ thống vệ tinh dẫn đường toàn cầu 
        -> Ý tường dẫn đến việc xây dựng hệ thống này là việc đo khoảng cách từ vị trí trên mặt đất tới các vệ tinh bằng cách dựa trên tốc độ và thời gian của sóng vô tuyến 
        -> Các hệ thống thành viên nằm trong GNSS :
            + GPS : mỹ
            + GLONASS : nga
            + BEIDOU / bắc đẩu : trung quốc...

        - GPS (global positioning system) : Hệ thống định vị toàn cầu do bộ quốc phòng mỹ phát triển 
        -> GPS có nhiệm vụ cung cấp vị trí , vận tốc , thời gian chuẩn xác cho các máy thu tín hiệu trên hoặc gần bề mặt trái đất ở mọi thời điểm , mọi điều kiện 
        -> Thực chất nhiệm vụ các vệ tinh GPS : Liên tục phát ra tín hiệu thời gian kết hợp với quỹ đạo của vệ tinh . Từ đó bộ xử lý trên máy thu ở mặt đất sẽ sử dụng
        thuật toán toán học để tính toán ra vị trí và vận tốc 
        -> Quy trình 3 bước từ "thời gian" biến thành "vị trí" và "vận tốc" :

            + Bước 1 :  Vệ tinh phát tín hiệu (thời gian và quỹ đạo)
                -> Tại 1 thời điểm , vệ tinh GPS phát ra sóng radio chứa 2 thông tin chính
                    1. "Bây giờ chính xác là T phát" (đo bằng đồng hồ nguyên tử) -> thời gian phát sóng
                    2. "Vị trí tọa độ ngoài vũ trụ của tôi là (x , y , z) -> tọa độ của vệ tinh tại thời điểm phát sóng 

            + Bước 2 : Máy thu tính ra vị trí (x , y , z)
                -> Khi sử dụng điện thoại / máy thu tín hiệu GIS nhận được tín hiệu được phát từ vệ tinh trên tại thời điểm T nhận
                    1. Tính khoảng cách đến vệ tinh phát đó bằng công thức : 
                        Khoảng cách (d) = Vận tốc sóng radio (c) x (T nhận - T phát)
                    2. Sử dụng thuật toán tam giác đạc không gian : Thu tín hiệu từ tối thiểu 4 vệ tinh cùng lúc , máy thu giải phương trình hình học không gian 3 chiều tìm ra giao điểm duy nhất -> tìm ra tọa độ (x , y , z) của đối tượng địa lý thu tín hiệu 

            + Bước 3 : Máy thu tính ra vận tốc 
                -> Sau khi có thời gian chuẩn và tọa độ đối tượng thì việc tính ra vận tốc của đối tượng được máy thu thực hiện theo 2 cách sau : 
                    1. Phương pháp khoảng cách / thời gian cơ bản : so sánh tọa độ ở 2 thời điểm liên tiếp bằng công thức
                        Vận tốc = vị trí 2 (x2 , y2 , z2) - vị trí 1 (x1 , y1 , z1) / T2 - T1
                    2. Phương pháp hiệu ứng Doppler (chính xác hơn) : Khi bạn di chuyển lại gần hoặc ra xa vệ tinh , tần số sóng radio gửi về bị co giãn nhẹ . Máy thu đo độ lệch tần số này để tính ra vận tốc tức thời và hướng di chuyển 

    2. Ba phân đoạn cấu thành hệ thống GPS 
    - Hệ thống GPS không phải một vệ tinh đơn lẻ mà là hệ thống hoàn chỉnh gồm 3 phân đoạn phối hợp chặt chẽ với nhau 

        2.1. Phân đoạn Không gian 
            - Gồm 24 vệ tinh quay trên 6 mặt phẳng quỹ đạo cách đều nhau , nghiêng 55 độ so với mặt phẳng quỹ đạo 
            - Vệ tinh bay ở độ cao xấp xỉ 20.200 km với chu kì quay 718 phút (-12 giờ)
            -> Cách phân bổ này đảm bảo tại bất kì thời điểm nào và ở bất cứ đâu trên trái đất người dùng cũng nhìn thất ít nhất 4 vệ tinh trên bầu trời 
    
        2.2. Phân đoạn điều khiển 
            - Gồm 4 trạm quan sát mặt đất tạo thành vành đai bao quanh trái đất , trong đó trạm điều khiển trung tâm đặt tại Mỹ và 4 trạm theo dõi xung quanh đặt tại
            Hawaii , đảo Ascension , Diego Garcia và Kwajalein 
            -> Nhiệm vụ : Theo dõi chuyển động quỹ đạo và hoạt động của đồng hồ vệ tinh . Việc chính xác hóa thông tin và truyền lệnh điều khiển lên vệ tinh được tiến hành 3 lần trong 1 ngày 

        2.3. Phân đoạn người dùng 
            - Bao gồm các thiết bị thu tín hiệu chuyên dụng trắc địa hoặc smart phone tích hợp GPS 
            -> Mục đích : Nhằm khai thác tọa độ của đối tượng địa lý nhằm vào các mục đích khác nhau 

    3. Nguyên lý định vị dựa vào thuật toán tam giác đạc không gian (trilateration) 
    - Mục đích là tìm ra vị trí của đối tượng địa lý với công thức cơ bản : Khoảng cách =  Vận tốc x (T nhận - T phát)
    -> Tính ra khoảng cách từ vị trí máy thu tín hiệu tới vệ tinh 

    - Dựa trên thuật toán tam giác đo đạc không gian cần ít nhất thu tín hiệu 4 vệ tinh cùng lúc : 
    -> Để xác định vị trí chính xác không gian 3D bao gồm kinh độ , vĩ độ , độ cao và quan trọng nhất là khắc phục / đồng bộ sai số đồng hồ giữa máy thu và đồng hồ nguyên tử trên vệ tinh 

    4. Câu hỏi ôn tập 
        Câu 1 : Phân biệt sự khác nhau giữa khái niệm GNSS và GPS . Kể tên 4 hệ thống GNSS lớn nhất trên thế giới hiện nay 
        -> Khái niệm của GNSS là hệ thống vệ tinh dẫn đường toàn cầu , GNSS là từ khóa chỉ chung tất cả các hệ thống vệ tinh trên thế giới
        -> Khái niệm của GPS là hệ thống định vị toàn cầu , GPS là từ khóa chỉ 1 hệ thống vệ tinh định vị của Mỹ 
        -> 4 hệ thống GNSS lớn nhất trên thế giới hiện nay : GPS , Galileo , Bắc đẩu , Glonass

        Câu 2 : Trình bày thông số kỹ thuật của phân đoạn không gian trong hệ thống GPS (số lượng vệ tinh , số mặt phẳng quỹ đạo , độ cao và chu kỳ quay)
        - Thông số kỹ thuật của phân đoạn không gian trong hệ thống GPS là : 
            + Số lượng vệ tinh : 24 vệ tinh
            + Số mặt phẳng quỹ đạo : 6 mặt phẳng cách đều nhau 
            + Độ cao : 20.200 km
            + Chu kỳ quay : 718 phút (xấp xỉ 12h) . Cụ thể mỗi vệ tinh sẽ bay qua đúng 1 điểm cho trước trên mặt đất mỗi lần 1 ngày
        -> Với thông sỗ kỹ thuật trên đảm bảo mọi thời điểm ở mọi vị trí trên thế giới đều nhìn thấy ít nhất 4 vệ tinh trên trời  

        Câu 3 : Tại sao khi định vị mặt đất bằng GPS , thiết bị thu cần nhận tín hiệu ít nhất từ 4 vệ tinh thay vì 3 vệ tinh 
        - Quy trình xác định vị trí của 1 đối tượng trên mặt đất bằng GPS : 
            Giai đoạn 1 : Phát tín hiệu 
                + Vệ tinh luôn phát ra tín hiệu gồm : T phát (thời gian lúc phát ra tín hiệu) , Tọa độ (x , y , z) của vệ tinh thời điểm phát 

            Giai đoạn 2 : Nhận tín hiệu 
                + Sử dụng thiết bị thu / smart phone mở định vị GPS : Thu tín hiệu từ vệ tinh và nhận được T thu (thời gian lúc thu được tín hiệu)
                -> Tính được khoảng cách đến vệ tinh bằng công thức : Khoảng cách = vận tốc ánh sáng X (T thu - T phát)

                + Nhưng để có thể tính ra được tọa độ của đối tượng trên mặt đất cần thu tín hiệu ít nhất từ 4 vệ tinh vì : 
                -> Giải phương trình  4 ẩn gồm x , y ,z và t : x , y ,z để xác định tọa độ của đối tượng còn t giúp tránh sai số về thời gian do đồng hồ trên vệ tinh  là đồng hồ nguyên tử thời gian chính xác , đồng hồ từ thiết bị thu đồng hồ thạch anh có thể có sai số 
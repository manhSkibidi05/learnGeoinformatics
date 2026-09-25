Review day5 : 

- Quy trình thu thập dữ liệu tọa độ bằng hệ thống GPS : 

    Bước 1 : Chuẩn bị máy thu 
        - Sử dụng các máy thu chuyên ngành để thu tín hiệu hoặc smartphone tích hợp chip GPS 

    Bước 2 : Quy trình tính toán dữ liệu thu được từ vệ tinh 
        - Gồm các bước nhỏ sau : 
            + Thu tín hiệu ít nhất 4 vệ tinh của GPS -> tín hiệu thu về là T phát và tọa độ vệ tinh (X , Y , Z)
            + Lập phương trình 4 ẩn tính toán ra tọa độ -> Dựa trên công thức : d = c X (T thu - T phát) 
            + Tính ra được tọa độ (x , y , z) và độ lệch thời gian đen ta T 
            + Chuyển tọa độ tính ra về hệ tọa độ địa lý với (kinh độ , vĩ độ , độ cao) 

    Bước 3 : Mã hóa dữ liệu thu được 
        - Mã hóa dữ liệu thu được theo định dạng text chuẩn NMEA 0183 giúp việc giao tiếp giữa phần cứng chip GPS và phần mềm GIS 

    Bước 4 : Giải mã và biểu diễn dữ liệu 
        - Giải mã dữ liệu thu được và sử dụng nó với quy trình biểu diễn dữ liệu :      
            + Sau khi giải mã tọa độ thu được đang ở hệ tọa độ địa lý 
            + Chuyển sang hệ tọa độ phẳng để hiện thị điểm đó lên bản đồ phẳng của openStreetMap 

Chương 2 - Giai đoạn 4 : Thu thập dữ liệu vị trí 

-> Hai phương thức thu thập vị trí cốt lõi 
    - Phương thức lấy vị trí một lần : 
        + Sử dụng khi người dùng thao tác chức năng dạng check-in " tìm trạm xăng gần tôi " 
        + Cơ chế : Xác định ví trí hiện tại máy thu (smartphone) , sau đó tính toán khoảng cách điểm hiện tại tới các điểm quan tâm (POI) các điểm này đã có vị trí trước đó

    - Phương thức theo dõi liên tục : 
        + Sử dụng với các ứng dụng cần theo dõi vị trí người dùng liên tục để tính toán lộ trình (grab / bee) 
        + Cơ chế : Máy thu (smartphone) lên tục kích hoạt phản hồi để tự động cập nhật tọa độ mỗi khi phần cứng di chuyển hoặc thay đổi vị trí 

Chương 2 - Giai đoạn 5 : Xử lý chuỗi quỹ đạo 

- Chuỗi quy đạo là : Dữ liệu GPS thu thập liên tục theo thời gian . Lúc này dữ liệu thô thu được chứa nhiều điểm nhiễu , do đó kỹ sư cần áp dụng 3 kỹ thuật xử lý chuyên sâu trước khi đưa vào CSDL 

    + Lọc nhiễu : 
        - Vấn đề : Khi xe dừng ngã 4 , tọa độ GPS vẫn nhảy loạn xạ quanh vị trí đó do sai số đa đường dẫn , gây cộng dồn sai lệch tổng quảng đường 
        - Giải pháp : Loại bỏ các điểm có bán kính sai số accuracy > 30m , hoặc dùng bộ lọc kalman filter 

    + Khớp bản đồ : 
        - Vấn đề : Tọa độ GPS thường bị đâm xuyên nhà cửa lệch vỉa hè
        - Giải pháp : SỬ dụng thuật toán đồ thị kế hợp xstk để khớp chuỗi điểm thô về đúng tâm đoạn đường giao thông thực tế 

    + Trích xuất điểm dừng nghỉ 
        - Giải pháp : Áp dụng thuật toán phân cụm không gian nếu nhiều điểm GPS tập trung trong bán kính nhỏ (< 20m) trong thời gian đủ lâu (> 15min) , hệ thống tự gộp lại thành 1 điểm dừng 
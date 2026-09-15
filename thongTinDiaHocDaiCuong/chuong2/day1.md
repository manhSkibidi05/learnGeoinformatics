    * GPS/GNSS

    - Các bước xác định vị trí người dùng qua GPS/ GNSS : Khi cầm điện thoại mở các ứng dụng như GG map hay grab... điện thoại hoạt động như một đầu thu thụ động
    -> Toàn bộ quá trình thu thập tọa độ và xác định vị trí ngay lập tức được thực hiện qua các bước sau :

        B1 : Vệ tinh phát tín hiệu
        - Các vệ tinh định vị (GPS , GLONASS , GALILEO , Bắc đẩu) bay quanh trái đất ở độ cao xấp xỉ 20000 km liên tục phát ra tín hiệu vô tuyến xuống dưới mặt đất
        - Tín hiệu vô tuyến này chứa 2 thông tin quan trọng :
            + Mã định danh của vệ tinh
            + Thời gian chính xác tín hiệu phát ra

        B2 : Điện thoại bắt tín hiệu
        - Chip GNSS tích hợp trong điện thoại sẽ lắng nghe và thu các sóng vô tuyến này . Điện thoại so sánh thời gian phát ghi trên tín hiệu với thời gian nhận được tín hiệu từ đó tính ra khoảng cách từ điện thoại đến vệ tinh đó
        -> Khoảng cách = Vận tốc ánh sáng X thời gian truyền sóng

        B3 : Tính toán vị trí (3D) -> sử dụng thuật toán giao các khối cầu
        - Để tìm ra tọa độ chính xác , điện thoại cần bắt tín hiệu từ ít nhất 4 vệ tinh cùng lúc
            + 3 vệ tinh giúp giao 3 khối cầu khoảng cách để tìm ra điểm kinh độ , vĩ độ và độ cao
            + vệ tinh thứ 4 dùng để khử sai số đồng hồ điện thoại

        B4 : Xuất tọa độ WGS 84 -> chuyển đổi tín hiệu thành tọa độ hiển thị
        - Chip định vị xuất ra kết quả ở dạng hệ tọa độ địa lý 3D với chuỗi dữ liệu thô dạng Lat , Long
        -> hệ điều hành adroid/ios nhận dữ liệu này cung cấp cho ứng dụng bản đồ để vẽ một chấm xanh trên màn hình 2D

    -> Nếu chỉ phụ thuộc vào sóng vệ tinh thô việc điện thoại thu 4 tín hiệu từ 4 vệ tinh có thể mất từ 30s -> 1p nên việc để xác định vị trí của bạn ngay lập tức  1- 2s dù ở bất cứ đâu cần có thêm các công nghệ hỗ trợ :
        + A-GPS : Điện thoại gửi nhận dữ liệu internet qua 4G/5G -> giảm thời gian định vị vệ tinh xuống dưới 2s
        + Wifi & Tháp sóng : Điện thoại quét/lắng nghe địa chỉ MAC và ID trạm sóng -> định vị tức thì và hỗ trợ khi ở trong nhà , dưới hầm

Review :

    - Hệ tọa độ là : Hệ thống quy tắc dùng để xác định vị trí của 1 đối tượng địa lý được xác định bằng khoảng cách hoặc góc đo của đối tượng địa lý đó so với gốc tọa độ

    - 2 Hệ tọa độ chính là :
        + Hệ tọa độ địa lý : Trái đất được biểu diễn dưới dạng 3D , đơn vị đo của 1 tọa độ là độ thập phân
        -> Sử dụng để thu thập dữ liệu từ vệ tinh và xác định vị trí của 1 đối tượng bằng hệ thống GPS

        + Hệ tọa độ phẳng : Trái đất được biểu diễn dưới dạng 2D , đơn vị đo của 1 tọa độ là mét
        -> Sử dụng để tính toán đường đi và diện tích

    - Vị trí của 1 đối tượng địa lý là : Gồm vị trí tuyệt đối thể hiện qua tọa độ hoặc địa chỉ duy nhất , vị trí tương đối là mối quan hệ không gian của đối tượng đó với các đối tượng xung quanh
    - Tọa độ của 1 đối tượng địa lý là : là những dữ liệu số dùng để xác định vị trí tuyệt đối của đối tượng địa lý

    - Đối tượng địa lý :
        + Dữ liệu không gian (spatial data) : trả lời câu hỏi ở đâu
            - Vị trí :
                + Vị trí tuyệt đối : thể hiện bằng tọa độ
                + Vị trí tương đối : mối quan hệ không gian với các đối tượng khác
            - Kích thước , hình dáng
        + Dữ liệu thuộc tính (Attribute data) : trả lời câu hỏi cái gì , như thế nào
            - Thông tin mô tả về đặc điểm của đối tượng :
                + tên
                + năm xây dựng
                + diện tích...

    - GNSS : Là hệ thống định vị vệ tinh toàn cầu trong đó gồm GPS , Galileo...
    -> Cách định vị vị trí : Điện thoại / thiết bị đóng vai trò máy thu sóng vô tuyến từ ít nhất 4 vệ tinh sau đó sử dụng thuật toán giao giữa các khối cầu để tính ra
    tọa độ 3D (x , y , z) + Độ lệch thời gian đồng hồ (t lệch)

    -> Hệ tọa độ cung cấp quy tắc (gốc tọa độ , đơn vị đo) cách biểu diễn 1 tọa độ của 1 đối tượng địa lý , Để xác định tọa độ cụ thể của bản thân hay 1 đối tượng địa lý cần các thiết bị đo đạc (máy thu GNSS/GPS , máy đo đạc) sau đó từ các dữ liệu đó tính toán chính xác ra tọa độ

Question : 

    Câu 1 : Các yếu tố nào ảnh hưởng được đến biểu diễn dữ liệu Raster ? Giải thích ? 
    -> Các yếu tố ảnh hưởng đước đến biểu diễn dữ liệu raster là : 
        + Kích thước của 1 ô pixel -> kích thước càng nhỏ độ phân dải càng lớn 
        + Kích thước vùng phủ : Phạm vi không gian mà toàn bộ ma trận Raster bao phủ 
        + Giá trị 1 ô lưới : Dữ liệu liên tục (số thực) hay dữ liệu rời rạc (số nguyên) , kiểu dữ liệu lưu trữ (8bit , 16bit...) quyết định tới dải giá trị màu
        + Điểm mốc tọa độ : Quyết định vị trí của ma trận ô lưới trên hệ tọa độ thực địa

    Câu 2 : Dữ liệu dạng điểm và dạng vùng có thể chuyển đổi qua lại với nhau không ? Giải thích ?
    -> Có thể chuyển đổi qua lại nhau vì dữ liệu dạng điểm hay vùng gồm 2 khía cạnh : 
        1. Chuyển đổi theo tỷ lệ bản đồ 
            vd : tphn với bản đồ thế giới rất nhỏ nên dữ liệu dạng điểm , với bản đồ Việt Nam tphn rất to nên dữ liệu dạng vùng
        2. Chuyển đổi bẳng kĩ thuật / thuật toán GIS 
            + Từ vùng sang điểm : Sử dụng thuật toán Tâm vùng để thu gọn 1 polygon thành 1 point đại diện
            + Từ điểm sang vùng : 
                -> Tạo vùng đệm (buffer) : Tạo vùng với bán kính r quanh điểm ban đầu
                -> Sử dụng thuật toán Nội suy : Tối ưu hóa từ tập hợp các điểm đo đạc để tạo thành không gian bao phủ 

    Câu 3 : Với bảng dữ liệu thuộc tính , hàng ngang , cột dọc cho biết điều gì ? Có thể thực hiện thao tác nào với bảng thuộc tính ? 
    -> Ý nghĩa hàng và cột :
        + Hàng ngang : 1 bản ghi đại diện cho 1 đối tượng địa lý cụ thể , mỗi hàng nối 1-1 với 1 hình học trên bản đồ qua mã ID
        + Cột dọc : 1 trường dữ liệu đại diện cho 1 thuộc tính của tất cả đối tượng 
    -> Các thao tác có thể thực hiện với bảng thuộc tính : 
        + Thao tác cơ bản : Thêm , sửa , xóa các bản ghi hoặc trường dữ liệu 
        + Truy vấn và lọc : Lọc đối tượng theo điều kiện nhất định 
        + Tính toán số liệu : Tính toán giá trị cột tự động bằng công thức toán học 
        + Liên kết dữ liệu : Nối bảng thuộc tính với bảng dữ liệu bên ngoài thông qua trường khóa chung
        + Thống kê dữ liệu : Tính tổng , trung bình , min , max các cột dữ liệu của mỗi thuộc tính   


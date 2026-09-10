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

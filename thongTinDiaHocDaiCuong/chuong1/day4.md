Review day 3 :

    - Quy trình lưu trữ 1 đối tượng địa lý :
        B1 : Mô tả đối tượng địa lý -> Thu thập các dữ liệu của đối tượng đó
            + Thu thập dữ liệu không gian : Vị trí , kích thước của đối tượng . vd : tọa độ của đối tượng
            + Thu thập dữ liệu thuộc tính : Thông tin phi vật lý của đối tượng . vd : tên , đánh giá của đối tượng

        B2 : Mô hình hóa đối tượng địa lý -> Chuyển hóa các dữ liệu đã thu thập được thành dạng mô hình cho máy tính có thể hiểu được
            + Xác định loại mô hình phù hợp với đối tượng
                - Mô hình vector : Sử dụng với các đối tượng rời rạc có ranh giới rõ ràng . vd : hồ nước , điểm dừng xe bus...
                -> Mô hình vector xây dựng các đối tượng dựa trên hình học các dạng phổ biến là :
                    + Point (điểm) : Chỉ 1 đối tượng riêng lẻ duy nhất tạo thành từ 1 đỉnh (tọa độ)
                    + LineString (đường) : Chỉ 1 đối tượng cần phải nối với nhau tạo thành các đường không khép kín tạo thành tối thiểu 2 đỉnh
                    + Polygon (vùng) : Chỉ 1 đối tượng cần nối với nhau tạo thành vùng khép kín với đỉnh đầu trùng với đỉnh cuối và tối thiếu 4 đỉnh
                - Mô hình raster : Sử dụng với các đối tượng liên tục . vd : thời tiết , nhiệt độ , địa hình...
                -> Mô hình raster xây dựng các đối tượng dựa trên 1 ô dữ liệu , với 1 ảnh có nhiều ô dữ liệu và kích thước ô dữ liệu càng nhỏ thì ảnh có độ phân giải càng lớn tương ứng việc kích thước file lớn theo

            + Lựa chọn định dạng dữ liệu dựa trên mô hình vừa xác định
            -> Định dạng dữ liệu là cấu trúc dữ liệu xây dựng dựa trên các mô hình nhằm lưu trữ và quản lý dữ liệu của đối tượng địa lý
                - Mô hình vector -> định dạng GeoJSON
                {
                    "type" : "FeatureCollection", -> Cố định : định dạng file cho phép lưu trữ các đối tượng địa lý
                    "features" : [
                        {
                            "type" : "Feature", -> Cố định : định dạng kiểu để lưu trữ 1 đối tượng địa lý gồm 1 properties và 1 geometry
                            "properties" : {
                                "name" : "Tháp rùa" , "rating" : 3.6  -> Linh hoạt : lưu trữ dữ liệu phi vật lý của đối tượng
                            },
                            "geometry" :{
                                "type" : "Point" -> Cố định : định dạng kiểu hình học của mô hình vector
                                "coordinates" : [105.2727 28.2727]
                            }
                        }
                    ]
                }
                - Lợi ích với định dạng GeoJSON :
                    + Lưu các dữ liệu chung 1 file
                    + Lưu trữ nhiều đối tượng địa lý với các loại hình khác nhau

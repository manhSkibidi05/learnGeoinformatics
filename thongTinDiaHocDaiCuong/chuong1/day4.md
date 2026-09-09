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

Review :

    - CNTT : là ngành sử dụng phần cứng , phần mềm và mạng máy tính để thu thập , xử lý , lưu trữ , truyền đạt và bảo vệ thông tin nhằm phục vụ nhu cầu con người

    - CNTT địa học : là ngành ứng dụng CNTT ngoài ra sử dụng thêm viễn thám và định vị để thu thập , xử lý , lưu trữ , mô phỏng và truyền đạt dữ liệu không gian địa lý nhằm phục vụ quy hoạch đô thị , dự báo thời tiết , tối ưu hóa tuyến đường giao thông...

    - Thông tin là : dữ liệu khi đặt trong 1 ngữ cảnh nhất định được coi là thông tin , có ý nghĩa đối với người dùng và giúp người dùng có thêm hiểu biết về 1 vấn đề , sự vật , hiện tượng...

    - Dữ liệu là : chuỗi các con số , chữ viết , hình ảnh , âm thanh... dữ liệu thô chưa qua xử lý và không có ý nghĩa gì đối với người dùng khi nhìn các dữ liệu riêng lẻ . Dữ liệu là sự biểu diễn của thông tin vì thông tin mang tính trừu tượng không thể lưu trữ và truyền đạt đi nên cần biến thông tin thành dữ liệu

    - Dữ liệu không gian địa lý là : Gồm 2 dữ liệu chính là dữ liệu không gian và dữ liệu thuộc tính mang thông tin về 1 đối tượng địa lý trên trái đất được lưu trữ dưới dạng dữ liệu
        + dữ liệu không gian : các thông tin về tọa độ , hình dạng , vị trí -> trả lời câu hỏi đối tượng này ở đâu
        + dữ liệu thuộc tính : các thông tin về đặc điểm , tính chất , tên gọi -> trả lời câu hỏi đối tượng này như thế nào

    - Các bước để lưu trữ 1 đối tượng địa lý thành dữ liệu không gian địa lý:
        + B1 : thu thập thông tin về đối tượng địa lý đó gồm dữ liệu không gian và dữ liệu thuộc tính
        + B2 : mô hình hóa thông tin đó -> mô hình hóa là việc biến thông tin thành cấu trúc dữ liệu giúp lưu trữ thông tin dưới dạng dữ liệu 1 cách có quy tắc và làm cho máy tính có thể hiểu được
        -> 2 mô hình phổ biến để chuyển hóa thông tin thành dữ liệu không gian địa lý :
            + mô hình vector : mô hình biểu diễn các đối tượng thành các dạng hình học gồm điểm , đường , vùng
            -> phù hợp với các đối tượng rời rạc và có ranh giới nhất định

            + mô hình raster : mô hình biểu diễn các đối tượng thành các ô pixel mỗi ô chứa dữ liệu của đối tượng đó
            -> phù hợp với các đối tượng liên tục và không có ranh giới nhất định
        -> Việc mô hình hóa đối tượng thực chất việc biến thông tin mang tính trừu tượng của đối tượng thành các cấu trúc lưu trữ dữ liệu cho máy tính hiểu được

        + B3 : Lưu trữ dữ liệu không gian và dữ liệu thuộc tính thông qua khóa id nhất định cho mỗi đối tượng tạo thành dữ liệu không gian địa lý hoàn chỉnh
        -> Tạo mối liên kết giữa dữ liệu không gian và thuộc tính thành 1 dữ liệu không gian địa lý

Chương 3 : Hệ tọa độ và phép chiếu bản đồ (CRS - COORDINATE REFERENCE SYSTEM)

    1. Bản chất của hệ tọa độ : Từ trái đất đến máy tính phẳng

    - Để đưa một vị trí thực tế trên bề mặt trái đất vào máy tính xử lý chúng ta phải trải qua quy trình mô hình hóa toán học 3 bước
        1. Trái đất thực tế : Không phải hình cầu hoàn hảo mà là khối GeoId lồi lõm không thể biểu diễn bằng công  thức toán học
        2. Mô hình hóa toán học xấp xỉ : Sử dụng khối toán học xấp xỉ hình trái đất là Ellipsoid -> giúp tính toán bằng máy tính
        3. Gốc tọa độ : Để định vị và neo ellipsoid vào đúng vị trí thực tế của trái đất người ta xác định hướng của  ellipsoid gọi là datum  -> giúp xác định tọa độ của 1 địa điểm 1 cách chính xác nhất

    -> Đưa vị trí thực tế của 1 đối tượng địa lý vào cho máy tính có thể xử lý được thì phải xác định hệ tọa độ hiện tại
        + Mỗi hệ tọa độ sẽ có gốc tọa độ khác nhau từ đó xác định vị trí tọa độ của đối tượng sẽ khác nhau

    -> Bản chất hệ tọa độ là có gốc tọa độ đã được đặt cố định và từ đó có thể tính toán tọa độ của đối tượng địa lý thực chất là việc tính toán khoảng cách của vị trí địa lý đó so với gốc tọa độ

        + Tính toán khoảng cách giữa 2 điểm : Máy tính chỉ dùng công thức hình học để tính toán khoảng cách giữa 2 điểm bằng cách tính khoảng cách từ từng điểm tới gốc tọa độ

        + Chuyển đổi hệ tọa độ : Bản chất là phép toán tịnh tiến và quay hệ trục -> rời điểm tính tọa độ từ gốc A sang gốc B và tính toán lại các con số khoảng cách tương ứng

    2. Hai hệ tọa độ không gian địa lý phổ biến

        2.1. Hệ tọa độ địa lý
            - Bản chất là : Sử dụng hệ tọa độ mặt cong 3D
            - Đơn vị đo : Tính độ thập phân thông qua cặp góc kinh độ vĩ độ
            - Gốc tọa độ : Giao điểm giữa kinh tuyến GreenWich và đường xích đạo
            - Mô hìh chuẩn phổ biến : WGS84
            - Ứng dụng : ĐỊnh vị GPS trên điện thoại di động và lưu trữ dữ liệu dạng GeoJSON

        -> Ứng dụng chính là giúp thu thập dữ liệu từ vệ tinh hoặc thiết bị định vị ban đầu luôn được lưu tại hệ tọa độ địa lý này

        2.2. Hệ tọa độ dự chiếu / phẳng
            - Bản chất là : Sử dụng công thức toán học trải 3D sang 2D
            - Đơn vị đo : Mét
            - Ứng dụng : Bắt buộc sử dụng hệ tọa phẳng để tính toán khoảng cách thực tế , diện tích thửa đất , vẽ bán kính vùng đệm

        -> Ứng dụng chính là tính toán và đo đạc 1 cách chính xác

    3. Mã định danh tiêu chẩn EPSG bắt buộc phải nhớ
        - EPSG:4326 (WGS 84) : Hệ tọa độ địa lý toàn cầu , đây là hệ tọa độ mặc định mà chip GPS trên điện thoại trả về cũng là chuẩn tọa độ file GeoJSON
        - EPSG:3857 : Hệ tọa độ phẳng dùng cho bản đồ web
        - EPSG:4756 / EPSG:5899 (VN-2000) : Hệ tọa độ phẳng quốc gia Việt Nam bắt buộc dùng khi làm việc cơ quan nhà nước , quy hoạch đất ....

    4. Câu hỏi ôn tập

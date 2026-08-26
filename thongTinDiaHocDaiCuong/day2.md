Review Ngày 1 :

    - CNTT : Là ngành sử dụng các thiết bị công nghệ , phần mềm  , phần cứng... giúp thu thập , lưu trữ , quản lý , bảo vệ , phân tích và truyền tải thông tin đến người dùng

    - CNTT địa học : Là ngành ứng dụng nguyên lí kĩ thuật từ 2 ngành CNTT và Khoa học máy tính (cơ sở dữ liệu , thuật toán , web/mobile , trực quan hóa dữ liệu , điện toán đám mây và AI). Từ các nguyên lí và kĩ thuật trên sử dụng giúp thu thập , lưu trữ , quản lý , bảo vệ , phân tích và truyền tải dữ liệu mang thuộc tính không gian đến người dùng

    - CNTT địa học có thể chia ra làm hệ sinh thái 3S với 3 kỹ thuật được sử dụng hầu hết trong các sản phẩm của ngành :
        + GIS : Là hệ thống cơ sở dữ liệu nâng cao giúp lưu trữ dữ liệu không gian , từ đó có thể truy vấn , phân tích và đưa ra dự đoán dựa trên dữ liệu này
        -> Ngoài ra GIS có 5 thành phần : people , data (ở phía trên) , software , hardware , procedures .
        -> Chức năng mạnh nhất của GIS không phải là lưu trữ dữ liệu mà là phân tích không gian : phân tích vùng đệm , chồng xếp bản đồ , tìm đường đi tối ưu

        + RS (remote sensing - viễn thám) : Là kỹ thuật thu thập dữ liệu mà không cần tiếp xúc thông qua cảm biến của vệ tinh , drone bằng cách sử dụng hình ảnh được cung cấp kết hợp với thuật toán của computer vision (thị giác máy tính) trả về dữ liệu của đối tượng địa lí này (nhiệt độ , độ ẩm , ...)

        + GNSS / GPS : Là hệ thống thu thập dữ liệu gồm tọa độ (kinh độ , vĩ độ , độ cao) của 1 đối tượng tại 1 thời điểm nhất định

        -> Mối liên kết của 3 kỹ thuật trên trong 1 hệ thống hoàn chỉnh :
            + GNSS/GPS : Cung cấp tọa độ của 1 đối tượng
            + RS : Cung cấp dữ liệu nền / lớp phủ (mặt)
            + GIS : Là bộ não tích hợp cả tọa độ và lớp phủ để phân tích , truy vấn và đưa ra quyết định

    - Dữ liệu là : Các con số , chữ viết , hình ảnh chưa qua xử lí và không mang ý nghĩa nào đối với người dùng
    -> Dữ liệu là sự biểu diễn của thông tin do thông tin mang tính trừu tượng nên để tồn tại trong thế giới vật lý thông tin bắt buộc phải mặc một lớp áo dữ liệu . lưu trữ thông tin lại bằng cách biến nó thành dữ liệu và khi đặt dữ liệu này vào 1 ngữ cảnh mới sẽ tạo ra 1 thông tin mới

    - Thông tin là : Bao gồm dữ liệu + ngữ cảnh tạo ra 1 thông tin và nó mang ý nghĩa đối với người dùng

    - Hiểu biết là : Bao gồm thông tin + tư duy của người dùng , khi người dùng tiếp nhận thông tin với tư duy khác nhau mỗi người sẽ có 1 hiểu biết khác nhau về chung
    cùng  1 thông tin

    - Trí tuệ là : Bao gồm hiểu biết + hành động đúng đắn , Khi người dùng có trí tuệ dựa trên hiểu biết về 1 vấn đề thì họ sẽ đưa ra hành động khi gặp vấn đề đó

Chương 2 : Mô hình và định dạng dữ liệu không gian

    1. Bản chất của dữ liệu không gian địa lý (Geospatial Data)
        - Mô tả hóa là : Quá trình thu thập , liệt kê , diễn đạt các đặc điểm của 1 đối tượng thực tế dưới dạng tư duy con người (văn bản , lời nói , ghi chú)
        -> Mô tả 1 đối tượng tức là thu thập , liệt kê các thông tin của đối tượng đó và hướng tới người nhận là con người

        - Để mô tả 1 đối tượng địa lý sử dụng dữ liệu không gian địa lý , dữ liệu này gồm 2 phần tách biệt :
            -> Dữ liệu không gian : Trả lời câu hỏi ở đâu -> dữ liệu này cung cấp vị trí địa lý , hệ tọa độ , hình dạng (X,Y,Z, điểm , đường , vùng) và mối quan hệ vị trí
            -> Dữ liệu thuộc tính : Trả lời câu hỏi cái gì , bao nhiêu , như thế nào -> Dữ liệu mô tả các đặc điểm phi không gian mô tả đặc điểm của đối tượng(không có trên bản đồ) vd : tên , chiều cao tòa nhà , nhiệt độ không khí ...

        -> Dữ liệu không gian :
            + Bản chất : ví trí , hình dạng của 1 đối tượng địa lý
            + Dạng dữ liệu máy tính lưu : Tọa độ (X, Y , Z) . vd : POINT(105.8542 , 21.0285)
        -> Dữ liệu thuộc tính :
            + Bản chất : Đặc điểm , thông tin của 1 đối tượng địa lý
            + Dạng dữ liệu máy tính lưu : Chữ , số , bảng (table/database) . vd : Tên : hồ hoàn kiếm , diện tích : 5km
        -> Dữ liệu không gian địa lý :
            + Bản chất : Gồm cả dữ liệu không gian và dữ liệu thuộc tính
            + Dạng dữ liệu máy tính lưu : Tệp GIS hoàn chỉnh . vd : GeoJSON ...

    2. Mô hình dữ liệu không gian kinh điển
        - Mô hình hóa là : Quá trình đơn giản hóa và chuyển đổi đối tượng bên ngoài thế giới thực thành các cấu trúc dữ liệu kỹ thuật số có quy tắc để máy tính có thể
        hiểu được giúp lưu trữ và tính toán
        -> Mô hình hóa là quá trình biến đổi 1 đối tượng thành 1 cấu trúc dữ liệu có thể giúp máy tính hiểu được

        - Quy trình thực hiện xây dựng cơ sở dữ liệu GIS : Mô tả -> Mô hình hóa
            + B1 : Mô tả (giai đoạn thu thập và khái niệm hóa)
                - Việc cần làm : Thu thập dữ liệu đối tượng ngoài thực địa (tọa độ , hình ảnh...) , sử dụng ngôn ngữ tự nhiên để mô tả đối tượng là gì , gồm thuộc tính gì và mục đích quản lý là gì
                - Kết quả : Tạo ra mô hình khái niệm đối tượng

            + B2 : Mô hình (Giai đoạn thiết kế cấu trúc và kỹ thuật)
                - Việc cần làm : Từ mô tả ở b1 bạn dịch các khái niệm đó sang ngôn ngữ máy tính có thể hiểu được bằng cách quyết định kiểu dữ liệu hình học và cấu trúc bảng thuộc tính
                - Kết quả : Tạo ra mô hình logic và vật lý trong hệ thống GIS

        - Để đưa các đối tượng địa lý vào máy tính xử lý chúng ta cần mô hình hóa các đối tượng địa lý đó và 2 mô hình cơ bản là : Mô hình Vector và Mô hình Raster

        2.1. Mô hình dữ liệu Vector
            - Định nghĩa : Mô hình dữ liệu vector sử dụng để biểu diễn các đối tượng địa lý dưới dạng các đối tượng hình học có ranh giới rõ ràng thông qua các
            đỉnh (vertices) liên kết với nhau . Một đỉnh là một vị trí không gian được xác định bởi cặp tọa độ (X , Y) đôi khi có thêm độ cao Z

            -> Sử dụng với các đối tượng rời rạc có ranh giới rõ ràng (thường là đối tượng nhân tạo hoặc quy hoạch)

            - Ba kiểu hình học Vector cốt lõi :
                + Điểm (Point) : Là một đỉnh đơn chỉ có giá trị tọa độ và các thuộc tính đi kèm , không có thuộc tính về chiều dài và diện tích
                -> vd : vị trí cây xăng , cột mốc lộ giới

                + Đường (Line / Polyline) : Hệ thống các đỉnh liên kết với nhau bằng các phân đoạn thẳng nhưng không khép kín (điểm đầu và điểm cuối khác nhau) . Đường có thuộc tính chiều dài nhưng không có diện tích được cấu hình từ ít nhất 2  đỉnh
                -> vd : đường giao thông , sông ngòi

                + Vùng (Polygon) : Hệ thống các đỉnh liên kết với nhau khép kín (điểm đầu và điểm cuối trùng nhau) , tạo thành hình 2 chiều đóng . Vùng có các thuộc tính chu vi và diện tích , thường được cấu hình từ ít nhất 4 đỉnh trở lên
                -> vd : ranh giới tỉnh , hồ nước

            -> Mỗi đỉnh được xác định dựa  trên cặp tọa độ (X , Y) trên bản đồ :
                + Dạng diểm : Xác định bằng 1 cặp tọa độ (X, Y)
                -> Đối tượng : Tháp rùa , máy tính lưu trữ : Point(104.8524 , 21.0285)
                -> Ý nghĩa : Máy tính cắm 1 mốc duy nhất tại kinh độ X và vĩ độ Y

                + Dạng đường : Xác định bằng chuỗi liên tiếp các cặp tọa độ (X1, Y1) , (X2 , Y2) ... (Xn , Yn) nối với nhau bằng các đoạn thẳng
                -> Đối tượng : Đường đinh tiên hoàng , máy tính lưu trữ : LineString(105.8521 21.0298, 105.8530 21.0280, 105.8541 21.0265)
                -> Ý nghĩa : Máy tính vẽ 1 con đường xuất phát từ đỉnh (X1 , Y1) nối sang đỉnh (X2 , Y2) và kết thúc tại đỉnh (X3 , Y3)

                + Dạng vùng : Xác định bằng một chuỗi tọa độ khép kín , trong đó đỉnh đầu và cuối có tọa độ trùng nhau (X1 , Y1) = (Xn ,Yn)
                -> Đối tượng : Bề mặt nước hồ hoàn kiếm , máy tính lưu trữ : Polygon((105.8521 21.0298, 105.8530 21.0280, 105.8541 21.0265 , 105.8521 21.0298))
                -> Ý nghĩa : Nối 4 điểm theo thứ tự và quây lại điểm xuất phát tạo thành 1 đa giác khép kín , phần không gian bên trong được hiểu là diện tích mặt hồ

            -> Cách lựa chọn hình học vector cho mô hình vector :
                1. Tỷ lệ bản đồ - Yếu tố quan trọng nhất
                - Kích thước của đối tượng cần biểu diễn so với phạm vi bản đồ sẽ quyết định hình dạng học vector
                    + Tỷ lệ nhỏ (nhìn từ xa / toàn cảnh) : Đối tượng thu nhỏ thành 1 chấm -> chọn Point
                    + Tỷ lệ lớn (nhìn cận cảnh / chi tiết) : Đối tượng lộ rõ diện tích , ranh giới và chiều rộng -> chọn Polygon hoặc Line

                2. Mục đích và bài toàn quản lý
                - Cùng 1 thời điểm và góc nhìn , nhưng bài toán bạn cần giải quyết sẽ quyết định dạng dữ liệu
                    + Bài toán định tuyến / tìm đường : Con đường mô hình hóa dạng Line để tính toán thuật toán đường đi ngắn nhất
                    + Bài toán quản lý diện tích / giải phóng mặt bằng : Con đường đó phải được mô hình hóa dạng Polygon để tính chính xác diện tích mặt đường và vỉa hè cần đền bù

                3. Sự thay đổi theo thời gian
                - Khi đối tượng thực tế có sự phát triển hoặc biến đổi theo thời gian , dạng vector cũng có thể thay đổi
                    + năm 2000 : 1 khu dân cư nhỏ biểu diễn bằng dạng điểm
                    + năm 2027 : khu dân cư đô thi họa rộng lớn cập nhật thành dạng vùng

            -> Đối tượng muốn biểu diễn -> Đối tượng đóng vai trò gì trong bài toán -> Bản đồ đang tỷ lệ nào -> Chốt hình học vector cho đối tượng

            -> Lưu ý kĩ thuật : Trong cấu trúc dữ liệu không gian , một lớp dữ liệu vector chỉ chứa duy nhất một kiểu hình học (một lớp toàn Point hoặc toàn Polygon)

        2.2. Mô hình dữ liệu Raster
            - ĐỊnh nghĩa : Thích hợp nhất để mô hình hóa các hiện tượng thay đổi liên tục trên bề mặt trái đất và không có ranh giới rời rạc
            vd : độ cao địa hình , nhiệt độ , lượng mưa...

            - Cấu trúc : Chia bề mặt trái đất thành một mạng lưới các ô vuông bằng nhau (cell/pixel) tổ chức theo hàng và cột . Mỗi ô vuông sẽ lưu trữ đúng 1 giá trị
            số biểu thị cho thuộc tính của vị trí địa lý đó
                + Kích thước 1 ô vuông : Xác định độ phân giải ngoài không gian -> vd : 1 ô 10m X 10m vậy mỗi ô trên máy tính đại diện cho 100m2 ngoài thực địa
                + Giá trị ô vuông : Là một giá trị số địa diện cho hiện tượng địa lý

        2.3. So sánh Mô hình Raster và Vector
            - Mô hình Vector :
                + Bản chất vị trí : Xác định bằng tọa độ điểm chính xác (x , y)
                + Lưu thuộc tính : Được tách biệt làm 2 thành phần độc lập nhưng nối với nhau qua mã định danh

            - Mô hình Raster :
                + Bản chất vị trí : Xác định bằng vị trí ô trong mạng lưới ma trận
                + Lưu thuộc tính : Lưu trực tiếp dưới dạng giá trị số của từng ô lưới

    3. Các định dạng dữ liệu không gian hiện đại
    - Định dạng dữ liệu là : Chuẩn các tệp tin và kiến trúc thế hệ mới được thiết kế dựa trên các mô hình Vector/Raster để tối ưu hóa cho điện toán đám mây , xử lý dữ liệu lớn và truyền tải qua internet
    -> Máy tính không thể hiểu các khái niệm điểm , vùng hay ảnh vệ tinh . Muốn lưu trữ chúng nhà phát triển phải tạo ra tệp tin (định dạng) tuân theo đúng quy tắc của mô hình dữ liệu :
        + Dựa trên mô hình Vector (Point , Line , Polygon + Bảng thuộc tính)
        -> Các định dạng sẽ được thiết kế để lưu chuỗi tọa độ (X , Y) và bảng dữ liệu đi kèm . vd : GeoJSON

        + Dựa trên mô hình Raster (Ma trận Pixel r, c + Giá trị ô)
        -> Các định dạng sẽ được thiết kế để lưu cấu trúc mảng ô vuông , tọa độ mốc Origin và giá trị số của từng ô . vd ; GeoTIFF

    - Trong thực tế phần mềm , dữ liệu không gian tồn tại dưới rất nhiều định dạng khác nhau tùy mục đích sử dụng . Dưới đây là các định dạng buộc phải biết

        3.1. Định dạng vector phổ biến

        * GeoJSON (mã nguồn js) : Khác với các định dạng cũ như Shapefile (bắt buộc 1 file chỉ chứa toàn điểm , hoặc toàn đường , vùng)
        -> File GeoJSON dạng FeatureCollection cho phép bạn trộn lẫn nhiều kiểu hình học trong cùng 1 file duy nhất

        - Cấu trúc 1 file GeoJSON :
            {
                "type" : "FeatureCollection" , -> cố định : bắt buộc phải khai báo cấp file
                "features" : [
                    {
                        "type" : "Feature",  -> cố định : bắt buộc khai báo cấp đối tượng
                        "properties" : " {
                            "ten" : "Tháp rùa"  -> Khu vực tự do thêm/sửa thuộc tính cho đối tượng này
                        }
                        "geometry" : {
                            "type" : "Point",  -> cố định : bắt buộc dùng đúng 1 trong 7 kiểu hình học của vector
                            "coordinates" : [105 , 21]
                        }
                    }
                ]
            }

        -> Cấu trúc đóng gói :
            1. "type" : "FeatureCollection" : Đại diện cho tập hợp danh sách nhiều "Feature" trong cùng 1 file
            2. "type" : "Feature" : Đại diện cho 1 đối tượng địa lý hoàn chỉnh gồm 1 "geometry" và 1 "properties"

        -> Các loại hình học của vector : Point , LineString , Polygon , MultiPoint , MultiLineString , MultiPolygon , Feature , FeatureCollection
            + Feature là : đại diện cho 1 đối tượng địa lý hoàn chỉnh
            + MultiPoint là : gồm nhiều cặp tọa độ độc lập nhau cùng nằm trong 1 mảng
            + MultiLineString : gồm nhiều đường/đoạn độc lập , bị chia cắt đứt đoạn trong không gian nhưng vẫn chung 1 đối tượng quản lý
            + MultiPolygon : gồm nhiều vùng độc lập nằm tách rời nhau nhưng hợp lại thành 1 đơn vị địa lý
            -> Dạng hình học Multi- ra đời nhằm giải quyết các trường hợp một đối tượng địa lý bị phân tách trong không gian nhưng vẫn cần gắn chung một bộ thông tin thuộc tính duy nhất

        -> Lưu ý quan trọng :
            + GeoJSON công thức tọa độ : [X , Y] = [Kinh độ , Vĩ độ]
            + GG map công thức tọa độ : [X , Y] = [Vĩ độ , Kinh độ]
            -> cách đọc tọa độ của GeoJSON khác so với tọa dộ của GG map nên khi sử dụng tọa độ gg map cần đảo ngược lại khi thêm vào file GeoJSON

        * ESRI Shapefile (*.shp)
            - Định dạng dữ liệu vector cổ điển do Esri phát triển . Một bộ dữ liệu Shapefile bắt buộc đi kèm tối thiểu 3 file có tên giống nhau nhưng phần mở rộng khác nhau :
                + .shp : lưu trữ dữ liệu hình học vector
                + .shx : lưu trữ chỉ mục vị trí hình học giúp truy cập nhnah
                + .dbf : lưu trữ các thuộc tính phi không gian dạng bảng
            -> hạn chế : tên cột thuộc tính tối đa 10 kí tự , dung lượng file giới hạn 2GB

        3.2. Các định dạng Raster phổ biến

        * GeoTIFF (*.tif / *.img) :
            - Thực chất là tệp ảnh TIFF tiêu chuẩn nhưng được nhúng thêm các thẻ siêu dữ liệu (GeoKeys) chứa các thông tin về hệ tọa độ , phép chiếu phẳng và tọa độ thực địa của các pixel ảnh

        * Cloud-Optimized GeoTIFF (COG) :
            - Cấu trúc GeoTIFF cải tiến tối ưu cho hạ tầng đám mây . Nó cho phép máy chủ web chỉ cần tải đúng vùng dữ liệu hoặc mức thu phóng mà client dang cần thông qua cơ chế HTTP Range Requests , giúp tiết kiệm băng thông mà không cần tải toàn bộ tệp tin dung lượng lớn về máy

        3.3. Định dạng Big data nâng cao

        * GeoParquet : Định dạng lưu trữ dữ liệu dạng cột tối ưu hóa việc phân tích dữ liệu không gian cực lớn trên các công cụ Big data như Apache Spark hay DuckDB

        * STAC : Chuẩn REST API / JSON dùng để mô tả và quản lý các danh mục dữ liệu không gian - thời gian lớn

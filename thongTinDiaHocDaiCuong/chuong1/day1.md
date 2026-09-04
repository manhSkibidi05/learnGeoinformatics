Chương 1 : Công nghệ thông tin địa học và hệ sinh thái 3S

    1. Khái niệm về công nghệ thông tin địa học
        - Công nghệ thông tin là : Là ngành sử dụng các thiết bị công nghệ như máy tính , phần mềm , ... để thu thập , lưu trữ , xử lý , bảo vệ và truyền tải
        thông tin (các hoạt động liên quan đến thông tin) . Từ đó nó phát triển thành nhiều chuyên ngành nhỏ khác : AI , big data , kiểm thử...

        - Công nghệ thông tin địa học (Geoinformatics) : Là ngành ứng dụng các nguyên lí và kĩ thuật từ 2 ngành CNTT và khoa học máy tính trong đó các nguyên lí và kĩ thuật cần thiết (cơ sở dữ liệu , thuật toán , trực quan hóa dữ liệu , lập trình web/mobile , điện toán đám mây và trí tuệ nhân tạo) . Nắm chắc các nguyên lí
        và kĩ thuật trên với các công việc cần thực hiện là : thu thập , lưu trữ , truy vấn , xử lí ,phân tích và hiện thị dữ liệu có thuộc tính không gian

        -> Sự khác biệt giữa Địa tin học truyền thống và kỹ sư CNTT địa học:
            + Địa tin học truyền thống : Tập trung vào kỹ năng vẽ bản đồ thủ công và vận hành các phần mềm thương mại đóng gói sẵn

            + Kỹ sư CNTT địa học :
                - Coi địa lý là một kiểu dữ liệu nâng cao tích hợp sâu trong các hệ thống phần mềm
                - Xây dựng các Spatial API / RESTful services nhằm hỗ trợ truy vấn không gian trực tiếp từ máy chủ
                - Lập trình xử lý các tập dữ liệu cực lớn trên hệ tầng điện toán đám mây
                - Ứng dụng trí tuệ nhân tạo vào việc tự động hóa việc dự báo , nhận diện và phân loại đối tượng địa lý từ dữ liệu không gian
                - Xây dựng giao diện hiện thị thông tin bản đồ trực quan , tương tác cao và đúng chuẩn kỹ thuật

        -> Nhờ những kĩ năng trên một kỹ sư CNTT địa học có khả năng giải quyết toàn diện bài toán về không gian thông qua 6 năng lực : Quan sát , định vị , dự đoán
        và tương tích dữ liệu . Các ứng dụng thực tế như : hệ thống dự báo thời tiết , thiết lập đường bay tối ưu , tối ưu hóa tuyến đường giao vận và logistics (g
        g map , grab...)

    2. Hệ sinh thái 3S
        - Hệ sinh thái công nghệ không gian được vận hành dựa trên 3 trụ cột (3S) : GIS , RS , và GNSS(GPS) . Nhờ sự phối hợp nhịp nhàng giữa 3 công nghệ này , chúng
        ta có thể tiến hành các công việc là : thu thập , lưu trữ , quản lý , phân tích và biểu diễn các mối quan hệ địa lý và xu thế trong tương lai

        2.1. GIS (geographic information system - Hệ thống thông tin địa lý)

            - Khái niệm : Là hệ thống thông tin chuyên dụng để lưu trữ , quản lý và truy vấn dữ liệu không gian địa lý kèm theo các thuộc tính phi không gian của đối
            tượng
            - Cách hiểu CNTT : Là cơ sở dữ liệu nâng cao lưu trữ các dữ liệu không gian và thực thi các truy vấn không gian phức tạp bằng mã lệnh

        2.2. RS (Remote sensing - Viễn thám)

            - Khái niệm : Là kỹ thuật thu thập thông tin về bề mặt trái đất từ xa thông qua các cảm biến lắp đặt trên vệ tinh hoặc các thiết bị bay không người lái mà
            không cần tiếp xúc trực tiếp với đối tượng địa lý
            - Các hiểu CNTT : Cách mà thu thập dữ liệu thông qua cảm biến thực chất là việc xử lý ảnh số Raster đa băng phổ và phối hợp với các thuật toán thị giác máy
            tính (computer vision) để tự động phân tích và nhận diện đối tượng địa lý

        2.3. GNSS / GPS (Global Navigation Satellite System / Global Positioning System)

            - Khái niệm : Hệ thống định vị vệ tinh toàn cầu có nhiệm vụ cung cấp tọa độ thực địa (kinh độ , vĩ độ , độ cao) chính xác của một đối tượng tại 1 thời điểm
            - Cách hiểu CNTT : Là nguồn cung cấp luồng dữ liệu chuỗi thời gian (Trajectory / IoT sensor data stream) giúp theo dõi chuyển động thời gian thực của thiết
            bị

    -> Cách hiểu của tôi (bổ sung) :
        + GIS : Là hệ thống cơ sở dữ liệu nâng cao giúp lưu trữ dữ liệu không gian sau đó có thể tiến hành truy vấn , phân tích và đưa ra dự đoán dựa trên dữ liệu đó
        -> Bản chất GIS không chỉ là cơ sở dữ liệu , mà còn ở khả năng hiển thị trực quan bằng các lớp bản đồ (layers) đè lên nhau để giải quyết các bài toán thực tế

        + RS : Là kĩ thuật giúp thu thập dữ liệu thông qua vệ tinh bằng cảm biến bằng cách thu thập ảnh rồi dựa trên thuật toán để phân tích đưa ra dữ liệu cụ thể của đối tượng địa lý đó
        -> Remote sensing (RS) : sử dụng trên drone và ngoài thu thập dữ liệu thông qua ảnh mà còn có sóng , hồng ngoại , radar , laser để phân tích địa hình , nhiệt
        độ , chỉ số thực vật...

        + GNSS / GPS : Là hệ thống giúp thu thập dữ liệu tọa độ (kinh độ , vĩ độ , độ cao) của 1 đối tượng tại 1 thời điểm nhất định
        -> GPS là hệ thống của Mỹ còn GNSS là từ chỉ chung cho toàn bộ hệ thống định vị trên toàn cầu

    -> Câu hỏi ôn tập :
        Câu 1 : Hãy phân biệt vai trò công việc giữa một người sử dụng Địa tin học truyền thống và một kỹ sư CNTT địa học hiện đại khi tiếp cận một bài toán bản đồ.
        - Vai trò người sử dụng Địa tin học truyền thống khi tiếp cận một bài toán bản đồ : giải quyết bài toán và sử dụng các phần mềm có sẵn hỗ trợ kết quả đầu ra của bài toán
        - Vai trò kỹ sư CNTT địa học hiện đại khi tiếp cận bài toán : Thu thập dữ liệu đầu vào , phân tích bài toán , sử dụng thuật toán tối ưu cho bài toán , đưa ra kết quả đầu ra

        Câu 2 : Dưới lăng kính của 1 lập trình viên bản chất thực sự của GIS , RS (remote sensing) , GNSS/GPS là gì ?
        - GIS : Là hệ thống cơ sở dữ liệu giúp lưu trữ dữ liệu không gian sau đó dựa trên dữ liệu đó có thể thực hiện truy vấn , phân tích và đưa ra dự đoán
        - RS : Là kỹ thuật giúp thu thập dữ liệu bằng phân tích hình ảnh đã thu thập được qua cảm biến thông qua vệ tinh , drone ... sau đó dựa trên thuật toán để đưa ra dữ liệu của đối tượng địa lý được thu thập
        - GNSS/GPS : Là hệ thống giúp thu thập dữ liệu tọa độ (kinh độ , vĩ độ , độ cao) của 1 đối tượng cụ thể tại 1 thời điểm nhất định

        Câu 3 : Trong bài toán giao hàng thông minh như (grab/grab food) hệ sinh thái 3S phối hợp và hỗ trợ như thế nào trong việc cập nhật vị trí shipper và tối ưu hóa lộ trình di chuyển
        - GNSS / GPS (đầu vào - thu nhập) : Cảm biến GPS trên Điện thoại của shipper phát ra dữ liệu tọa độ [kinh độ , vĩ độ] vị trí của shipper liên tục và dữ liệu đó được gửi về máy chủ
        - GIS (mắt xích xử lý trung tâm) :
            + Map matching (khớp đường) : Tiếp nhận tọa độ GPS (thường bị sai lệch vài mét do nhà cao tầng) và dùng thuật toán khớp vị trí đó đúng vào con đường
            thực tế trên bản đồ số
            + Spatial Query (truy vấn không gian) : Tìm kiếm các tài xế trống trong bán kính 3km xung quanh khu vực nhà hàng (thuật toán nearest neighbor)
            + Routing Algorithm (tối ưu lộ trình) : GIS chạy các thuật toán tìm đường đi ngắn nhất/ nhanh nhất dựa trên dữ liệu giao thông thời gian thực để gợi ý lộ
            trình tối ưu cho tài xế
        - RS - Remote sensing (trực quan hóa thực địa) : Bản đồ nền vệ tinh (sản phẩm của viễn thám) được tích hợp phía dưới ứng dụng giúp khách hàng và shipper nhìn rõ hình ảnh thực địa (nhà cửa , cây cối , đường...) để dễ dàng giao và nhận hàng ở các khu vực ngõ , hẻm phức tạp

Chương 2 : Mô hình và định dạng dữ liệu không gian

    * Dữ liệu là gì ? Thông tin là gì ? -> Dữ liệu không gian là gì ?

    -> Dữ liệu là : các số liệu , ký tự , hình ảnh hoặc sự kiện chưa qua xử lý và chưa có ngữ cảnh . Bản thân dữ liệu chưa mang lại ý nghĩa trực tiếp để đưa ra quyết
    định . vd : 29 , @....

    -> Thông tin là : Dữ liệu đã được xử lý , sắp xếp và đặt vào ngữ cảnh cụ thể để mang lại ý nghĩa cho người dùng . vd : 29 độ C ...

    -> Mô hình DIKW (Data - Information - Knowledge - Wisdom) :
        + Dữ liệu (Data) : dữ liệu thô , rời rạc không mang bất kì ý nghĩa nào đối với người dùng -> vd : 37

        + Thông tin (Information) : Dữ liệu + ngữ cảnh tạo ra 1 thông tin về 1 đối tượng cụ thể , có ý nghĩa đối với người dùng khi tiếp nhận thông tin -> vd : con người có nhiệt độ trung bình 37 độ C

        + Tri thức (Knowledge) : Thông tin + kinh nghiệm của người dùng tạo nên sự hiểu biết của người dùng về 1 đối tượng cụ thể -> vd : Khi con người vượt quá nhiệt độ trung bình là 37 độ C sẽ gây nên sốt

        + Trí tuệ / quyết định (Wisdom) : Từ những tri thức đã có của người dùng từ đó có thể đưa ra những quyết định cụ thể về 1 vấn đề -> vd : Không nên để nhiệt độ vượt quá 37 độ C

    -> Dữ liệu không gian :

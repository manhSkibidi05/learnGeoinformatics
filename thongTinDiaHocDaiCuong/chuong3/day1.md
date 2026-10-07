# Review : 

## Chương 1 : Tổng quan về Công nghệ thông tin địa học 

- Công nghệ thông tin địa học là ngành áp dụng các công nghệ và kỹ thuật nhằm phục vụ con người giúp con người tiếp cận được thông tin về địa lý thông qua các phần mềm , ngoài ra đối với các kỹ sư còn phục vụ nghiên cứu và phân tích dựa trên dữ liệu không gian thu thập được 
-> Bổ sung : Công nghệ thông tin địa học là sự kết hợp 3 ngành chính : Khoa học trái đất ( địa lý , trắc địa) + Khoa học máy tính (CNTT) + Toán học / thống kê -> Mục tiêu cuối cùng là đưa thông tin về địa lý đến người dùng và hỗ trợ đưa ra quyết định không gian 

- 3 công nghệ chủ chốt công nghệ thông tin địa học : 
    + GIS : Là hệ thống quản lý và lưu trữ dữ liệu không gian ngoài ra còn giúp trực quan hóa dữ liệu và phân tích dữ liệu không gian , tạo bản đồ số dựa trên việc xây dựng các lớp bản đồ 

    + GPS/GNSS : GNSS là hệ thống đại diện cho toàn bộ các hệ thống về định vị vệ tinh trên toàn cầu trong đó có GPS . GPS là hệ thống định vị vệ tinh toàn cầu giúp người dùng biết mình đứng vị trí nào trên trái đất 

    + Remote Sensing : Là hệ thống giúp thu thập dữ liệu không gian từ viễn thám thông qua hệ thống chụp ảnh bằng vệ tinh , drone ... từ ảnh đó sẽ phân tích 
    ảnh rồi đưa ra dữ liệu -> Sai 
    -> Sửa : Remote Sensing là khoa học thu thập thông tin về một đối tượng mà không cần tiếp xúc vật lý với nó mà thông qua đo lường bức xạ điện từ (ánh sáng khả kiến , hồng ngoại , vi sóng). Vệ tinh và drone là các thiết bị mang cảm biến có thể máy ảnh , radar , quang phổ kế giúp thu thập dữ liệu 

->BỔ sung Mối quan hệ 3 công nghệ : RS cung cấp cái nhìn trên cao (dữ liệu bề mặt) + GPS cung cấp tọa độ chính xác + GIS tiếp nhận dữ liệu từ đó tích hợp và phân tích 2 nguồn dữ liệu trên để tạo bản đồ và mô hình
-> Một ứng dụng về công nghệ thông tin địa học có thể áp dụng 3 công nghệ cùng lúc hoặc chỉ 1 công nghệ và có thể kết hợp thêm nhiều công nghệ khác 

- Mô hình dữ liệu : Là cách đưa dữ liệu thu thập được vào 1 quy tắc nhất định vào máy tính để nhằm lưu trữ , quản lý và phân tích 
-> 2 Mô hình dữ liệu để lưu trữ dữ liệu không gian là : Mô hình dữ liệu Raster và mô hình dữ liệu vector 
    + Mô hình dữ liệu Raster : Dữ liệu được lưu trữ dưới dạng các ô dữ liệu liên tục bằng nhau và mỗi ô này đề chứa 1 dữ liệu cụ thể 
    -> Sử dụng với các dạng dữ liệu thu thập được thay đổi liên tục và không có ranh giới nhất định 
    -> Bổ sung : Độ phân giải là kích thước ô lưới với ô càng nhỏ độ phân giải càng cao nhưng dung lượng tăng lên , có thể biểu diễn dữ liệu rời rạc nếu ô lưới đủ nhỏ nhưng điểm mạnh vẫn là dữ liệu liên tục

    + Mô hình dữ liệu Vector : Dữ liệu được lưu trữ dưới dạng hình học (điểm , đường , vùng) 
    -> Sử dụng với các dạng dữ liệu thu thập được rời rạc có ranh giới nhất định thường là 1 đối tượng địa lý cụ thể nằm trên bản đồ 
    -> Bổ sung : Điểm mạnh lớn nhất mô hình dữ liệu vector là quan hệ topology -> vector lưu trữ quan hệ giữa các đối tượng giúp phân tích mạng lưới (tìm đường đi ngắn nhất) một cách hiệu quả

- Định dạng dữ liệu không gian : Là cách tổ chức lưu trữ dữ liệu dựa trên 1 mô hình dữ liệu được lưu trữ dưới dạng file cho phép phần mềm dễ dàng đọc
-> Với 2 mô hình dữ liệu cốt lõi nhưng có thể tạo ra rất nhiều định dạng dữ liệu dựa trên nó mỗi định dạng ưu nhược điểm riêng 
    + GeoJSON : Xây dựng dựa trên mô hình vector lưu trữ nhiều đối tượng địa lý dưới dạng văn bản , phù hợp với việc phát triển web 
    + GeoPackage : Lưu trữ nhiều file GeoJSON phù hợp với trực quan hóa dữ liệu không gian -> sai
    -> Sửa : GeoPackage là định dạng dữ liệu dựa trên cơ sở dữ liệu SQLite nó có thể chứa dữ liệu raster và vector cùng lúc , GeoPackage là định dạng nhị phân phù hợp để lưu trữ dữ liệu lớn , phức tạp và ổn định hơn GeoJSON

- Hệ tọa độ : Là cách trái đất biểu diễn dưới dạng số hóa sao cho máy tính có thể hiểu được -> Sai
-> Sửa : Hệ tọa độ là hệ quy chiếu toán học dùng để xác định vị trí của một điểm trên bề mặt trái đất . Nó bao gồm hệ trục tọa độ và các tham số gắn hệ trục đó vào trái đất (mô hình ellipsoid , geoid)
-> 2 hệ tọa độ chính : Hệ tọa độ địa lý và hệ tọa độ phẳng 
    + Hệ tọa độ địa lý : Trái đất biểu diễn dưới dạng 3D , đơn vị là độ (degree)
    -> Sử dụng hệ tọa độ này để giao tiếp giữa các ứng dụng về địa lý khác nhau và thu thập , lưu trữ dữ liệu không gian với hệ tọa độ này
    -> Bổ sung : Điểm mạnh lưu trữ dữ liệu toàn cầu , không tính toán khoảng cách 1 cách chính xác

    + Hệ tọa độ phẳng : Trái đất trải phẳng và biểu diễn dưới dạng 2D , đơn vị là mét (meter)
    -> Sử dụng hệ tọa độ này để tính toán hình học như tính khoảng cách , diện tích ... giúp việc quy hoạch đô thị 

- Mô hình là cách tư duy , định dạng là cách đóng gói ? 


# Chương 3 : Remote Sensing 

## Giai đoạn 1 : Cơ sở vật lý và nguyên lý viễn thám 
- Bản chất vật lý của công nghệ viễn thám , cấu trúc hệ thống thu nhận dữ liệu từ xa và giải mã nguyên lý 'dấu vết phổ' giúp máy tính phân biệt các đối tượng
trên bề mặt trái đất 

1. Khái niệm viễn thám (Remote sensing - RS) 
- Định nghĩa : Kỹ thuật thu nhận các thông tin của đối tượng địa lý hoặc hiện tượng trên trái đất và các hành tinh khác mà không cần tiếp xúc vào chúng 
- Nguyên lý : Việc thu nhận thông tin của đối tượng địa lý mà không cần trực tiếp tiếp xúc vào chúng thực chất là việc thu nhận năng lượng phản xạ quang phổ điện từ hoặc bức xạ nhiệt phát ra từ các đối tượng đó 
    + Năng lượng phản xạ quang phổ điện từ : Là sóng điện từ phản xạ lại từ một đối tượng khi được chiếu sóng điện từ có thể từ mặt trời hoặc từ chính thiết bị viễn thám 
    -> Mỗi đối tượng địa lý khi được chiếu sóng điện từ sẽ hấp thụ một phần và phản xạ lại một phần từ phần phản xạ đó được gọi là 'dấu hiệu quang phổ' nó được coi như là id sóng của đối tượng này 
    -> Công việc viễn thám còn lại là sử dụng cảm biến để thu thập / chụp mã id sóng đó từ đó có thể suy ra đối tượng là gì mà không cần trực tiếp đến nơi

    + Bức xạ nhiệt : Là nhiệt độ phát ra từ một đối tượng địa lý từ đó và được thiết bị viễn thám thu nhận được thông tin đó từ đó xác định được nhiệt độ bề mặt và mức độ tỏa nhiệt của đối tượng 
    -> Khác với thu thập bằng viễn thám phản xạ chỉ thu nhận vào ban ngày thì viễn thám nhiệt thu nhập cả ngày lẫn đêm 24/7

- Thông tin thu nhận được từ viễn thám gồm : Dấu hiệu quang phổ là dải màu sắc đặc trưng -> dựa trên sóng phản xạ lại , nhiệt độ bề mặt , độ ẩm , độ nhám khối sinh thực vật 

2. Bốn thành phần cơ bản của hệ thống viễn thám 
- Hệ thống viễn thám hoàn chỉnh sẽ hoạt động dựa trên 4 thành phần cơ bản liên kết chặt chẽ với nhau bao gồm : 
    1. Nguồn năng lượng 
        - Vai trò : Cung cấp sóng điện từ chiếu đến đối tượng để thu nhận tín hiệu 
        - Phân loại : 
            + Nguồn năng lượng tự nhiên : Chủ yếu mặt trời phát ra sóng điện từ (as nhìn thấy , tia hồng ngoại...) hoặc nhiệt độ đối tượng tự tỏa ra 
            + Nguồn năng lượng nhân tạo : Thiết bị tự phát ra sóng (sóng radar hoặc tia laser) xuống mặt đất 

    2. Đối tượng nghiên cứu 
        - Vai trò : Xác nhận đối tượng cần nghiên cứu như bề mặt trái đất , rừng cây , nguồn nước...
        - Cơ chế : Khi nhận năng lượng từ nguồn phát , mỗi đối tượng sẽ hấp thụ một phần và phản xạ lại một phần đặc trưng riêng biệt nó được gọi là dấu hiệu quang phổ 

    3. Cảm biến và vật mang 
        - Cảm biến : Thiết bị đo đạc và ghi nhận năng lượng sóng điện từ (máy ảnh đa phổ , cảm biến nhiệt...)
        - Vật mang : Phương tiện mang cảm biến lên không gian (vệ tinh , máy bay , trạm mặt đất...)
        -> Khi kết hợp vật mang và cảm biến thì nó được coi là một thiết bị viễn thám 

    4. Hệ thống thu nhận , xử lý và ứng dụng 
        - Truyền dẫn và thu nhận : Tín hiệu truyền từ vệ tinh xuống trạm thu mặt đất dưới dạng dữ liệu thô
        - Xử lý và giải mã : Chuyên gia phần mềm GIS / viễn thám thực hiện hiệu chỉnh khí quyển , giải mã sóng thành các thông tin thực tế (tọa độ , chỉ số NDVI , nhiệt độ bề mặt...)
        - Ứng dụng : Xuất bản đồ , giúp đưa ra lựa chọn không gian ... 

3. Phân loại công nghệ viễn thám 
- Công nghệ viễn thám được phân loại dựa trên nguồn cung cấp năng lượng sóng điện từ từ đó thu nhận được thông tin khác nhau về đối tượng 

    1. Viễn thám bị động 
    - Cảm biến không tự phát ra năng lượng mà cảm biến đóng vai trò hoàn toàn máy thu ghi nhận năng lượng phản xạ lại từ mặt trời chiếu tới đối tượng 

    - Nguyên lý hoạt động : 
    Mặt trời - chiếu sáng - > Bề mặt trái đất - bật ngược - > cảm biến thu thập năng lượng bật ngược lại đó 

    - Đặc điểm : 
        + phụ thuộc năng lượng tự nhiên 
        + chỉ thu dải sóng phản xạ (RGB , NIR) và vào ban ngày khi có as mặt trời
        + bị cản trở mạnh bới điều kiện thời tiết (mây , khói , sương mù , mưa)
    
    - Công nghệ và thiết bị điển hình : 
        + camera quang học đa phổ , cảm biến nhiệt lượng
        + vệ tinh đại diện : landsat , sentinel-2...
    
    -> Viễn thám bị động cho chúng ta biết đối tượng này là cái gì và trạng thái sinh hóa / nhiệt độ ra sao (màu gì , cây yếu hay khỏe , nóng hay lạnh)

    2. Viễn thám chủ động 
    - Cảm biến tích hợp nguồn phát sóng điện từ riêng , chủ động bắn ra các chùm sóng / tia năng lượng xuống bề mặt trái đất và đo đạc tín hiệu phản hồi ngược trở lại 

    - Nguyên lý hoạt động : 
    Cảm biến phát sóng - bắn nl xuống - > đối tượng địa lý - phản hổi nl - > cảm biến đo đạc

    - Đặc điểm : 
        + chủ động 100% về nguồn phát và không phụ thuộc vào thời gian có thể hoạt động cả ngày và đêm
        + sử dụng dải sóng xuên thấu mây , mưa... không bị cản trở bởi thời tiết
        + đo được chính xác độ cao 3D , cấu trúc bề mặt và độ nhám

    - Công nghệ & Thiết bị điển hình:
        + Radar / SAR (Synthetic Aperture Radar): Phát sóng vi ba thu tín hiệu tán xạ ngược.
        + LiDAR (Light Detection and Ranging): Phát các xung tia Laser để đo khoảng cách và tạo đám mây điểm 3D.
        + Vệ tinh đại diện: Sentinel-1 (SAR), TerraSAR-X, RADARSAT, ICESat (LiDAR).

    -> Viễn thám chủ động cho chúng ta biết hình thể cơ học và cấu trúc 3D của đối tượng (cao bao nhiêu , gồ gề thế nào , chứa bn nước bên trong)

4. 


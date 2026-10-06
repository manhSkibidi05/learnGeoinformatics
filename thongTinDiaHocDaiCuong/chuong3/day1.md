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

- Mô hình là cách tư duy , định dạng là cách đóng gói 
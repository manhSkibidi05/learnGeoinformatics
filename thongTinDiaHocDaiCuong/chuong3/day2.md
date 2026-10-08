# Review 

## Chương 1 : Tổng quan về CNTT địa học 

- Công nghệ thông tin địa học là sự kết hợp của 3 ngành chính Khoa học máy tính (cntt) + Khoa học trái đất (trắc địa , địa lý) + toán học / thống kê mục đích là đưa thông tin về địa lý đến người dùng và hỗ trợ đưa ra quyết định về không gian 

- Hệ sinh thái 3S : 
    + GIS : Hệ thống quản lý , lưu trữ và phân tích dữ liệu không gian và trực quan hóa dữ liệu không gian để tạo bản đồ số ...
    + GNSS/GPS : GNSS là hệ thống đại diện cho tất cả hệ thống định vị vệ tinh trên toàn thế giới trong đó có GPS . GPS là hệ thống định vị về tinh toàn cầu giúp xác định vị trí của bất cứ đối tượng địa lý nào ở bất cứ đâu và bất kể mọi thời điểm , ngoài ra còn giúp phát triển hệ thống tìm đường , đo vận tốc..
    + Remote Sensing (RS) : Viễn thám là kỹ thuật sử dụng để thu thập thông tin của đối tượng hay hiện tượng của trái đất , hành tinh mà không cần tiếp xúc trực tiếp với chúng 

-> Mối quan hệ giữa 3 công nghệ trên : GPS giúp xác định vị trí của đối tượng , RS cung cấp thông tin đối tượng là gì trạng thái như thế nào , GIS lưu trữ cả 2 thông tin đó lại rồi tiến hành trực quan hóa dữ liệu lên bản đồ số 

- Mô hình dữ liệu là cách tư duy con người về 1 đối tượng địa lý trong tự nhiên : Với chung 1 đối tượng có người tư duy là đối tượng này rời rạc có ranh rới rõ ràng nó gọi là mô hình vector , có người tư duy là đối tượng này liên tục nó gọi là mô hình raster 
-> Vậy việc lựa chọn mô hình nào là phù hợp thì cần dựa vào mục đích nghiện cứu , tỷ lệ bản đồ , nguồn dữ liệu và yêu cầu cụ thể từ đó xác định loại mô hình phù hợp hơn

- Định dạng dữ liệu cách biến các mô hình thành quy tắc tạo file để lưu trữ đối tượng đó sao cho máy tính có thể đọc và hiểu được và giao tiếp giữa các phần mềm với nhau 
-> Một mô hình dữ liệu có thể có nhiều định dạng khác nhau mỗi định dạng phù hợp với ứng dụng khác nhau 

- Hệ tọa độ : Là đưa trái đất vào một hệ quy chiếu toán học từ đó xác định vị trí cụ thế của một đối tượng trên trái đất 
+ Hệ tọa độ địa lý : Trái đất biểu diễn dưới dạng 3D , đơn vị đo độ (degree)
-> Sử dụng để lưu trữ dữ liệu không gian toàn cầu , giao tiếp giữa các ứng dụng GIS

+ Hệ tọa độ phẳng : Trái đất được trải phẳng và biểu diễn dưới dạng 2D , đơn vị đo mét (meter)
-> Sử dụng để tính toán toán học các đối tượng với nhau , khoảng cách , diện tích ...

## Chương 3 : Remote Sensing 

- Câu 1 : Định nghĩa viễn thám và trình bày 4 thành phần cơ bản cấu tạo nên hệ thống viễn thám hoàn chỉnh 
-> Định nghĩa viễn thám : Viễn thám là kỹ thuật thu thập thông tin về một đối tượng địa lý hoặc hiện tượng của trái đất / hành tinh mà không cần tiếp xúc trực tiếp với nó 
-> Hệ thống viễn thám được cấu tạo dựa trên 4 thành phần cơ bản sau : 
    + Nguồn năng lượng : Năng lượng cung cấp đến các đối tượng địa lý trên bề mặt trái đất hầu hết từ ánh sáng mặt trời (sóng điện từ) , từ cảm biến phát ra tia năng lượng 
    + Khí quyển : Do bề dày khí quyển (2000km) làm tán xạ và hấp thụ một phần năng lượng điện từ trưới khi tới cảm biến
    + Đối tượng : Nguồn năng lượng chiếu vào đối tượng thì đối tượng hấp thụ 1 phần và phản xạ lại 1 phần và phần phản xạ lại đó được gọi là 'dấu hiệu quang phổ ' 
    + Cảm biến và vật mang : Cảm biến là thiết bị giúp thu thập các sóng được phản xạ là từ đối tượng cụ thể , vật mang là thiết bị mang cảm biến đến vị trí cần thu thập thông tin 
     

- Câu 2 : Phân biệt sự khác nhau về cơ chế hoạt động , ưu/nhược điểm giữa viễn thám bị động và viễn thám chủ động . Cho ví dụ về hệ thống vệ tinh / công nghệ mỗi loại 
-> Cơ chế hoạt động : 
    - Viễn thám bị động : Thu nhận sóng phản xạ lại của đối tượng nhận từ sóng phát ra từ ánh sáng mặt trời hoặc thu nhận nhiệt lượng phát ra từ đối tượng đó
    - Viễn thám chủ động : Tự phát ra sóng đến đối tượng rồi thu nhận sóng phản xạ lại 
-> Ưu điểm :
    - Viễn thám bị động : Có nhiều hệ thống vệ tinh lớn  
    - Viễn thám chủ động : Có thể thu nhận thông tin 24/7 không kể ngày đêm , không quan tâm đến thời tiết 
-> Nhược điểm : 
    - Viễn thám bị động : Chỉ thu nhận được vào ban ngày và có bị ảnh hưởng bởi thời tiết (mưa , sương mù ...)
    - Viễn thám chủ động : Chi phí chế tạo đắt đỏ , xử lý dữ liệu phức tạp do ảnh radar thường bị hiện tượng nhiễu đốm cần các thuật toán xử lý phức tạp hơn ảnh quang học thông thường  
-> vd : 
    - Viễn thám bị động : Landsat , sentinel-2
    - Viễn thám chủ động : sentinel-1

- Câu 3 : Khái niệm phản xạ quang phổ ? giải thích tại sao thảm thực vật xanh tươi phản xạ mạnh ở dải cận hồng ngoại nhưng phản xạ rất kém ở dải màu đỏ ? 
-> Phản xạ quang phổ là Khi sóng điện từ chiếu tới đối tượng tự nhiện lúc này đối tượng tự nhiên hập thụ một phần sóng đó và phản xạ lại một phần và phần phản xạ đó sẽ được coi là dấu hiệu quang phổ do mỗi đối tượng mức phản xạ khác nhau . 
-> Ở cây xanh phản xạ mạnh ở dải cận hồng ngoại là do cấu trúc cây biểu hiện cây còn khỏe hay yếu , phản xạ kém dải màu đỏ do hập thu hết màu đỏ rồi 

# Chương 3 : Remote Sensing 

## Giai đoạn 1 : Tổng quan về remote sensing 

4. Nguyên lý phản xạ quang phổ 
- Nguyên lý phản xạ quang phổ : Khả năng phản xạ của 1 đối tượng phụ thuộc vào bước sóng chiếu tới , độ phản xạ đưới tính bằng tỉ lệ phần trăm giữa năng lượng phản xạ và năng lượng chiếu tới tại từng dải sóng cụ thể 

- Dấu hiệu quang phổ : Khi biểu diễn độ phản xạ theo từng bước sóng trên 1 hệ trục tọa dộ ta thu được đường cong đặc trưng gọi là đường cong phản xạ quang phổ hay dấu hiệu quang phổ
-> Mỗi đối tượng tự nhiên có cấu trúc hóa lý khác nhau nên tạo ra đường cong khác nhau tạo nên sự riêng biệt giữa các đối tượng

- Dấu hiệu quang phổ của 3 đối tượng cơ bản : 
    + Thực vật xanh : 
        - Ánh sáng nhìn thấy : Diệp lục hấp thụ mạnh màu đỏ và xanh dương , chỉ phản xạ nhẹ ở dải xanh lá -> mắt người thấy lá màu xanh
        - Hồng ngoại gần (NIR) : Cấu trúc tế bào lá phản xạ cực kỳ mạnh -> Giúp nhận diện sức khỏe cây trồng 
        - Hồng ngoại sóng ngắn (SWIR) : Độ phản xạ giảm xuống ở bước sóng 1.4 - 1.9 do nước trong lá cây hấp thụ 

    + Đất khô : 
        - Đường cong phản xạ của đối tượng đất tương đối đơn điệu  và tăng dần từ dải nhìn thấy đến dải hồng ngoại
        - Yếu tố ảnh hưởng : Đất càng ẩm hoặc chứa nhiều chất hữu cơ thì độ phản xạ càng giảm , với đất khô / cát mịn phản xạ mạnh hơn

    + Nước sạch : 
        - Nước độ phản xạ tổng thể rất thấp < 10%
        - Phản xạ lượng nhỏ ở dải nhìn thấy xanh dương / xanh lá , nhưng hấp thụ gần như toàn bộ năng lượng ở dải hồng ngoại 
        - Vì vậy ảnh hồng ngoại các dòng sông / hồ luôn hiện thị bằng màu đen hoặc xanh đen thẫm 

- Ứng dụng trong kỹ thuật và CNTT địa học : 
    1. Phát triển các chỉ số không gian : NDVI (chỉ số thực vật) , NDWI 
    2. Phân loại ảnh vệ tinh tự động 

## Giai đoạn 2 : Độ phân giải ảnh và hệ thống vệ tinh landsat 8/9 
- Các thông số kỹ thuật quyết định chất lượng ảnh viễn thám , tìm hiểu cấu trúc dải phổ của hệ thống vệ tinh landsat 8/9 và cách ghép các dải phổ thành tổ hợp màu phục vụ từng mục đích phân tích địa lý cụ thể 

1. Độ phân giải của ảnh viễn thám 
- Hệ thống viễn thám sẽ trả lại ảnh viễn thám sau khi thu nhận thông tin và ảnh viễn thám thu được đó sẽ sở hữu 4 độ phân giải ảnh cố định do phần cứng của vệ tinh đó quyết định , 4 độ phân giải ảnh này sẽ quyết định đến việc lựa chọn ảnh có loại độ phân giải nào cao nhất / thấp nhất sao cho phù hợp với mục đích bài toán 
- vd : Bài toán quản lí địa chính và đô thị cần thấy rõ từng căn nhà , con đường -> độ phân giải ưu tiên không gian siêu cao , ảnh lựa chọn : worldWiew 

- 4 độ phân giải của ảnh viễn thám thu được sẽ quyết định chất lượng ảnh và khả năng ứng dụng ảnh đó : 
    1. Độ phân giải không gian 
        - Khái niệm : Độ phân giải không gian là thước quy định tỷ lệ 1 pixel (điểm ảnh) có kích thước bao nhiêu tương ứng với 1 vị trí trên bề mặt trái đất 
        -> Một ảnh có GSD là 10 m thì mỗi pixel đại điện cho 1 vị trí trên mặt đất có kích thước 100m vuông 
        -> Giá trị GSD càng nhỏ thì lúc này độ phân giải không gian càng cao , bức ảnh càng sắc nét và cho phép phân biệt các vật thể nhỏ hơn 

    2. Độ phân giải quang phổ 
        - Khái niệm : Độ phân giải quang phổ là hộp bút màu quy định số màu trong 1 pixel (điểm ảnh)
        -> Độ phân giải quang phổ càng cao 1 pixel sẽ không chỉ chứa 1 màu cơ bản mà chứa hàng chục / trăm màu trồng lên nhau bên trong 1 điểm ảnh 
        -> Khi độ phân giải quang phổ cao thì chứa nhiều ảnh bên trong 1 pixel từ đó có thể dễ dàng xác định đối tượng là gì thông qua màu sắc 

    3. Độ phân giải bức xạ
        - Khái niệm : Độ phân giải bức xạ là khả năng phân biệt sáng - tối (đậm - nhạt) của 1 màu sắc trong điểm ảnh 
        -> Độ phân giải quang phổ cho biết một điểm ảnh chứa bao nhiêu màu thì độ phân giải bức xạ cho biết mỗi màu đó có bao nhiêu sắc độ (từ cực sáng đến cực tối)
        -> Độ phân giải bức xạ càng lớn thì giúp nhìn rõ các chi tiết ẩn trong vùng quá tối hoặc vùng quá sáng 

    4. Độ phân giải thời gian 
        - Khái niệm : Độ phân giải thời gian là tần suất hay khoảng thời gian cố định mà vệ tinh quay trở lại vị trí chỉ định lần thứ 2 
        -> Độ phân giải thời gian cao thì khoảng thời gian cần đợi càng giảm vì vệ tinh quay lại vị trí cũ nhanh hơn 
        -> Độ phân giải thời gian giúp theo dõi tham họa / nông nghiệp cách liên tục giúp xử lý tình huống cách nhanh chóng 

2. Vệ tinh Landsat 8/9 và cấu trúc dải phổ 
- Hệ thống vệ tinh Landsat do NASA và USGS (mỹ) vận hành là nguồn cung cấp dữ liệu ảnh vệ tinh tài nguyên với độ phân giải trung bình được cung cấp miễn phí phổ biến nhất trên thế giới .
    + Landsat 8 phóng 2013 Landsat 9 phóng 2021 là phiên bản cải tiến song sinh của Landsat 8 , giữ nguyên cấu trúc kênh sóng để đảm bảo tính liên tục của chuỗi dữ liệu không gian 
    + 2 vệ tinh đều mang 2 cảm biến chính : 
        - OLI / OLI-2 : Cảm biến quang học đa phổ (bands 1 - 9)
        - TIRS / TIRS-2 : Cảm biến hồng ngoại nhiệt (bands 10 - 11)
    + Chu kì chụp lặp : 16 ngày 

- Cấu trúc dải phổ là : Tập hợp các dải sóng điện từ (ánh sáng nhìn thấy , hồng ngoại) mà vệ tinh chụp lại

3. Kỹ thuật tổ hợp dải màu 
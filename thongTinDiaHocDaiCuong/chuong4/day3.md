# Chương 4 : Cơ sở dữ liệu - PostgreSQL , PostGIS 

## Giai đoạn 2 : Lập trình truy vấn thuộc tính SQL & SPATIAL 

- Giai đoạn 2 bạn sẽ thực hành viết các câu truy vấn SQL thuộc tính , các phép toán thống kê và liên kết bảng (JOIN) dựa trên 12 btth

- 3 Bảng dữ liệu thêm vào gồm : states , cities , census2020 
    + Bảng census2020 : Chứa dữ liệu dân số nước mỹ năm 2020 theo từng bang -> Bảng dữ liệu thuộc tính
    -> Các cột gồm : state -> tên bang , total -> tổng dân số , male/female -> Dân số nam/nữ , white/black... -> Dân số theo chủng tộc 

    + Bảng states : Chứa dữ liệu ranh giới các bang dưới dạng Polygon 
    -> Các cột gồm : gid -> mã định danh , name -> tên bang , rank -> thứ hạng dân số , sub_region -> phân vùng nhóm theo nước ngọt  , pop2018 -> dân số 2018 

    + Bảng cities : Chứa dữ liệu các thành phố dưới dạng Point 
    -> Các cột gồm : gid -> mã định danh , name -> tên thành phố , stateabb -> mã bang dạng US-AK...

- Mối liên kết giữa 3 bảng là : 
    + Bảng states và census2020 : Nối với nhau bằng tên bang states.name = census2020.state -> gắn dữ liệu dân số 2020 vào ranh giới bang 

    + Bảng states và cities : Liên kết không gian với nhau ST_Within(cities.geom , states.geom) -> xác định xem thành phố nằm trong ranh giới bang không 

    + Bảng census2020 và cities : Liên kết gián tiếp thông qua states , cities -> states bằng không gian -> census2020 bằng tên bang 


### 1. Nhóm bài tập truy vấn lọc và sắp xếp dữ liệu 

1. Câu 1 : Lọc danh sách các bang thuộc khu vực gọi nước ngọt là 'Soda' 

    SELECT name , sub_region FROM usa.states WHERE sub_region = 'Soda';

2. Câu 2 : Lọc danh sách các bang thuộc khu vực gọi nước ngọt là 'Soda' và có tổng số dân năm 2020 > 10tr người 

    SELECT s.name, s.sub_region, c.total FROM usa.states s JOIN usa.census2020 c ON s.name = c.state 
    WHERE s.sub_region = 'Soda' AND c.total > 10000000;


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

-> Bài tập thực hành 

1. Câu 1 : Chọn các bang có dân số năm 2018 trên 10 triệu người 

    select name , pop2018 from usa.states where pop2018 > 10000000

2. Câu 2 : Chọn các thủ phủ của bang (state capitals)

    select name , capital from usa.cities where capital = 1

3. Câu 3 : Chọn các bang có tên bắt đầu bằng từ "New"

    select name from usa.states where name ilike 'NEW%'

4. Câu 4 : Chọn các thành phố có tên chứa chữ cái 'z' 

    select name from usa.states where name ilike '%z%'

5. Câu 5 : Sắp xếp danh sách các bang theo dân số năm 2018 từ cao xuống thấp.

    select name , pop2018 from usa.states order by pop2018 DESC

6. Câu 6 : Sắp xếp danh sách các bang trước tiên theo tên gọi nước giải khát, sau đó theo tên bang

    select name , sub_region from usa.states order by  sub_region, name

7. Câu 7 : Chọn các bang có dân số năm 2018 trên 10 triệu người và có đa số dân số gọi nước giải khát là "pop"

    select name , sub_region , pop2018 from usa.states where pop2018 > 10000000 and sub_region = 'Pop'

8. Câu 8 : Chọn các thành phố thuộc các bang NY, NJ, và PA (sử dụng cột stateabb).

    select name , country , stateabb from usa.cities where stateabb in ('US-NY', 'US-NJ', 'US-PA')

9. Câu 9 : Đối với mỗi bang, hãy tính tỷ lệ phần trăm dân số da trắng năm 2020. Đặt tên giả (alias) cho cột kết quả này là pctwhite. Ngoài cột pctwhite, đầu ra chỉ bao gồm duy nhất tên của bang.

    SELECT state, white::double precision / total * 100 AS pctwhite
    FROM usa.census2020;

10. Câu 10 : Tính tổng dân số năm 2018 của các bang theo từng danh mục Soda (tức là: Tổng dân số của các bang dùng từ 'soda' là bao nhiêu? Của các bang dùng 'pop'? Của các bang dùng 'coke'?)

    select SUM(pop2018) as total , sub_region  from usa.states 
    group by sub_region 

11. Câu 11 : Kết hợp dữ liệu từ hai bảng states và census2020, xuất ra cột tên bang (name) từ bảng states, tổng dân số (total) từ bảng census2020, và cột không gian (geom) từ bảng states.

    select s.name , c.total , s.geom from usa.states s join usa.census2020 c on s.name = c.state

12. Câu 12 : Tính dân số nam trung bình năm 2020 theo từng danh mục Soda

    select s.sub_region , AVG(c.male) as avg_male from usa.states s join usa.census2020 c on s.name = c.state 
    group by s.sub_region
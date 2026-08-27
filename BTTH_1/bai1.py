import geopandas as gpd
import folium
import json
from shapely.geometry import Point

# ==============================================================================
# BƯỚC 1 : Khởi tạo dữ liệu mẫu 
# ==============================================================================

data_geojson = {
    "type" : "FeatureCollection",
    "features" : [
        {
            "type" : "Feature",
            "properties" : {
                "name" : "Bảo tàng Lịch sử Quốc gia" , "category" : "Museum" , "rating" : 4.6
            },
            "geometry" : {
                "type" : "Point",
                "coordinates" : [105.8595, 21.0252]
            }
        },
        {
            "type" : "Feature",
            "properties" : {
                "name" : "Bảo tàng Mỹ thuật Việt Nam" , "category" : "Museum" , "rating" : 4.7
            },
            "geometry" : {
                "type" : "Point",
                "coordinates" : [105.8347, 21.0310]
            }
        },
        {
            "type" : "Feature",
            "properties" : {
                "name" : "Bảo tàng Lịch sử Quân sự Việt Nam" , "category" : "Museum" , "rating" : 4.5
            },
            "geometry" : {
                "type" : "Point",
                "coordinates" : [105.7557 , 21.0086]
            }
        },
        {
            "type" : "Feature",
            "properties" : {
                "name" : "Bảo tàng Dân tộc học Việt Nam" , "category" : "Museum" , "rating" : 4.6
            },
            "geometry" : {
                "type" : "Point",
                "coordinates" : [105.7987 , 21.0405]
            }
        },
        {
            "type" : "Feature",
            "properties" : {
                "name" : "Hồ Hoàn Kiếm" , "category" : "Nature" , "rating" : 4.9
            },
            "geometry" : {
                "type" : "Point",
                "coordinates" : [105.8524, 21.0287]
            }
        }
    ]
}

# Ghi ra file tạm minh họa việc đọc file
with open("poi_hanoi.geojson", "w", encoding="utf-8") as f:
    json.dump(data_geojson, f, ensure_ascii=False, indent=2)

# ==============================================================================
# BƯỚC 2: Đọc vào GEODATAFRAME -> đọc file geojson dạng từ điển lồng nhau thành dạng bảng 2 chiều (hàng và cột)
# ==============================================================================

gdf_poi = gpd.read_file("poi_hanoi.geojson")
print("Dữ liệu gốc ban đầu : ")
print(gdf_poi[['name', 'category', 'rating', 'geometry']])
print(f"\n Hệ tọa độ ban đầu: {gdf_poi.crs}")

# ==============================================================================
# BƯỚC 3 : Lọc dữ liệu thuộc tính 
# ==============================================================================

filtered_museums = gdf_poi[
    (gdf_poi['category'] == 'Museum') & 
    (gdf_poi['rating'] >= 4.6)
].copy()

print("Dữ liệu sau khi lọc : ")
print(filtered_museums[['name' , 'rating' , 'geometry']])

# ==============================================================================
# BƯỚC 4 : Xuất kết quả ra file GeoJSON mới  
# ==============================================================================

output_filename = "filtered_museums.geojson"
filtered_museums.to_file(output_filename, driver="GeoJSON")
print(f"\n Đã xuất file thành công: {output_filename}")

# ==============================================================================
# BƯỚC 5 : Trực quan hóa bản đồ tương tác  
# ==============================================================================

# Folium nhận thứ tự [Lat, Lon]
center_lat, center_lon = 21.0285, 105.8542
m = folium.Map(location=[center_lat, center_lon], zoom_start=14, tiles="CartoDB positron")

# Thêm các Marker vào bản đồ
for idx, row in filtered_museums.iterrows():
    lon = row.geometry.x
    lat = row.geometry.y

    popup_content = f"""
    <b>{row['name']}</b><br>
    Thể loại: {row['category']}<br>
    Đánh giá: ⭐ {row['rating']}
    """

    folium.Marker(
        location=[lat, lon],
        popup=folium.Popup(popup_content, max_width=300),
        tooltip=row['name'],
        icon=folium.Icon(color="red", icon="museum", prefix="fa")
    ).add_to(m)

# Lưu bản đồ ra file HTML
m.save("museums_map.html")
print("Bản đồ tương tác đã được tạo: museums_map.html ")

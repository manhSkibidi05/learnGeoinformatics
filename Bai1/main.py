import geopandas as gpd
import folium

# ==============================================================================
# BƯỚC 1 & 2: ĐỌC DỮ LIỆU TỪ FILE GeoJSON RIÊNG VÀO GEODATAFRAME
# ==============================================================================
input_file = "data.geojson"

try:
    # Đọc dữ liệu từ file GeoJSON đã tạo sẵn
    gdf = gpd.read_file(input_file)
    print(f"-> Đã đọc dữ liệu thành công từ file '{input_file}'! Tổng số bản ghi: {len(gdf)}")
    print(gdf[['name', 'type', 'rating']])
except FileNotFoundError:
    print(f"Lỗi: Không tìm thấy file '{input_file}'. Hãy đảm bảo file này nằm cùng thư mục với main.py!")
    sys.exit()

# ==============================================================================
# BƯỚC 3: LỌC DỮ LIỆU THUỘC TÍNH
# Điều kiện: type == 'Museum' và rating >= 4.6
# ==============================================================================
filtered_gdf = gdf[(gdf['type'] == 'Museum') & (gdf['rating'] >= 4.6)]

print(f"\n-> Kết quả lọc (Bảo tàng có Rating >= 4.6) - Tìm thấy {len(filtered_gdf)} địa điểm:")
print(filtered_gdf[['name', 'type', 'rating']])

# ==============================================================================
# BƯỚC 4: XUẤT DỮ LIỆU ĐÃ LỌC RA FILE GEOJSON MỚI
# ==============================================================================
output_file = "hanoi_museums_top.geojson"
filtered_gdf.to_file(output_file, driver="GeoJSON", encoding="utf-8")

print(f"\n-> Đã xuất dữ liệu sau khi lọc ra file mới: '{output_file}'")

# ==============================================================================
# BƯỚC 5: TRỰC QUAN HÓA BẢN ĐỒ TƯƠNG TÁC BẰNG FOLIUM
# ==============================================================================
# Khởi tạo bản đồ Folium với tâm tại Hà Nội
map_center = [21.0285, 105.8542]

# Dùng Nền CartoDB để tránh bị chặn IP
m = folium.Map(
    location=map_center, 
    zoom_start=12,
    tiles="https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png",
    attr='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors &copy; <a href="https://carto.com/attributions">CARTO</a>'
)

if len(filtered_gdf) > 0:
    for _, row in filtered_gdf.iterrows():
        lat = row.geometry.y
        lon = row.geometry.x
        name = row['name']
        rating = row['rating']
        
        popup_text = f"<b>{name}</b><br>Loại: Bảo tàng<br>Đánh giá: ⭐ {rating}"
        
        folium.Marker(
            location=[lat, lon],
            popup=folium.Popup(popup_text, max_width=300),
            tooltip=name,
            icon=folium.Icon(color="red", icon="info-sign")
        ).add_to(m)
else:
    print("Không có điểm nào để hiển thị lên bản đồ.")

# Lưu file
map_html = "ban_do_bao_tang_ha_noi.html"
m.save(map_html)
print(f"-> Đã xuất file {map_html}. Mở bằng Google Chrome để xem!")
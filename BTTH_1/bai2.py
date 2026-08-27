import geopandas as gpd
from shapely.geometry import Point , LineString
import folium

# ==============================================================================
# BƯỚC 1 : Khởi tạo tọa độ vị trí người dùng 
# ==============================================================================

user_lat = 21.02953181897225
user_lon = 105.73842197499965

# Tạo GeoDataFrame cho Người dùng (CRS = WGS84: EPSG:4326)
gdf_user = gpd.GeoDataFrame(
    [{'id': 'USER_01', 'name': 'Vị trí của tôi', 'geometry': Point(user_lon, user_lat)}],
    crs="EPSG:4326"
)

# ==============================================================================
# BƯỚC 2 : Danh sách các trạm xe buýt lân cận  
# ==============================================================================

bus_stop_data = [
    {'stop_id' : 'BUS_01' , 'name' : 'Điểm dừng 320 Xuân Phương' , 'geometry' : Point( 105.7390580068872 , 21.032345379811762)},
    {'stop_id' : 'BUS_02' , 'name' : 'Điểm dừng Chùa Ngọc Mạch' , 'geometry' : Point( 105.73976171040881 , 21.030930680995997)},
    {'stop_id' : 'BUS_03' , 'name' : 'Điểm dừng KĐT Vân Canh' , 'geometry' : Point( 105.73891365751226 , 21.028286505537952)},
    {'stop_id' : 'BUS_04' , 'name' : 'Điểm dừng sân bóng Vân Canh' , 'geometry' : Point( 105.73931061847316 , 21.028168611272008)},
    {'stop_id' : 'BUS_05' , 'name' : 'Điểm dừng đối diện bưu điện Vân Canh' , 'geometry' : Point( 105.73810211296919 , 21.036073356742357)},
]

gdf_bus_stops = gpd.GeoDataFrame(bus_stop_data , crs="EPSG:4326")

# ==============================================================================
# BƯỚC 3: CHUYỂN ĐỔI HỆ TỌA ĐỘ SANG HỆ CHIẾU PHẲNG ĐƠN VỊ MÉT (PROJECTED CRS)
# Khu vực miền Bắc Việt Nam sử dụng lưới chiếu UTM Zone 48N -> EPSG:32648 
# ==============================================================================

UTM_VN_CRS = "EPSG:32648" 

gdf_user_proj = gdf_user.to_crs(UTM_VN_CRS)
gdf_bus_stops_proj = gdf_bus_stops.to_crs(UTM_VN_CRS)

user_geom_proj = gdf_user_proj.geometry.iloc[0]

# ==============================================================================
# BƯỚC 4: TÍNH KHOẢNG CÁCH CHÍNH XÁC (ĐƠN VỊ: MÉT)  
# ==============================================================================

gdf_bus_stops_proj['distance_meters'] = gdf_bus_stops_proj.geometry.distance(user_geom_proj)

# ==============================================================================
# BƯỚC 5: TÌM TRẠM GẦN NHẤT 
# ==============================================================================

nearest_idx = gdf_bus_stops_proj['distance_meters'].idxmin()
nearest_stop = gdf_bus_stops_proj.loc[nearest_idx]

print("=== BẢNG TÍNH KHOẢNG CÁCH ĐẾN CÁC TRẠM XE BUÝT ===")
for _, row in gdf_bus_stops_proj.sort_values(by='distance_meters').iterrows():
    print(f"👉 Trạm: {row['name']:<35} | Khoảng cách: {row['distance_meters']:.2f} m")

print("\n-----------------------------------------------------------")
print(f"🎯 TRẠM GẦN NHẤT: {nearest_stop['name']}")
print(f"📏 KHOẢNG CÁCH: {nearest_stop['distance_meters']:.2f} mét (~ {nearest_stop['distance_meters']/1000:.2f} km)")
print("-----------------------------------------------------------")

# ==============================================================================
# BƯỚC 6: TRỰC QUAN HÓA BẢN ĐỒ KẾT NỐI (FOLIUM) 
# ==============================================================================

map_routing = folium.Map(location=[user_lat, user_lon], zoom_start=16, tiles="CartoDB positron")

# 1. Đánh dấu vị trí người dùng (Marker xanh dương)
folium.Marker(
    location=[user_lat, user_lon],
    popup="<b>Vị trí của bạn</b>",
    tooltip="Vị trí hiện tại",
    icon=folium.Icon(color="blue", icon="user", prefix="fa")
).add_to(map_routing)

# 2. Đánh dấu tất cả các trạm buýt
for _, row in gdf_bus_stops.iterrows():
    is_nearest = (row['stop_id'] == nearest_stop['stop_id'])
    icon_color = "green" if is_nearest else "gray"

    stop_lat = row.geometry.y
    stop_lon = row.geometry.x

    # Lấy khoảng cách đã tính
    dist = gdf_bus_stops_proj.loc[gdf_bus_stops_proj['stop_id'] == row['stop_id'], 'distance_meters'].values[0]

    folium.Marker(
        location=[stop_lat, stop_lon],
        popup=f"<b>{row['name']}</b><br>Khoảng cách: {dist:.1f} m",
        tooltip=row['name'],
        icon=folium.Icon(color=icon_color, icon="bus", prefix="fa")
    ).add_to(map_routing)

# 3. Vẽ đường chim bay (LineString) nối người dùng tới trạm gần nhất
nearest_orig = gdf_bus_stops.loc[gdf_bus_stops['stop_id'] == nearest_stop['stop_id']].iloc[0]
line_coords = [
    [user_lat, user_lon],
    [nearest_orig.geometry.y, nearest_orig.geometry.x]
]

folium.PolyLine(
    locations=line_coords,
    color="red",
    weight=3,
    dash_array="5, 10",
    tooltip=f"Tuyến gần nhất ({nearest_stop['distance_meters']:.1f}m)"
).add_to(map_routing)

# 4. Vẽ vòng bán kính đi bộ 500m (Buffer Visualization)
folium.Circle(
    location=[user_lat, user_lon],
    radius=500,
    color="#3388ff",
    fill=True,
    fill_opacity=0.1,
    tooltip="Bán kính đi bộ 500m"
).add_to(map_routing)

map_routing.save("nearest_bus_stop_map.html")
print("\n[OK] Đã tạo bản đồ đường nối trạm gần nhất: nearest_bus_stop_map.html")

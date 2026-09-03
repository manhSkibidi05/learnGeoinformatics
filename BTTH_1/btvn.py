import geopandas as gpd
import folium
from shapely.geometry import Point

# ==========================================
# BƯỚC 1: KHỞI TẠO DỮ LIỆU ĐIỂM (POI)
# ==========================================
# Vị trí trung tâm: Trường ĐH Mỏ - Địa chất
humg_lat, humg_lon = 21.0722, 105.7741

poi_data = [
    # ==========================================
    # NHÓM 1: BẾN XE BUÝT (Blue - Icon: bus)
    # ==========================================
    {
        "name": "Điểm xe buýt ĐH Mỏ - Địa chất (Phố Viên)", 
        "category": "Bến xe buýt", 
        "icon": "bus", 
        "color": "blue", 
        "geometry": Point(105.7735, 21.0718)
    },
    {
        "name": "Điểm xe buýt Cổng B - ĐH Mỏ Địa chất", 
        "category": "Bến xe buýt", 
        "icon": "bus", 
        "color": "blue", 
        "geometry": Point(105.7750, 21.0732)
    },
    {
        "name": "Điểm xe buýt Học viện Tài chính", 
        "category": "Bến xe buýt", 
        "icon": "bus", 
        "color": "blue", 
        "geometry": Point(105.7785, 21.0736)
    },
    {
        "name": "Điểm dừng xe buýt KTX Học viện Tài chính", 
        "category": "Bến xe buýt", 
        "icon": "bus", 
        "color": "blue", 
        "geometry": Point(105.7770, 21.0708)
    },
    {
        "name": "Điểm dừng Phố Viên (Đường Lê Văn Hiến)", 
        "category": "Bến xe buýt", 
        "icon": "bus", 
        "color": "blue", 
        "geometry": Point(105.7698, 21.0705)
    },

    # ==========================================
    # NHÓM 2: TRƯỜNG ĐẠI HỌC (Orange - Icon: graduation-cap)
    # ==========================================
    {
        "name": "Trường ĐH Mỏ - Địa chất (Cơ sở chính)", 
        "category": "Trường Đại học", 
        "icon": "graduation-cap", 
        "color": "orange", 
        "geometry": Point(humg_lon, humg_lat)
    },
    {
        "name": "Học viện Tài chính (Cơ sở Đức Thắng)", 
        "category": "Trường Đại học", 
        "icon": "graduation-cap", 
        "color": "orange", 
        "geometry": Point(105.7727 , 21.0755)
    },
    

    # ==========================================
    # NHÓM 3: TIỆM THUỐC (Red - Icon: medkit)
    # ==========================================
    {
        "name": "Nhà thuốc Long Châu (Số 88 Phố Viên)", 
        "category": "Tiệm thuốc", 
        "icon": "medkit", 
        "color": "red", 
        "geometry": Point(105.7730, 21.0710)
    },
    {
        "name": "Nhà thuốc Pharmacity Cổ Nhuế 2", 
        "category": "Tiệm thuốc", 
        "icon": "medkit", 
        "color": "red", 
        "geometry": Point(105.7752, 21.0725)
    },
    {
        "name": "Nhà thuốc An Kang (Đường Đức Thắng)", 
        "category": "Tiệm thuốc", 
        "icon": "medkit", 
        "color": "red", 
        "geometry": Point(105.7715, 21.0700)
    },
    {
        "name": "Nhà thuốc Tốt Tâm Đức (Cổng Học viện Tài chính)", 
        "category": "Tiệm thuốc", 
        "icon": "medkit", 
        "color": "red", 
        "geometry": Point(105.7775, 21.0728)
    },
    {
        "name": "Quầy thuốc Học viện (Đường Lê Văn Hiến)", 
        "category": "Tiệm thuốc", 
        "icon": "medkit", 
        "color": "red", 
        "geometry": Point(105.7760, 21.0712)
    }
]

# Tạo GeoDataFrame cho các điểm POI (CRS: EPSG:4326)
gdf_poi = gpd.GeoDataFrame(poi_data, crs="EPSG:4326")

# ==========================================
# BƯỚC 2: TẠO VÙNG ĐỆM BUFFER 500M (GEOPANDAS)
# ==========================================
# Lọc lấy riêng dòng ĐH Mỏ - Địa chất từ gdf_poi có sẵn
gdf_humg = gdf_poi[gdf_poi['name'].str.contains('Trường ĐH Mỏ - Địa chất')].copy()

# Chuyển sang hệ tọa độ phẳng UTM Zone 48N (EPSG:32648) để tính theo Mét
gdf_humg_proj = gdf_humg.to_crs("EPSG:32648")

# Tạo đường tròn Buffer 500m
gdf_buffer_proj = gdf_humg_proj.copy()
gdf_buffer_proj['geometry'] = gdf_humg_proj.geometry.buffer(500)

# Chuyển ngược về WGS84 (EPSG:4326) để vẽ lên Folium
gdf_buffer_4326 = gdf_buffer_proj.to_crs("EPSG:4326")

# ==========================================
# BƯỚC 3: DỰNG BẢN ĐỒ TƯƠNG TÁC (FOLIUM)
# ==========================================
m = folium.Map(location=[humg_lat, humg_lon], zoom_start=16, tiles="OpenStreetMap")

# Tạo các FeatureGroup để phân lớp dữ liệu (cho phép bật/tắt trên bản đồ)
fg_buffer = folium.FeatureGroup(name="⭕ Vùng bán kính 500m")
fg_bus = folium.FeatureGroup(name="🚏 Bến xe buýt")
fg_university = folium.FeatureGroup(name="🎓 Trường Đại học")
fg_pharmacy = folium.FeatureGroup(name="💊 Tiệm thuốc")

# 1. Thêm Vùng Buffer 500m vào FeatureGroup tương ứng
folium.GeoJson(
    gdf_buffer_4326,
    style_function=lambda x: {
        'fillColor': '#3388ff',
        'color': '#0055ff',
        'weight': 2,
        'fillOpacity': 0.15
    },
    tooltip="Bán kính 500m quanh ĐH Mỏ - Địa chất"
).add_to(fg_buffer)

# 2. Phân loại và thêm các điểm POI vào FeatureGroup tương ứng
group_map = {
    "Bến xe buýt": fg_bus,
    "Trường Đại học": fg_university,
    "Tiệm thuốc": fg_pharmacy
}

for idx, row in gdf_poi.iterrows():
    popup_text = f"""
    <div style='font-family: Arial; width: 180px;'>
        <h4 style='margin-bottom: 5px; color: #2c3e50;'>{row['name']}</h4>
        <b>Phân loại:</b> {row['category']}
    </div>
    """
    
    marker = folium.Marker(
        location=[row.geometry.y, row.geometry.x],
        popup=folium.Popup(popup_text, max_width=250),
        tooltip=row['name'],
        icon=folium.Icon(color=row['color'], icon=row['icon'], prefix='fa')
    )
    
    marker.add_to(group_map[row['category']])

# Thêm tất cả các lớp vào bản đồ chính
fg_buffer.add_to(m)
fg_bus.add_to(m)
fg_university.add_to(m)
fg_pharmacy.add_to(m)

# 3. Thêm bảng điều khiển bật/tắt lớp (Layer Control)
folium.LayerControl(collapsed=False).add_to(m)

# ==========================================
# BƯỚC 4: LƯU FILE KẾT QUẢ
# ==========================================

output_file = "PhanVanManh.html"
m.save(output_file)

print(f"✅ Đã tạo thành công file bản đồ: {output_file}")
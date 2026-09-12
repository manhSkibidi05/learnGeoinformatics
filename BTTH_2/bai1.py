# ============================================================
# BÀI TẬP 1: GIẢI MÃ DỮ LIỆU PHẦN CỨNG GPS THÔ (NMEA 0183 PARSING)
# ============================================================

import pandas as pd
import geopandas as gpd
from shapely.geometry import Point
import folium
from pathlib import Path

# 1. Đọc 100 bản ghi NMEA 0183 từ file dữ liệu GPS
input_file = Path(__file__).with_name("12_nmea_100_points.txt")
with input_file.open("r", encoding="utf-8") as file:
    nmea_logs = [line.strip() for line in file if line.strip()]

def nmea_to_decimal(raw_val, direction):
#""" Hàm chuyển đổi tọa độ định dạng DDMM.MMMM / DDDMM.MMMM sang Độ thập phân (Decimal Degrees)"""
    if not raw_val or pd.isna(raw_val):
        return None

    val = float(raw_val)
    degrees = int(val // 100)        # Lấy phần độ (DD hoặc DDD)
    minutes = val % 100              # Lấy phần phút (MM.MMMM)
    decimal = degrees + (minutes / 60.0)

    if direction in ['S', 'W']:
        decimal = -decimal
    return decimal

def parse_gpgga_log(logs):
#"""Giải mã danh sách các dòng văn bản $GPGGA"""
    parsed_data = []
    for line in logs:
        parts = line.split(',')
        if parts[0] == "$GPGGA" and len(parts) >= 10:
            # Bỏ qua các chuỗi không fix được tín hiệu (trường số 6 bằng 0)
            if parts[6] == '0': continue

            time_str = parts[1]
            lat_raw, lat_dir = parts[2], parts[3]
            lon_raw, lon_dir = parts[4], parts[5]
            satellites = parts[7]
            altitude = parts[9]

            lat_dec = nmea_to_decimal(lat_raw, lat_dir)
            lon_dec = nmea_to_decimal(lon_raw, lon_dir)

            if lat_dec is not None and lon_dec is not None:
                parsed_data.append({
                    "time": f"{time_str[:2]}:{time_str[2:4]}:{time_str[4:6]}",
                    "latitude": lat_dec,
                    "longitude": lon_dec,
                    "altitude_m": float(altitude),
                    "satellites": int(satellites),
                    "geometry": Point(lon_dec, lat_dec)
                })
    return parsed_data

# 2. Thực thi giải mã dữ liệu
parsed_list = parse_gpgga_log(nmea_logs)

# 3. Chuyển đổi kết quả sang GeoDataFrame
gdf_gps = gpd.GeoDataFrame(parsed_list, crs="EPSG:4326")

print("=== KẾT QUẢ GIẢI MÃ BÀI 1 ===")
print(gdf_gps[["time", "latitude", "longitude", "altitude_m", "satellites"]])

# 4. Xuất file GeoJSON chuẩn cho hệ thống WebGIS
output_geojson = "gps_parsed.geojson"
gdf_gps.to_file(output_geojson, driver="GeoJSON")
print(f"\n[+] Đã xuất file GeoJSON thành công: {output_geojson}")

# 5. Hiển thị điểm trên bản đồ Folium
if not gdf_gps.empty:
    map_center = [gdf_gps['latitude'].iloc[0], gdf_gps['longitude'].iloc[0]]
    m = folium.Map(location=map_center, zoom_start=16)

    for _, row in gdf_gps.iterrows():
        folium.Marker(
            location=[row['latitude'], row['longitude']],
            popup=f"Time: {row['time']} | Alt: {row['altitude_m']}m",
            icon=folium.Icon(color='blue', icon='info-sign')
        ).add_to(m)

    output_map = "gps_parsed_map.html"
    m.save(output_map)
    print(f"[+] Đã xuất bản đồ thành công: {output_map}")
else:
    print("No valid GPS data to display on the map.")
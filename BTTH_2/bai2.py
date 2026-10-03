"""Phan tich chuoi GPS NMEA va phat hien cac diem dung."""

from pathlib import Path

import folium
import geopandas as gpd
import pandas as pd
from shapely.geometry import Point

INPUT_FILE = Path(__file__).with_name("12_nmea_100_points.txt")
OUTPUT_CSV = Path(__file__).with_name("gps_analysis.csv")
OUTPUT_GEOJSON = Path(__file__).with_name("gps_trajectory.geojson")
OUTPUT_MAP = Path(__file__).with_name("gps_stay_points_map.html")
STAY_DURATION_SECONDS = 1 * 60
STAY_DISTANCE_METERS = 20.0


def nmea_to_decimal(value, direction):
    if not value or direction not in {"N", "S", "E", "W"}:
        return None
    number = float(value)
    decimal = int(number // 100) + (number % 100) / 60
    return -decimal if direction in {"S", "W"} else decimal


def parse_gpgga_file(file_path):
    records = []
    with file_path.open("r", encoding="utf-8") as file:
        for line_number, line in enumerate(file, start=1):
            parts = line.strip().split(",")
            if len(parts) < 10 or parts[0] != "$GPGGA" or parts[6] == "0":
                continue
            latitude = nmea_to_decimal(parts[2], parts[3])
            longitude = nmea_to_decimal(parts[4], parts[5])
            if latitude is None or longitude is None:
                continue
            time_text = parts[1].split(".")[0].zfill(6)
            records.append(
                {
                    "record": line_number,
                    "time": pd.to_datetime(time_text, format="%H%M%S"),
                    "latitude": latitude,
                    "longitude": longitude,
                    "satellites": int(parts[7]),
                    "altitude_m": float(parts[9]),
                    "geometry": Point(longitude, latitude),
                }
            )
    if not records:
        raise ValueError("Khong tim thay cau GPGGA hop le trong file du lieu.")
    return gpd.GeoDataFrame(records, crs="EPSG:4326")


def analyze_trajectory(gps_points):
    points = gps_points.to_crs(epsg=32648).copy()
    points["time_diff_s"] = points["time"].diff().dt.total_seconds().fillna(0)
    points["distance_m"] = points.geometry.distance(points.geometry.shift()).fillna(0)
    points["speed_kmh"] = points.apply(
        lambda row: row["distance_m"] / row["time_diff_s"] * 3.6
        if row["time_diff_s"] > 0
        else 0,
        axis=1,
    )
    points["is_stay"] = False
    stop_groups = []
    start_index = 0

    while start_index < len(points):
        end_index = start_index
        while end_index + 1 < len(points):
            candidate_cluster = points.iloc[start_index : end_index + 2]
            candidate_center = candidate_cluster.geometry.union_all().centroid
            max_distance = candidate_cluster.geometry.distance(candidate_center).max()
            if max_distance > STAY_DISTANCE_METERS:
                break
            end_index += 1

        cluster = points.iloc[start_index : end_index + 1]
        duration_s = (cluster["time"].iloc[-1] - cluster["time"].iloc[0]).total_seconds()
        if duration_s >= STAY_DURATION_SECONDS:
            points.loc[cluster.index, "is_stay"] = True
            center = cluster.geometry.union_all().centroid
            center_wgs84 = gpd.GeoSeries([center], crs=points.crs).to_crs(
                epsg=4326
            ).iloc[0]
            stop_groups.append(
                {
                    "start_time": cluster["time"].iloc[0],
                    "end_time": cluster["time"].iloc[-1],
                    "duration_s": duration_s,
                    "latitude": center_wgs84.y,
                    "longitude": center_wgs84.x,
                    "geometry": center_wgs84,
                }
            )

        start_index = end_index + 1

    stay_points = gpd.GeoDataFrame(
        stop_groups,
        columns=[
            "start_time",
            "end_time",
            "duration_s",
            "latitude",
            "longitude",
            "geometry",
        ],
        geometry="geometry",
        crs="EPSG:4326",
    )
    return points, stay_points


gps_points = parse_gpgga_file(INPUT_FILE)
analyzed_points, stay_points = analyze_trajectory(gps_points)

total_distance_m = analyzed_points["distance_m"].sum()
total_time_s = (gps_points["time"].max() - gps_points["time"].min()).total_seconds()
average_speed_kmh = total_distance_m / total_time_s * 3.6 if total_time_s else 0

print("=== PHAN TICH CHUOI GPS ===")
print(f"So cau NMEA hop le: {len(gps_points)}")
print(f"Tong quang duong: {total_distance_m / 1000:.3f} km")
print(f"Khoang thoi gian: {total_time_s / 60:.1f} phut")
print(f"Van toc trung binh: {average_speed_kmh:.2f} km/h")
print("\n=== DIEM DUNG ===")
if stay_points.empty:
    print(
        "Khong phat hien diem dung theo nguong "
        f">= {STAY_DURATION_SECONDS / 60:.0f} phut va <= {STAY_DISTANCE_METERS:.0f} m."
    )
else:
    for _, row in stay_points.iterrows():
        print(
            f"- {row['start_time'].strftime('%H:%M:%S')} - "
            f"{row['end_time'].strftime('%H:%M:%S')}: "
            f"{row['latitude']:.6f}, {row['longitude']:.6f}; "
            f"dung {row['duration_s'] / 60:.1f} phut"
        )

analyzed_points.drop(columns="geometry").to_csv(OUTPUT_CSV, index=False)
gps_points.to_file(OUTPUT_GEOJSON, driver="GeoJSON")

map_center = [gps_points.iloc[0]["latitude"], gps_points.iloc[0]["longitude"]]
gps_map = folium.Map(location=map_center, zoom_start=14)
trajectory_segment = []
for row in analyzed_points.itertuples():
    if trajectory_segment and row.distance_m > STAY_DISTANCE_METERS:
        folium.PolyLine(
            trajectory_segment,
            color="red",
            weight=3,
            tooltip="Chuoi GPS gan nhau",
        ).add_to(gps_map)
        trajectory_segment = []
    trajectory_segment.append((row.latitude, row.longitude))

if len(trajectory_segment) > 1:
    folium.PolyLine(
        trajectory_segment,
        color="red",
        weight=3,
        tooltip="Chuoi GPS gan nhau",
    ).add_to(gps_map)

for row in gps_points.itertuples():
    folium.CircleMarker(
        location=[row.latitude, row.longitude],
        radius=3,
        color="blue",
        fill=True,
        fill_opacity=0.7,
        tooltip=f"{row.time.strftime('%H:%M:%S')} - {row.latitude:.6f}, {row.longitude:.6f}",
    ).add_to(gps_map)

for row in stay_points.itertuples():
    folium.Marker(
        location=[row.latitude, row.longitude],
        icon=folium.Icon(color="green", icon="pause", prefix="fa"),
        tooltip=f"Diem dung: {row.time.strftime('%H:%M:%S')}",
    ).add_to(gps_map)

gps_map.save(OUTPUT_MAP)
print(f"\nDa luu chuoi GPS: {OUTPUT_CSV.name}")
print(f"Da luu quy dao GeoJSON: {OUTPUT_GEOJSON.name}")
print(f"Da luu ban do: {OUTPUT_MAP.name}")

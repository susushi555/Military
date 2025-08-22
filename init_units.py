import pandas as pd, geopandas as gpd
from shapely.geometry import Point

df = pd.read_csv('data/units.csv')
gdf = gpd.GeoDataFrame(
    df,
    geometry=[Point(xy) for xy in zip(df.lon, df.lat)],
    crs="EPSG:4326"
)
gdf.to_file("units.geojson", driver="GeoJSON")
print("Wrote units.geojson")


import pandas as pd, geopandas as gpd
from shapely.geometry import Point
import matplotlib.pyplot as plt, contextily as cx

df = pd.read_csv('data/units.csv')
gdf = gpd.GeoDataFrame(df,
                       geometry=[Point(xy) for xy in zip(df.lon, df.lat)], crs="EPSG:4326")
gdf3857 = gdf.to_crs(3857)

ax = gdf3857.plot(
    color=gdf["side"].map({"red": "red", "white": "white"}),
    edgecolor=gdf["side"].map({"red":"darked", "white": "gray"}),
    markersize=(gdf["personal"]**0.5)*3, figsize=(6,6)
)

cx.add_basemap(ax, attribution=False, source=cx.providers.OpenStreetMap.Mapink)
ax.set_axis_off(); plt.tight_layout(); plt.show();

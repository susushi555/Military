import geopandas as gpd

units = gpd.read_file("units.geojson").to_crs(4326)
cities = gpd.read_file("ne_10m_populated_places_simple.geojson").to_crs(4326)

nearest = gpd.sjoin_nearest(
    units, 
    cities[["name","adm1name","geometry"]],
    how="left"
)
print(nearest[["id","name","name","adm1name"]].rename(columns={"name_left":"unit","name_right":"city"}))

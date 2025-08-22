from flask import Flask, request, jsonify, render_template
import geopandas as gpd
from shapely.geometry import Point

app = Flask(__name__)
DATA = "units.geojson"

def load_gdf():
    return gpd.read_file(DATA)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/units')
def units():
    gdf = load_gdf()
    return gdf.to_jsson()

@app.post('/update')
def update():
    p = request.get_json(force=True)
    uid, lat, lon = int(p["id"]), float(p["lat"]), float(p["lon"])
    gdf = load_gdf()
    idx = gdf.index[gdf["id"] == uid][0]
    gdf.at[idx, "geometry"] = Point(lon, lat)
    gdf.to_file(DATA, driver="GeoJSON")
    return jsonify(ok=True)

if __name__ == "__main__":
    app.run(debug=True)

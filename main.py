from flask import Flask, jsonify
import psycopg2 
import json
import os

app = Flask(__name__)

db_params = {
    'database': "final_project",
    'user': os.environ.get("USER"),  
    'password': os.environ.get("PASSWORD"), 
    'host': "34.132.23.62",
    'port': "5432"
}

def fetch_geom_as_geojson(table_name, geom_column, db_params):
    conn = psycopg2.connect(**db_params)
    cur = conn.cursor()
    cur.execute(f"SELECT JSON_BUILD_OBJECT('type','FeatureCollection', 'features', JSON_AGG(ST_AsGeoJSON({table_name}.*)::json)) FROM {table_name}")
    geojson = cur.fetchone()[0]
    conn.close()
    return geojson


@app.route('/et')
def get_et_point():
    try:
        table_name = "et_point"
        geom_column = "shape"
        geojson = fetch_geom_as_geojson(table_name, geom_column, db_params)
        return jsonify(geojson)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/gdd')
def get_idw_gdd_point():
    try:
        table_name = "gdd_data"
        geom_column = "shape"
        geojson = fetch_geom_as_geojson(table_name, geom_column, db_params)
        return jsonify(geojson)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/soil')
def get_soil_point():
    try:
        table_name = "soil_point"
        geom_column = "shape"
        geojson = fetch_geom_as_geojson(table_name, geom_column, db_params)
        return jsonify(geojson)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8080)

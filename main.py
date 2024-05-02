rom flask import Flask, jsonify
import psycopg2 
import json
import os

app = Flask(__name__)

db_params = {
    'database': 'final_project',
    'user': 'postgres',  
    'password': 'gisishard2024', 
    'host': '34.132.23.62',
    'port': '5432'
}


@app.route('/idw_et_point')
def get_idw_temp_point():
    try:
        table_name = "idw_et_point"
        geom_column = "shape"
        geojson = fetch_geom_as_geojson(table_name, geom_column, db_params)

        return jsonify(geojson)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8080)

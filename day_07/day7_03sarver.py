from flask import Flask, request, jsonify
import sqlite3
from datetime import datetime

app = Flask(__name__)
DB_NAME = "smart_home.db"

# -------------------------------
# Database Initialization
# -------------------------------
def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS sensor_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            light_status TEXT,
            fan_status TEXT,
            temperature REAL,
            timestamp TEXT
        )
    """)
    conn.commit()
    conn.close()

init_db()

# -------------------------------
# Update Sensor Data
# -------------------------------
@app.route('/update', methods=['POST'])
def update_data():
    data = request.json

    light_status = data.get('light_status')
    fan_status = data.get('fan_status')
    temperature = data.get('temperature')

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO sensor_data (light_status, fan_status, temperature, timestamp)
        VALUES (?, ?, ?, ?)
    """, (light_status, fan_status, temperature, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    conn.commit()
    conn.close()

    return jsonify({"message": "Sensor data updated successfully"}), 200

# -------------------------------
# Get Current Status
# -------------------------------
@app.route('/status', methods=['GET'])
def get_status():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        SELECT light_status, fan_status, temperature, timestamp
        FROM sensor_data
        ORDER BY id DESC
        LIMIT 1
    """)
    row = cursor.fetchone()
    conn.close()

    if row:
        return jsonify({
            "Light": row[0],
            "Fan": row[1],
            "Temperature (°C)": row[2],
            "Last Updated": row[3]
        })
    else:
        return jsonify({"message": "No data available"}), 404

# -------------------------------
# Run Server
# -------------------------------
if __name__ == '__main__':
    app.run(debug=True)

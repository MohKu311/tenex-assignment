# db.py

import psycopg2
from psycopg2.extras import Json
from datetime import datetime

# Update these values as per your PostgreSQL setup
DB_CONFIG = {
    "host": "localhost",
    "port": 5432,
    "dbname": "tenex_logs",
    "user": "postgres",
    "password": "mohit123"
}

def insert_log_record(filename, parsed_logs):
    error_count = sum(1 for log in parsed_logs if log.get("anomaly"))
    normal_count = len(parsed_logs) - error_count

    try:
        conn = psycopg2.connect(**DB_CONFIG)
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO log_files (filename, logs, error_count, normal_count, uploaded_at)
            VALUES (%s, %s, %s, %s, %s);
        """, (filename, Json(parsed_logs), error_count, normal_count, datetime.now()))
        conn.commit()
        cur.close()
        conn.close()
    except Exception as e:
        print("❌ Failed to insert into database:", e)
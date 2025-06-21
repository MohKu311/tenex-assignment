# app.py
from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from log_parser import parse_log
from db import insert_log_record  # 👈 importing from db.py
from insert_log_entries import insert_individual_logs

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/upload', methods=['POST'])
def upload_log():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)

    try:
        parsed = parse_log(filepath)
        insert_log_record(file.filename, parsed)  # 👈 insert to PostgreSQL
        # Save detailed entries
        insert_individual_logs(filepath)

    except Exception as e:
        return jsonify({"error": f"Failed to parse or insert log: {str(e)}"}), 500

    return jsonify({
        "status": "success",
        "filename": file.filename,
        "parsed": parsed
    })

if __name__ == '__main__':
    print("✅ Flask backend running at http://localhost:5000")
    app.run(debug=True, port=5000)

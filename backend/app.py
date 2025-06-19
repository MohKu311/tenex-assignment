# app.py

from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from log_parser import parse_log

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
        print("✅ Parsed log type:", type(parsed))  # ✅ LOG TYPE DEBUG
        print("✅ Parsed content:", parsed)          # ✅ LOG DATA DEBUG
    except Exception as e:
        return jsonify({"error": f"Failed to parse log file: {str(e)}"}), 500

    return jsonify({
        "status": "success",
        "filename": file.filename,
        "parsed": parsed
    })

if __name__ == '__main__':
    print("✅ Flask backend running at http://localhost:5000")
    app.run(debug=True, port=5000)

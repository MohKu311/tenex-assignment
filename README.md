# 🔐 Tenex SOC Log Analyzer

A full-stack web application designed to help SOC (Security Operations Center) analysts upload, parse, and analyze log files to detect anomalies using both rule-based and AI-based threat detection.

---

## Objective

Built for a cybersecurity take-home interview assessment. This app simulates real-world log ingestion and analysis workflows with a focus on functionality and threat intelligence.

---

## Features

- ✅ Upload `.log` files via web frontend
- ✅ Log parsing and validation on backend
- ✅ Rule-based and AI-based anomaly detection
- ✅ Stores parsed entries and raw files in PostgreSQL
- ✅ Displays anomalies clearly in a human-consumable format
- ✅ Built-in basic login system
- ✅ Frontend charts for summarized insights

---

## Tech Stack

### Frontend

- **Next.js** (React framework)
- **TypeScript**
- **Chart.js** (Data visualization)
- **Axios** (HTTP requests)

### Backend

- **Flask** (Python framework)
- **PostgreSQL** (Database)
- **Scikit-learn** (RandomForestClassifier for ML)
- **Pickle** (Model serialization)

---

## Folder Structure

```bash
TENEX/
├── backend/                   # Python + Flask API, anomaly detection, DB layer
│   ├── app.py                 # Flask application factory / route bootstrap
│   ├── db.py                  # PostgreSQL connection & helpers
│   ├── log_parser.py          # Log-file parsing utilities
│   ├── insert_log_entries.py  # Script to seed / test the DB with sample logs
│   ├── requirements.txt       # Backend Python dependencies
│   ├── uploads/               # Temp storage for user-uploaded log files
│   └── ml/                    # Saved model, datasets & inference helpers
│       ├── ml_inference.py
│       ├── threat_model.pkl
│       ├── Synthetic_Log_Dataset.csv
│       └── threat_data.csv
│
├── frontend/                  # Next.js (TypeScript) UI
│   ├── src/                   # React components, pages, hooks, helpers
│   ├── public/                # Static assets
│   ├── package.json           # Front-end dependencies
│   └── tsconfig.json          # TypeScript config
│
├── test_data/                 # Example log files for local testing
│   ├── sample.log
│   ├── test1.log
│   ├── test2.log
│   ├── test3.log
│   └── test4.log
│
├── .gitignore                 # Global ignore rules (includes venv/, node_modules/, etc.)
├── Question.pdf               # Take-home assignment prompt
└── README.md                  # Project documentation (you’re here!)
```

---

## How to Run Locally

### Backend (Flask)

```bash
cd backend
python -m venv venv
venv\Scripts\activate       # On Windows
pip install -r requirements.txt
python train_model.py        # Trains and saves model
python app.py                # Starts Flask server on port 5000
```

### Frontend (Next.js)

```bash
cd frontend
npm install
npm run dev                  # Runs frontend on port 3000
```

### Login Credentials

```text
Email: admin@soc.com
Password: secure123
```

---

## How It Works

### 1. Upload Log File

User uploads a `.log` file via the dashboard.

### 2. Parsing

Each line is parsed to extract:

- timestamp
- source IP
- destination IP
- URL
- action
- status code
- user agent
- threat type

### 3. AI-Based Threat Detection

If `threat_type` or `action` is missing, a **RandomForestClassifier** predicts it. Predictions include:

- `threat_type`: malware, phishing, proxy, or benign (`-`)
- `action`: ALLOW or BLOCK

### 4. Anomaly Flagging

Logs are marked as anomalies if:

- Threat type ≠ "-"
- Action is BLOCK
- Malformed log line

### 5. Data Storage

- Raw log file stored in `log_files` table
- Individual entries saved in `log_entries` table (with anomaly flag)

### 6. Visualization

- Full list of parsed entries
- Anomaly toggle to filter
- Pie chart + bar graph breakdowns

---

## Sample Input & Output

**Raw log (input):**

```
2023-06-01T10:20:18Z,192.168.1.12,139.162.123.42,https://suspicious-login.com,,401,Mozilla/5.0,
```

**After ML classification:**

```
2023-06-01T10:20:18Z,192.168.1.12,139.162.123.42,https://suspicious-login.com,BLOCK,401,Mozilla/5.0,phishing
```

---

## Example Log Files

Test logs are in `/test_data/`:

- `test1.log` – Basic
- `test2.log` – Includes anomalies
- `test3.log` – Mixed
- `test4.log` – For full-scale testing

---

## 👨‍💻 Author

Mohit Kunder\
[LinkedIn Profile](https://linkedin.com/in/mohitkunder311)

---

## 📜 License

MIT


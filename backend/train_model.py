# backend/ml/train_model.py

import pandas as pd
import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder

# Load data
df = pd.read_csv("ml/threat_data.csv")

# Encode target label
df = df.fillna("-")
y = df["threat_type"]
X = df.drop(columns=["threat_type"])

# Define preprocessing for categorical columns
categorical_cols = ["source_ip", "dest_ip", "url", "user_agent", "status_code"]
preprocessor = ColumnTransformer(
    transformers=[("cat", OneHotEncoder(handle_unknown="ignore"), categorical_cols)]
)

# Create pipeline
pipeline = Pipeline([
    ("preprocessor", preprocessor),
    ("classifier", RandomForestClassifier(random_state=42))
])

# Fit and save model
pipeline.fit(X, y)

with open("ml/threat_model.pkl", "wb") as f:
    pickle.dump(pipeline, f)

print("✅ Model retrained and saved as threat_model.pkl")

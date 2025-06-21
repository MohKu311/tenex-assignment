import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import joblib

# Load data
df = pd.read_csv("ml/Synthetic_Log_Dataset.csv")

# Drop rows with missing threat_type (can't train on unknown labels)
df = df[df["threat_type"].notna() & (df["threat_type"] != "-")]

# Extract features and label
features = df.drop(columns=["threat_type"])
labels = df["threat_type"]

# Drop non-predictive columns
features = features.drop(columns=["timestamp", "action"])  # action is inferred, timestamp is not helpful

# Encode categorical features
for col in features.select_dtypes(include="object").columns:
    features[col] = LabelEncoder().fit_transform(features[col])

# Encode the labels
label_encoder = LabelEncoder()
labels_encoded = label_encoder.fit_transform(labels)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(features, labels_encoded, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save model and label encoder
joblib.dump(model, "ml/threat_model.pkl")
joblib.dump(label_encoder, "ml/threat_label_encoder.pkl")

print("✅ Model training complete and saved to disk.")

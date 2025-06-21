import pickle
import pandas as pd

# Load the full model pipeline (including encoder + classifier)
with open("ml/threat_model.pkl", "rb") as f:
    model = pickle.load(f)

def predict_threat_and_action(entry: dict) -> tuple[str, str]:
    """
    Predicts the threat type and action based on a log entry.
    """
    df = pd.DataFrame([entry])
    df = df.fillna("-")

    # Predict threat_type
    predicted_threat = model.predict(df)[0]

    # Decide action based on threat
    action = "BLOCK" if predicted_threat.lower() != "-" else "ALLOW"

    return predicted_threat, action

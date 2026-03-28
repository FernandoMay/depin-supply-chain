from flask import Flask, request, jsonify
import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)

# Placeholder for a trained model
# In a real scenario, this would be loaded from a file (e.g., .pkl)
model = None
scaler = None

def train_anomaly_model(data: pd.DataFrame):
    global model, scaler
    # For demonstration, let's assume 'temperature' and 'humidity' are features
    features = data[["temperature", "humidity"]]
    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(features)
    
    model = IsolationForest(random_state=42)
    model.fit(scaled_features)
    print("Anomaly detection model trained.")

def predict_anomalies(data: pd.DataFrame) -> np.ndarray:
    if model is None or scaler is None:
        return np.array([0] * len(data)) # No anomaly if model not trained
    
    features = data[["temperature", "humidity"]]
    scaled_features = scaler.transform(features)
    predictions = model.predict(scaled_features)
    # IsolationForest returns -1 for anomalies, 1 for normal
    return np.array([1 if p == -1 else 0 for p in predictions])

@app.route("/predict_anomaly", methods=["POST"])
def anomaly_prediction():
    data = request.json
    if not data:
        return jsonify({"error": "No data provided"}), 400
    
    try:
        df = pd.DataFrame(data)
        # Ensure required columns are present for training/prediction
        if not all(col in df.columns for col in ["temperature", "humidity"]):
            return jsonify({"error": "Missing required features (temperature, humidity)"}), 400

        # In a real application, training would happen periodically or on new data batches
        # For this scaffold, we'll just predict.
        # If you want to simulate training, uncomment the line below and provide training data.
        # train_anomaly_model(df) 

        anomalies = predict_anomalies(df)
        return jsonify({"predictions": anomalies.tolist()})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/", methods=["GET"])
def health_check():
    return jsonify({"status": "AI module is running"}), 200

if __name__ == "__main__":
    # Example usage: Simulate some data and train the model
    sample_data = pd.DataFrame({
        "temperature": np.random.normal(25, 2, 100),
        "humidity": np.random.normal(60, 5, 100)
    })
    # Introduce a few anomalies
    sample_data.loc[5, "temperature"] = 40
    sample_data.loc[10, "humidity"] = 10

    train_anomaly_model(sample_data)

    app.run(debug=True, port=5000)

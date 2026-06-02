import pytest
import pandas as pd
import numpy as np
from unittest.mock import patch, MagicMock
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from app import app, train_anomaly_model, predict_anomalies


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as c:
        yield c


class TestAnomalyDetection:
    def test_train_and_predict(self):
        data = pd.DataFrame({"temperature": [25, 26, 24, 40, 25], "humidity": [60, 61, 59, 58, 10]})
        train_anomaly_model(data)
        result = predict_anomalies(data)
        assert len(result) == 5
        assert result.dtype == np.int64

    def test_predict_without_training(self):
        import app as app_module
        app_module.model = None
        app_module.scaler = None
        data = pd.DataFrame({"temperature": [25, 26], "humidity": [60, 61]})
        result = predict_anomalies(data)
        assert list(result) == [0, 0]


class TestFlaskRoutes:
    def test_health(self, client):
        resp = client.get("/")
        assert resp.status_code == 200
        assert resp.get_json() == {"status": "AI module is running"}

    def test_predict_no_data(self, client):
        resp = client.post("/predict_anomaly", json={})
        assert resp.status_code == 400

    def test_predict_missing_features(self, client):
        resp = client.post("/predict_anomaly", json=[{"foo": 1}])
        assert resp.status_code == 400

    @patch("app.predict_anomalies")
    def test_predict_success(self, mock_predict, client):
        mock_predict.return_value = np.array([0, 1, 0])
        resp = client.post("/predict_anomaly", json=[
            {"temperature": 25, "humidity": 60},
            {"temperature": 40, "humidity": 10},
            {"temperature": 24, "humidity": 59}
        ])
        assert resp.status_code == 200
        assert resp.get_json() == {"predictions": [0, 1, 0]}

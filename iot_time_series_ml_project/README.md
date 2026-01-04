# IoT Time Series Forecasting & Anomaly Detection

## How to Run
1. Install dependencies: pip install -r requirements.txt
2. Run sensor simulator: python iot/sensor_simulator.py
3. Train model: python ml/train_lstm.py
4. Detect anomalies: python ml/anomaly_detection.py
5. Launch dashboard: streamlit run app.py
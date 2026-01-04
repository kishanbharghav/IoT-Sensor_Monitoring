import pandas as pd
import numpy as np
import os
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

# Safe path handling
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "data", "sensor_data.csv")

# Load data safely
df = pd.read_csv(DATA_PATH)

# Convert types
df['temperature'] = pd.to_numeric(df['temperature'], errors='coerce')
df.dropna(inplace=True)

# Scale data
scaler = MinMaxScaler()
scaled = scaler.fit_transform(df[['temperature']])

# Create sequences
X, y = [], []
WINDOW = 5

for i in range(WINDOW, len(scaled)):
    X.append(scaled[i-WINDOW:i])
    y.append(scaled[i])

X = np.array(X)
y = np.array(y)

print("Training samples:", X.shape)

# Build LSTM
model = Sequential([
    LSTM(32, input_shape=(X.shape[1], X.shape[2])),
    Dense(1)
])

model.compile(optimizer="adam", loss="mse")
model.fit(X, y, epochs=10, batch_size=8)

# Save model
model.save(os.path.join(BASE_DIR, "ml", "lstm_model.h5"))
print("✅ LSTM model trained & saved")

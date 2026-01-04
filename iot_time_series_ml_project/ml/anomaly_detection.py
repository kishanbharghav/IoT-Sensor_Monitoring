import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "data", "sensor_data.csv")

df = pd.read_csv(DATA_PATH)
df['temperature'] = pd.to_numeric(df['temperature'], errors='coerce')
df.dropna(inplace=True)

mean = df['temperature'].mean()
std = df['temperature'].std()

df['anomaly'] = abs(df['temperature'] - mean) > 2 * std

print("🔥 Detected anomalies:")
print(df[df['anomaly']])

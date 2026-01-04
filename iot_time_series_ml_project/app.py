import streamlit as st
import pandas as pd

st.title("IoT Sensor Monitoring Dashboard")

import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
df = pd.read_csv(os.path.join(BASE_DIR, "data", "sensor_data.csv"))
st.line_chart(df[['temperature', 'humidity']])

st.subheader("Anomalies")
mean = df['temperature'].mean()
std = df['temperature'].std()
df['anomaly'] = abs(df['temperature'] - mean) > 2 * std
st.write(df[df['anomaly']])
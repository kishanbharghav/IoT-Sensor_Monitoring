import time
import csv
import random
import datetime
import os

# Always resolve path from project root
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "data", "sensor_data.csv")

# Ensure data folder exists
os.makedirs(os.path.dirname(DATA_PATH), exist_ok=True)

with open(DATA_PATH, "a", newline="") as f:
    writer = csv.writer(f)

    while True:
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        temp = random.randint(24, 36)
        hum = random.randint(55, 85)

        writer.writerow([now, temp, hum])
        f.flush()

        print(f"Generated → Temp: {temp}, Humidity: {hum}")
        time.sleep(5)

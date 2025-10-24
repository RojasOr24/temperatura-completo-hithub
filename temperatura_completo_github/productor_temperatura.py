from kafka import KafkaProducer
import pandas as pd
import json, time

# Productor de datos de temperatura para Kafka
df = pd.read_csv("historical-weather-medellin.csv")

producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

for _, row in df.iterrows():
    mensaje = {
        "date": str(row.get("date")),
        "tempmax": float(row.get("tempmax", 0)),
        "tempmin": float(row.get("tempmin", 0)),
        "temp": float(row.get("temp", 0))
    }
    producer.send("clima_medellin", value=mensaje)
    print(f"Enviado: {mensaje}")
    time.sleep(1)

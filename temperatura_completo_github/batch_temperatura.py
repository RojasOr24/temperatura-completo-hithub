from pyspark.sql import SparkSession
from pyspark.sql.functions import col, avg, max, min

# Procesamiento batch de temperaturas
spark = SparkSession.builder.appName("TemperaturaMedellinBatch").getOrCreate()
data_path = "historical-weather-medellin.csv"
df = spark.read.csv(data_path, header=True, inferSchema=True)

df.printSchema()
df.show(5)

df_clean = df.select("date", "tempmax", "tempmin", "temp").dropna()

stats = df_clean.agg(
    avg("tempmax").alias("promedio_max"),
    avg("tempmin").alias("promedio_min"),
    avg("temp").alias("promedio_general"),
    max("tempmax").alias("temperatura_maxima"),
    min("tempmin").alias("temperatura_minima")
)

stats.show()
stats.write.mode("overwrite").csv("resultados_temperatura_batch/")
print("✅ Resultados guardados en resultados_temperatura_batch/")

from pyspark.sql import SparkSession

# Start Spark
spark = SparkSession.builder \
    .appName("VSCodeTest") \
    .master("local[*]") \
    .getOrCreate()

# Simple DataFrame
df = spark.createDataFrame([(1,), (2,), (3,)], ["numbers"])

df.show()

spark.stop()
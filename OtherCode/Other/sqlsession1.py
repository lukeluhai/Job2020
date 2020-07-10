from pyspark.sql import SparkSession
spark=SparkSession.builder.getOrCreate()
df = spark.read.json('file:///home/hadoop/people.json')
df.show()


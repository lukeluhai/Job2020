from pyspark.sql import HiveContext
from pyspark import SparkContext, SparkConf
conf = SparkConf().setMaster("spark://Masteru:7077").setAppName('myApp')
sc = SparkContext(conf=conf)

hivectx = HiveContext(sc)

rows = hivectx.sql("show databases").collect()
print(rows.collect())

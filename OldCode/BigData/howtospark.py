from pyspark import SparkConf,SparkContext
from pyspark.sql import HiveContext
from pyspark.sql import SparkSession


conf = SparkConf().setMaster("spark://Masteru:7077").setAppName("My App")
sc = SparkContext(conf = conf)
hivectx = HiveContext(sc)
a = sc.textFile('hdfs://Masteru:9000/RLCPP.csv')
print(a.collect())

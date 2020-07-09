from pyspark import SparkContext,SparkConf
conf=SparkConf().setMaster("192.168.10.150").setAppName('my App')
sc=SparkContext(conf=conf)
lines=sc.parallelize(['a','b','c'])
lines.collect()


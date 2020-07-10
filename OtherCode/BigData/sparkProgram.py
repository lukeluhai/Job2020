from pyspark import SparkContext,SparkConf
import os
os.environ['JAVA_HOME']='/usr/lib/jvm/java-8-openjdk-amd64'
os.environ['HADOOP_HOME']='/usr/local/hadoop'
os.environ['SPARK_HOME']='/usr/local/spark'
os.environ['PYTHONPATH']='/usr/local/spark/python/lib/py4j-0.10.4-src.zip'

#export SPARK_HOME=/usr/local/spark
#export PYTHONPATH=$SPARK_HOME/python:$SPARK_HOME/python/lib/py4j-0.10.4-src.zip:$PYTHONPATH
#export PYSPARK_PYTHON=python3
#export PATH=$HADOOP_HOME/bin:$SPARK_HOME/bin:$PATH

conf=SparkConf().setMaster("local").setAppName('myApp')
sc=SparkContext(conf=conf)
lines=sc.parallelize(['a','b','c'])
lines.collect()
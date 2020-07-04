from pyspark.sql import HiveContext
from pyspark import SparkContext,SparkConf
conf=SparkConf().setMaster("spark://Masteru:7077").setAppName('myApp')
sc=SparkContext(conf=conf)

hivectx=HiveContext(sc)

rows=hivectx.sql("show databases").collect()

print(rows.collect())




from pyspark import SparkContext,SparkConf
import os


def filter1(x):
    try:
        return int(x.split(',')[3]) > 46
    except:
        return False


#os.environ['JAVA_HOME']='/usr/lib/jvm/java-8-openjdk-amd64'
#os.environ['HADOOP_HOME']='/usr/local/hadoop'
#os.environ['SPARK_HOME']='/usr/local/spark'
#os.environ['PYTHONPATH']='/usr/local/spark/python/lib/py4j-0.10.4-src.zip'

#export SPARK_HOME=/usr/local/spark
#export PYTHONPATH=$SPARK_HOME/python:$SPARK_HOME/python/lib/py4j-0.10.4-src.zip:$PYTHONPATH
#export PYSPARK_PYTHON=python3
#export PATH=$HADOOP_HOME/bin:$SPARK_HOME/bin:$PATH

conf=SparkConf().setMaster("spark://Masteru:7077").setAppName('myApp')
sc=SparkContext(conf=conf)
RLCPPCSV=sc.textFile('hdfs://Masteru:9000/user/data/RLCPP.csv')
RLDEPCSV=sc.textFile('hdfs://Masteru:9000/user/data/RLDEP.csv')

'''
s=RLCPPCSV.flatMap(lambda x:x+'|').collect()
for i in s:

    print(i)
d=RLCPPCSV.map(lambda x:x+'|').collect()
for i in d:

    print(i)


'''
#d=RLCPPCSV.map(lambda x:(x.split(',')[3],1)).reduceByKey(lambda x,y:x+y)
#print(d.collect())
a=RLCPPCSV.map(lambda x:(x.split(',')[1],x))
b=RLDEPCSV.map(lambda x:(x.split(',')[1],x))
c=a.join(b)
c=c.map(lambda x:x[0]+","+x[1][0]+','+x[1][1])
for i in c.collect():
    print(i)
'''
d=c.join(b)
for i in d.collect():
    print(i)
e=d.map(lambda x:x.split(','))
for i in e.collect():
    print(i)
'''



from pyspark import SparkContext, SparkConf
import os
import csv
from io import StringIO
import json


conf = SparkConf().setMaster("spark://Masteru:7077").setAppName('myApp')
sc = SparkContext(conf=conf)

'''
def loadRcord(line):
    input = StringIO(line)
    reader = csv.DictReader(input)
    return reader
'''

input = sc.textFile('hdfs://Masteru:9000/package.json')


data=input.map(lambda x:json.load(x))

print(data.count())

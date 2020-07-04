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

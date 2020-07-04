from pyspark import SparkContext, SparkConf
conf = SparkConf().setMaster("spark://Masteru:7077").setAppName('myApp')
sc = SparkContext(conf=conf)
rldep=sc.textFile('hdfs://masteru:9000/tmp/cdd/RLDEP.CSV').distinct()
rldep=rldep.map(lambda x:(x.split(',',2)[1],x.split(',',2)[2]))

rlcpp=sc.textFile('hdfs://masteru:9000/tmp/cdd/RLCPP.CSV').distinct()
rlcpp=rlcpp.map(lambda x:(x.split(',',2)[1],x.split(',',2)[2]))

rlchp=sc.textFile('hdfs://masteru:9000/tmp/cdd/RLCHP.CSV').distinct()
rlchp=rlchp.map(lambda x:(x.split(',',2)[1],x.split(',',2)[2]))
cdd=rldep.leftOuterJoin(rlcpp)
cdd=cdd.leftOuterJoin(rlchp)
for i in cdd.collect():

    print(i)
from pyspark import SparkConf,SparkContext
from pyspark.mllib.regression import LabeledPoint
from pyspark.mllib.feature import HashingTF
from pyspark.mllib.classification import LogisticRegressionWithLBFGS
conf = SparkConf().setMaster("local").setAppName("My App")
sc = SparkContext(conf = conf)
spam = sc.textFile('bad.csv')
normal = sc.textFile('good.csv')
test = sc.textFile('test.csv')
tf = HashingTF(numFeatures=10000)
spamFeatures = spam.map(lambda email:tf.transform(email.split(',')))
normalFeatures = normal.map(lambda email:tf.transform(email.split(',')))
positiveExample = spamFeatures.map(lambda features:LabeledPoint(1,features))
negativeExample = normalFeatures.map(lambda features:LabeledPoint(0,features))

trainingData = positiveExample.union(negativeExample)
trainingData.cache()
model = LogisticRegressionWithLBFGS.train(trainingData)
testResult = tf.transform(test.map(lambda x:x.split(',')))

print(model.predict(testResult).collect())
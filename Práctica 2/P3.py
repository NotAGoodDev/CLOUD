#!/usr/bin/python
import sys
from pyspark import SparkConf, SparkContext, SQLContext
conf = SparkConf().setAppName("Ex 3")
sc = SparkContext(conf=conf)
#sqlc = SQLContext(sc)

file = 'GOOGLE.csv'
fileRDD = sc.textFile(file).persist() #To RAM
dataRDD = fileRDD.filter(lambda line: "Date" not in line)
#Subset1 -> (year, close)
subsetRDD1 = dataRDD.map(lambda x: (int(x.split("-")[0]), float(x.split(",")[4])))

#Subset2 -> (year, repet)
subsetRDD2 = dataRDD.map(lambda x: (int(x.split("-")[0]), 1))

#reduce by year and join them
#(year(sum(close), sum(repet)))
submit = (subsetRDD1.reduceByKey(lambda x, y: x+y).join(subsetRDD2.reduceByKey(lambda x, y: x+y)))

#(year, sum(close)/sum(repet))
submit = submit.map(lambda x: (x[0], x[1][0] / x[1][1])).sortByKey()

submit.saveAsTextFile("output")

#!/usr/bin/python
import sys
from pyspark import SparkConf, SparkContext
conf = SparkConf().setAppName("Ex 2")
sc = SparkContext(conf=conf)

file = 'access_log'
fileRDD = sc.textFile(file).persist()   #To RAM

#Clean "OPTIONS *" and line 907, i dont consider them lines
cleanRDD = fileRDD.filter(lambda line: "\"-\"" not in line).filter(lambda line: "OPTIONS *" not in line)

urlsRDD = cleanRDD.map(lambda x: (str(x.split(" \"")[1].split(" ")[1]), 1))

resultRDD = urlsRDD.reduceByKey(lambda x, y: x+y).sortByKey()

resultRDD.saveAsTextFile("output")

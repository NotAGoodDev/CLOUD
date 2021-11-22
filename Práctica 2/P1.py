#!/usr/bin/python
import sys
from pyspark import SparkConf, SparkContext
conf = SparkConf().setAppName("Ex 1")
sc = SparkContext(conf=conf)

keyWord = sys.argv[1]

file = 'input.txt'
fileRDD = sc.textFile(file)
lines = fileRDD.filter(lambda line : keyWord in line).saveAsTextFile("output")


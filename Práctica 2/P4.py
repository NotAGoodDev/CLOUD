#!/usr/bin/python
import sys, math
from pyspark import SparkConf, SparkContext, SQLContext
conf = SparkConf().setAppName("Ex 4")
sc = SparkContext(conf=conf)
    

file = 'ratings.csv'
fileRDD = sc.textFile(file).persist()   #To RAM
fileRDD = fileRDD.filter(lambda line: "movieId" not in line);

#(movieid, rating)
dataset1 = fileRDD.map(lambda line: (int(line.split(",")[1]), float(line.split(",")[2])))

#(movieid, times)
dataset2 = fileRDD.map(lambda line: (int(line.split(",")[1]), 1))

#(movieid, (rating, times))     sorted by id
rating = dataset1.reduceByKey(lambda x, y: x+y).join(dataset2.reduceByKey(lambda x, y: x+y)).sortByKey()

#sorted by range (+ id)   ^
rating = rating.map(lambda x: ("Range: " + str(int(math.ceil(x[1][0] / x[1][1]))), x[0])).sortByKey()

rating.saveAsTextFile("output")

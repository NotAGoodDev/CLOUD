#!/usr/bin/python
import sys
from pyspark import SparkConf, SparkContext, SQLContext
conf = SparkConf().setAppName("Ex 5")
sc = SparkContext(conf=conf)
    

file = 'Meteorite_Landings.csv'
fileRDD = sc.textFile(file).persist()   #To RAM

#cleaning the RDD
cleanRDD = fileRDD.map(lambda x: (x.replace("~", "").replace('"', "").replace(", ", "-").replace(" ", "").replace(",,", ",0,")))

#mapping the key(type) - value(mass)
mappedRDD = cleanRDD.map(lambda x: (str(x.split(",")[3]), float(x.split(",")[4])))

#key(type) - value(times)
timesRDD = cleanRDD.map(lambda x: (str(x.split(",")[3]), 1))

#reduce
result = mappedRDD.reduceByKey(lambda x, y: x+y).join(timesRDD.reduceByKey(lambda x, y: x+y)).sortByKey()   #Reduced by keys the mass and the times -> (key, (mass, times))

#result
result = result.map(lambda x: (x[0], x[1][0] / x[1][1]))    #By key -> mass / times

result.saveAsTextFile("output")

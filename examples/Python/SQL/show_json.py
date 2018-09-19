import os
import sys
from pyspark import SparkContext, SparkFiles
from pyspark import  SQLContext, Row


conf = SparkConf().setMaster("spark://spark:7077").setAppName("Streaming-app")
sc = SparkContext(conf = conf)

files = SparkFiles.get()
print (files)
sqlc = SQLContext(sc)

print (str(sys.argv))
filename = sys.argv[0]

input = spark.read.json(filename)
input.show()

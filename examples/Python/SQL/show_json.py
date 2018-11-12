import os
import sys
from pyspark import SparkContext, SparkConf, SparkFiles
from pyspark import  SQLContext, Row


conf = SparkConf().setMaster("spark://spark:7077").setAppName("Streaming-app")
sc = SparkContext(conf = conf)


sqlc = SQLContext(sc)


input = sqlc.read.json("people.json")
input.show()

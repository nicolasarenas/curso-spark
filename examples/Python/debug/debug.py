log_file = sc.textFile("input.txt")
tokens = log_file.filter(lambda line: int(len (line)) > 0 ).map(lambda line: line.split(" "))
counts = tokens.map(lambda words: (words[0] , 1)).reduceByKey(lambda a , b: a + b)
print counts.collect()

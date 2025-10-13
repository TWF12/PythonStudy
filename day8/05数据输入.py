from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("local[*]").setAppName("test_spark")

sc = SparkContext(conf=conf)

# 通过parallelize方法将python中的数据类型转换为RDD对象
rdd1 = sc.parallelize([1, 2, 3, 4, 5])
rdd2 = sc.parallelize((1, 2, 3, 4, 5))
rdd3 = sc.parallelize("12345")
rdd4 = sc.parallelize({1, 2, 3, 4, 5})
rdd5 = sc.parallelize({"one": 1, "two": 2, "three": 3})

# 通过collect方法获取RDD对象中的数据
# print(rdd1)
print(rdd1.collect())
print(rdd2.collect())
print(rdd3.collect())
print(rdd4.collect())
print(rdd5.collect())

# 通过textfile方法将文件转换为RDD对象
rdd6 = sc.textFile("test.txt")
print(rdd6.collect())

sc.stop()

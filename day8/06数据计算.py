from pyspark import SparkConf, SparkContext
import os
os.environ['PYSPARK_PYTHON'] = 'D:\\PythonStudy\\.venv\\Scripts\\python.exe'


conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
sc = SparkContext(conf=conf)

rdd1 = sc.parallelize([1, 2, 3, 4, 5])

# 使用map算子将rdd1中的每个元素乘以2
rdd2 = rdd1.map(lambda x: x * 2)

print(rdd2.collect())

# flatMp算子与map算子类似, 但是flatMap算子可以解除嵌套
rdd3 = sc.parallelize(["hello world", "hello python", "hello spark"])
rdd4 = rdd3.map(lambda x: x.split(" "))
rdd5 = rdd3.flatMap(lambda x: x.split(" "))
print(rdd4.collect())
print(rdd5.collect())



sc.stop()
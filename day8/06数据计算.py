from pyspark import SparkConf, SparkContext
import os
os.environ['PYSPARK_PYTHON'] = 'D:\\PythonStudy\\.venv\\Scripts\\3.10.exe'


conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
sc = SparkContext(conf=conf)

rdd1 = sc.parallelize([1, 2, 3, 4, 5])

# 使用map算子将rdd1中的每个元素乘以2
rdd2 = rdd1.map(lambda x: x * 2)

print(rdd2.collect())




sc.stop()
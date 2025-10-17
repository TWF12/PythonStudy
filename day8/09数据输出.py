from pyspark import SparkConf, SparkContext
import os

# 使用jdk-11与pyspark兼容
os.environ["JAVA_HOME"] = "D:\\develop\\java\\jdk-11"
# 指定python解释器路径(数据计算时会调用python解释器)
os.environ["PYSPARK_PYTHON"] = "D:\\PythonStudy\\.venv\Scripts\\python.exe"
# 指定hadoop路径(saveAsTextFile算子会调用hadoop)
os.environ["HADOOP_HOME"] = "D:\\Python UV\\hadoop-3.0.0"

conf = SparkConf().setMaster("local[*]").setAppName("test_spark")

sc = SparkContext(conf=conf)

rdd = sc.parallelize([1, 2, 3, 4, 5])

# collect算子将RDD对象转换成列表
l = rdd.collect()
print(type(l))
print(l)

# reduce算子对RDD对象中的所有数据进行聚合
sum_result = rdd.reduce(lambda x, y: x + y)
print(sum_result)

# take算子获取rdd对象中的前n个元素并转换成列表
list_3 = rdd.take(3)
print(type(list_3))
print(list_3)

# count算子计算rdd对象中元素个数
rdd_count = rdd.count()
print(rdd_count)

# 使用saveAsTextFile算子将rdd对象中的数据保存到文件中
rdd.saveAsTextFile("output1")


sc.stop()
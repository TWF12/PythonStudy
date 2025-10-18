from pyspark import SparkConf, SparkContext
import os
# 使用jdk-11与pyspark兼容
os.environ["JAVA_HOME"] = "D:\\develop\\java\\jdk-11"
# 指定python解释器路径(数据计算时会调用python解释器)
os.environ["PYSPARK_PYTHON"] = "D:\\PythonStudy\\.venv1\\Scripts\\python.exe"


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

# reduceByKey算子实现对二元元组按key分组并对value进行聚合
rdd6 = sc.parallelize([("男", 99), ("女", 98), ("男", 97), ("女", 96)])
rdd6.reduceByKey(lambda a, b: a + b)
print(rdd6.collect())

# filter方法过滤rdd中的数据
rdd7 = sc.parallelize([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
rdd__filter = rdd7.filter(lambda x: x % 2 == 0)
print(rdd__filter.collect())

# distinct方法去重
rdd8 = sc.parallelize([1, 2, 3, 4, 5, 1, 2, 3, 4, 5])
rdd_distinct = rdd8.distinct()
print(rdd_distinct.collect())

sc.stop()

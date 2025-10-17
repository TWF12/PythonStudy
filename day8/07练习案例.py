from pyspark import SparkConf, SparkContext
# 设置环境变量
import os
# 使用jdk-11与pyspark兼容
os.environ["JAVA_HOME"] = "D:\\develop\\java\\jdk-11"
# 指定python解释器路径(数据计算时会调用python解释器)
os.environ["PYSPARK_PYTHON"] = "D:\\PythonStudy\\.venv\Scripts\\python.exe"

# 创建SparkConf对像和SparkContext对象
conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
sc = SparkContext(conf=conf)

# 读取文件数据创建RDD对象
rdd = sc.textFile("test.txt")

# 使用flatMap算子将每行数据拆分为单词
rdd2 = rdd.flatMap(lambda line: line.split(" "))

# 使用map算子将每个单词转换成二元元组
rdd3 = rdd2.map(lambda word: (word, 1))

# 使用reduceByKey算子对二元元组按单词分组并求和
rdd4 = rdd3.reduceByKey(lambda x, y: x + y)

# 使用sortBy算子对结果按单词数量排序
rdd5 = rdd4.sortBy(lambda x: x[1], ascending=False, numPartitions=1)

# 输出结果
print(rdd5.collect())

sc.stop()

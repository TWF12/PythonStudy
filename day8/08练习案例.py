from pyspark import SparkConf, SparkContext
import json
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
rdd1 = sc.textFile("orders.txt")

# 使用flatMap算子将每行数据拆分为json字符串
rdd2 = rdd1.flatMap(lambda line: line.split("|"))

# 使用map算子将每个json字符串转换成字典
rdd3 = rdd2.map(lambda x: json.loads(x))

# 使用map算子将每个字典转成二元元组,(城市, 销售额)
rdd4 = rdd3.map(lambda x: (x["areaName"], float(x["money"])))

# 使用reduceByKey算子对二元元组按城市分组对销售额聚合
rdd5 = rdd4.reduceByKey(lambda x, y: x + y)

# 使用sortBy算子对结果按销售额降序排序
rdd6 = rdd5.sortBy(lambda x: x[1], ascending=False, numPartitions=1)
print(rdd6.collect())

# 获取所有商品类别
rdd7 = rdd3.map(lambda x: x["category"]).distinct()
print(rdd7.collect())

# 获取北京的销售商品
rdd8 = rdd3.filter(lambda x: x["areaName"] == "北京").map(lambda x: x["category"]).distinct()
print(rdd8.collect())



sc.stop()

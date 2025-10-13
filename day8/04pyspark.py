from pyspark import SparkConf, SparkContext

# 创建SparkConf对象
conf = SparkConf().setMaster("local[*]").setAppName("test_spark_app")

# 创建SparkContext对象
sc = SparkContext(conf=conf)

# 输出版本
print(sc.version)

# 停止SparkContext
sc.stop()
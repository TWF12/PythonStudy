from pyspark import SparkConf, SparkContext
import os
# 使用jdk-11与pyspark兼容
os.environ["JAVA_HOME"] = "D:\\develop\\java\\jdk-11"
# 指定python解释器路径(数据计算时会调用python解释器)
os.environ["PYSPARK_PYTHON"] = "D:\\PythonStudy\\.venv1\Scripts\\python.exe"
# 指定hadoop路径(saveAsTextFile算子会调用hadoop)
os.environ["HADOOP_HOME"] = "D:\\Python UV\\hadoop-3.0.0"

conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
# 设置默认并行度为1
conf.set("spark.default.parallelism", "1")
sc = SparkContext(conf=conf)

# 读取文件数据创建RDD对象
rdd = sc.textFile("search_log.txt")

# 得到所有时间段数据
rdd_time = rdd.map(lambda x: x.split("\t")[0][:2])
# 把所有时间段数据转换成二元元组
rdd_time_tuple = rdd_time.map(lambda x: (x, 1))
# 对二元元组按时间段分组求和来得到各时间段的搜索次数
rdd_time_count = rdd_time_tuple.reduceByKey(lambda x, y: x + y)
# 对结果按次数降序排序
rdd_time_count_sorted = rdd_time_count.sortBy(lambda x: x[1], ascending=False, numPartitions=1)
# 输出前三热门时段
print(rdd_time_count_sorted.take(3))

# 得到所有搜索关键词
rdd_keyword = rdd.map(lambda x: x.split("\t")[2])
# 把所有关键词转换成二元元组
rdd_keyword_tuple = rdd_keyword.map(lambda x: (x, 1))
# 对二元元组按关键词分组求和来得到个关键词的搜索次数
rdd_keyword_count = rdd_keyword_tuple.reduceByKey(lambda x, y: x + y)
#  对结果按搜索次数降序排序
rdd_keyword_count_sorted = rdd_keyword_count.sortBy(lambda x: x[1], ascending=False, numPartitions=1)
# 输出前三热门关键词
print(rdd_keyword_count_sorted.take(3))

# 得到黑马程序员关键词时段和搜锁次数数据
rdd_blackhorse_time_count = rdd.map(lambda x: x.split("\t")).filter(lambda x: x[2] == "黑马程序员").map(lambda x: (x[0][:2], 1))
# 对二元元组按时间段分组求和来得到各时间段的搜索次数
rdd_blackhorse_count_by_time_tuple = rdd_blackhorse_time_count.reduceByKey(lambda x, y: x + y)
# 对结果按搜索次数降序排序
rdd_blackhorse_count_by_time_tuple_sorted = rdd_blackhorse_count_by_time_tuple.sortBy(lambda x: x[1], ascending=False, numPartitions=1)
# 输出搜索次数最多的时段
print(rdd_blackhorse_count_by_time_tuple_sorted.take(1))

# 将rdd对象中的数据转换成json格式保存到文件中
rdd.map(lambda x: x.split("\t")).\
    map(lambda x: '{"time": %s,"user": %s,"keyword": %s, "rank1": %d, "rank2": %d, "url": %s}'\
                  % (x[0], x[1], x[2], int(x[3]), int(x[4]), x[5])).saveAsTextFile("output2")


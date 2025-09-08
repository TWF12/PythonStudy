# 通过占位符,拼接字符串
name = "黑马程序员"
message = "学it来%s" % name
print(message)

# 通过占位符完成数字与字符串拼接
class_num = 57
avg_salary = 16781
message = "Python大数据学科,北京%s期,毕业平均工资: %s" % (class_num, avg_salary)
print(message)

name = "传智播客"
setup_year = 2006
stock_price = 19.99
message ="%s, 成立于%d, 今天股价为%f" % (name, setup_year, stock_price)
print(message)

# 宽度和精度控制
num1 = 11
num2 = 11.345
print("数字11宽度5, 结果是: %5d" % num1)
print("数字11宽度1, 结果是: %1d" % num1)
print("数字11.325宽度7,精度2,结果是: %7.2f" % num2)
print("数字11.325宽度不限制,精度2,结果是: %.2f" % num2)


# 快速格式化字符串(不对其类型,宽度,精度做控制)
print(f"{name}, 成立于{setup_year}, 今日股价为{stock_price}")




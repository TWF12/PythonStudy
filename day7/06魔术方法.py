class Student:
    # 重写构造方法
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # 重写输出对象内容
    def __str__(self):
        return f"name: {self.name}, age: {self.age}"
    # 重写对象大小比较规则(<)
    def __lt__(self, other):
        return self.age < other.age
    # 重写对象大小比较规则(<=)
    def __le__(self, other):
        return self.age <= other.age
    # 重写相等比较规则
    def __eq__(self, other):
        return self.name == other.name and self.age == other.age

stu1 = Student("周杰伦", 31)
print(stu1)  # 默认打印的是对象的地址, 重写__str__魔术方法可以改变打印的内容

stu2 = Student("林俊杰", 32)
print(stu1 <= stu2) # 如果没有重写__it__(或__le__)魔术方法, 两个对象不能比较大小, 会报错

print(stu1 == stu2) # 默认比较的是对象地址,重写__ep___魔术方法, 可以比较对象的属性


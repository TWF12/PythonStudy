class Student:
    # name = None
    # age = None
    # tel = None

    def __init__(self,name,age,tel):
        self.name = name
        self.age = age
        self.tel = tel
        print("成功创建一个对象")

stu = Student("林俊杰", 31, "18453279542")
print(stu.name)
print(stu.age)
print(stu.tel)
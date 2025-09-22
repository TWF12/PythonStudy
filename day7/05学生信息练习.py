class Student:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

students = []

for i in range(10):
    name = input("请输入学生姓名: ")
    age = input("请输入学生年龄: ")
    address = input("请输入学生地址: ")
    stu = Student(name, age, address)
    students.append(stu)

for stu in students:
    print(f"学生姓名: {stu.name}, 年龄: {stu.age}, 地址: {stu.address}")
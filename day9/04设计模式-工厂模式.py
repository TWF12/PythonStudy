# 工厂模式, 用于创建对象的设计模式, 定义一个工厂类, 通过它的实列化对象调用方法来创建对象, 使得创建对象有一个统一的接口
# 优点: 便于维护, 统一管理, 扩展性强

class Factory:
    def get_person(self, person_type):
        if person_type == "Student":
            return Student()
        elif person_type == "Teacher":
            return Teacher()
        elif person_type == "Worker":
            return Worker()
        else:
            return None


class Student:
    pass


class Teacher:
    pass


class Worker:
    pass

factory = Factory()

stu = factory.get_person("Student")
teacher = factory.get_person("Teacher")
worker = factory.get_person("Worker")

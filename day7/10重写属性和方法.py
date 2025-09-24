class Phone:
    IMEI = None
    producer = "HM"

    def call_by_5g(self):
        print("使用5g通话")

# 重写父类的属性和方法
class Myphone(Phone):
    producer = "itcast"

    def call_by_5g(self):
        print("开启单核模式")
        print("使用5g通话")
        # 子类中可以使用父类中的属性和方法
        # print("父类的厂商是%s" % Phone.producer)
        # Phone.call_by_5g(self) #必须加上self
        print(f"父类的厂商是{super().producer}")
        super().call_by_5g()

myphone = Myphone()
print(myphone.producer)
myphone.call_by_5g()
class Phone:
    # 私有成员变量
    __current_voltage = 0.5

    # 私有成员方法
    def __keep_single_core(self):
        print("CPU以单核模式运行")

    def call_by_5g(self):
        if(self.__current_voltage >= 1):
            print("5g通话已开启")
        else:
            self.__keep_single_core()
            print("电量不足, 无法开启5g通话")

phone = Phone()
phone.call_by_5g()
# print(phone.__current_voltage)
# phone.__keep_single_core()
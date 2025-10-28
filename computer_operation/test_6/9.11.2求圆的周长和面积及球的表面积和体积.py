import math


class MyMath:
    @staticmethod
    def get_circumference(r):
        return 2 * math.pi * r
    @staticmethod
    def get_area(r):
        return math.pi * r ** 2
    @staticmethod
    def get_surface_area(r):
        return 4 * math.pi * r ** 2
    @staticmethod
    def get_volume(r):
        return 4 / 3 * math.pi * r ** 3

r = float(input("请输入半径: "))

print(f"圆的周长 = {MyMath.get_circumference(r): .2f}")
print(f"圆的面积 = {MyMath.get_area(r): .2f}")
print(f"球的表面积 = {MyMath.get_surface_area(r): .2f}")
print(f"球的体积 = {MyMath.get_volume(r): .2f}")
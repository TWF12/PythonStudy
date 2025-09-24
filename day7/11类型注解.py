# 方法一
var_1: int = 3
var_2: str = 'itacast'
var_3: bool = True


class Student:
    pass


stu: Student = Student()
# 方法二
var_4 = False  # type: bool
var_5 = 3.14  # type: float
my_list = [3, 1213, True]  # type: list[int]
my_tuple = (3, '123', True)  # type: tuple[int, str, bool]
my_dict = {"name": 20}  # type: dict[str, int]

# 函数返回值和参数类型注解
def func(expt1: int, expt2: int) -> int:
    return expt1 * expt2  # type: int


func(1, 2)

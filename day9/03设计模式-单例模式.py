class StrUtils:
    pass

# 非单例模式
str1 = StrUtils()
str2 = StrUtils()
print(str1 is str2)

# 单例模式
from str_utils import str_util
str3 = str_util
str4 = str_util
print(str3 is str4)




import re

s = "hello 123 word HelloWorld Hello123"
# match方法
ret = re.match("hello", s) # 从字符串开头匹配, 第一个参数是正则表达式, 第二个参数是要匹配的字符串, 匹配成功返回match对象, 否则返回None
print(ret)
print(ret.group()) # 获取匹配的字符串
print(ret.span()) # 获取匹配的字符串的起始位置和结束位置

# search方法
ret = re.search("Hello", s) # 在整个字符串中搜索第一个匹配项
print(ret)
print(ret.group()) # 获取匹配的字符串
print(ret.span()) # 获取匹配的字符串的起始位置和结束位置

# findall方法
ret = re.findall("Hello", s) # 在整个字符串中搜索所有匹配项,返回一个列表
print(ret)



# 匹配账号,只能是字母数字,长度6-10
pattern = "^[0-9a-zA-Z]{6,10}$" # ^表示字符串开头, $表示字符串结尾,注意{6,10}逗号后面不能有空格
s = "user01"
print(re.findall(pattern, s))

# 匹配qq号, 只能纯数字, 长度5-11, 不能以0开头
pattern = "^[1-9][0-9]{4,10}$"
s = "12345"
print(re.findall(pattern, s))

# 匹配邮件地址
pattern = r'^[\w-]+(?:\.[\w-]+)*@(?:qq|163|gmail)(?:\.[\w-]+)+$'
s = "2192074454@qq.com"
print(re.findall(pattern, s))


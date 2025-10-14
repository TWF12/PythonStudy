s = input("输入字符串: ")
# 方法一
if s == s[::-1]:
    print(f"方法一: {s}是回文字符串")

# 方法二
s_reverse_list = list(reversed(s))
if list(s) == s_reverse_list:
    print(f"方法二: {s}是回文字符串")

# 方法三
if s == "".join(reversed(s)):
    print(f"方法三: {s}是回文字符串")

# 方法四
flag = True
for i, e in enumerate(s):
    if e != s[len(s) - i - 1]:
        flag = False
        break
if flag:
    print(f"方法四: {s}是回文字符串")


# 方法五
def check(s: str) -> bool:
    left, right = 0, len(s) - 1
    if left >= right:
        return True
    if s[left] != s[right]:
        return False
    else:
        return check(s[left + 1:right])


if check(s):
    print(f"方法五: {s}是回文字符串")

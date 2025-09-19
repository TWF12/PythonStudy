def str_reverse(s):
    """
    字符串反转
    反转字符串可以使用切片的方式, 步长为-1
    :param s: 原字符串
    :return: 返回值反转后的字符串
    """
    return s[::-1]


def substr(s, x, y):
    """
    字符串切片
    切片字符串可以使用切片的方式, s[x:y], 包含起始索引x, 不包含结束索引y
    :param s: 原字符串
    :param x: 起始索引
    :param y: 结束索引
    :return: 返回值切片后的字符串
    """
    return s[x:y]

if __name__ == "__main__":
    # 测试代码
    print(str_reverse("黑马程序员"))
    print(substr("黑马程序员", 1, 3))


def print_file_info(file_name):
    """
    读取并打印文件内容
    :param file_name: 文件路径
    :return: 返回值为空
    """""
    f = None
    try:
        f = open(file_name, 'r', encoding='utf-8')
        content = f.read()
        print(f"文件名: {file_name}")
        print(f"文件内容:\n{content}")
    except FileNotFoundError:
        print(f"文件 {file_name} 未找到.")
    except Exception as e:
        print(f"读取文件 {file_name} 时出错: {e}")
    finally:
        if f: # 如果f不为None, 则关闭文件
            f.close()

def append_to_file(file_name, data):
    """
    追加内容到文件
    以追加模式打开文件, 如果文件不存在则创建新文件, 并将data写入文件末尾
    追加内容后会自动换行
    :param file_name: 文件路径
    :param data: 要写入的内容
    :return: 无返回值
    """
    f = None
    try:
        f = open(file_name, 'a', encoding='utf-8')
        f.write(data + '\n')
        print(f"已向文件 {file_name} 追加内容.")
    except Exception as e:
        print(f"写入文件 {file_name} 时出错: {e}")
    finally:
        f.close()

if __name__ == "__main__":
    # 测试代码
    print_file_info("D:/PythonStudy/day5/test.txt")
    append_to_file("D:/PythonStudy/day5/test.txt", "这是追加的一行内容.")
    print_file_info("D:/PythonStudy/day5/test.txt")
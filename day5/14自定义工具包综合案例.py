import my_utils.str_util
from my_utils import file_util

print(my_utils.str_util.str_reverse("黑马程序员"))
print(my_utils.str_util.substr("黑马程序员", 1, 3))

file_util.print_file_info("test.txt")
file_util.append_to_file("test.txt", "这是追加的一行内容.")
file_util.print_file_info("test.txt")


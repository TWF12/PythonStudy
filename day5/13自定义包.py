# import my_package.my_moudle_1
# import my_package.my_moudle_2

# my_package.my_moudle_1.info_print_1()
# my_package.my_moudle_2.info_print_2()

print("------------------")

# from my_package import my_moudle_1
# from my_package import my_moudle_2

# my_moudle_1.info_print_1()
# my_moudle_2.info_print_2()


# from my_package.my_moudle_1 import info_print_1
# from my_package.my_moudle_2 import info_print_2
#
# info_print_1()
# info_print_2()


from my_package import *
my_moudle_1.info_print_1()
my_moudle_2.info_print_2()
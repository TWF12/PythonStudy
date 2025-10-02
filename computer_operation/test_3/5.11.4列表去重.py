def remove_duplicates(iterable):
    iterable = set(iterable)
    return list(iterable)

my_list = [1, 2, 3, 4, 5, 5, 6, 2, 3, 7, 7, 8, 8, 9, 10]
print(f"去重前: {my_list}")
list_remove_duplicates = remove_duplicates(my_list)
print(f"去重后: {list_remove_duplicates}")
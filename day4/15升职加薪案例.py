# 定义一个员工工资字典
employees_dict = {
    "王力宏": {
        "部门": "科技部",
        "工资": 3000,
        "级别": 1
    },
    "张学友": {
        "部门": "市场部",
        "工资": 5000,
        "级别": 2
    },
    "刘德华": {
        "部门": "人事部",
        "工资": 4000,
        "级别": 1
    }
}

for key in employees_dict:
    if employees_dict[key]["级别"] == 1:
        employees_dict[key]["级别"] += 1
        employees_dict[key]["工资"] += 1000

print(employees_dict)


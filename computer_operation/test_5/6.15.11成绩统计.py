# 存储每个学生学号及对应成绩到字典中
stu_dict = {}
with open("class_score.txt", "r", encoding="utf-8") as f:
    for line in f:
        stu_id = line.split(" ")[0]
        score_chinese = float(line.split(" ")[1])
        score_math = float(line.split(" ")[2])
        stu_dict[stu_id] = (score_chinese, score_math)

# 分别计算语文和数学的平均分,保留1位小数
total_chinese = 0
total_math = 0
for scores in stu_dict.values():
    total_chinese += scores[0]
    total_math += scores[1]
avg_chinese = round(total_chinese / len(stu_dict), 1)
avg_math = round(total_math / len(stu_dict), 1)
print(f"全班语文成绩的平均分为{avg_chinese} ,数学成绩的平均分为{avg_math}")

# 输出两门课都不及格学生的学号和成绩
print("两门课都不及格的学生信息如下:")
for stu_id in stu_dict:
    score_chinese = stu_dict[stu_id][0]
    score_math = stu_dict[stu_id][1]
    if score_chinese < 60 and score_math < 60:
        print(stu_id, score_chinese, score_math)

# 输出两门课平均分>=90的学生的学号,语文成绩, 数学成绩, 平均成绩
print("两门课成绩的平均分在90分以上的学生信息如下:")
for stu_id in stu_dict:
    score_chinese = stu_dict[stu_id][0]
    score_math = stu_dict[stu_id][1]
    avg_chinese_math = (score_chinese + score_math) / 2
    if avg_chinese_math >= 90:
        print(stu_id, score_chinese, score_math, avg_chinese_math)

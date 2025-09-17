f1 = open("bill.txt","r",encoding="utf-8")
f2 = open("bill.txt.bak","w",encoding="utf-8")


# 读取文件内容到bill.txt.bak文件中备份(要求标志位测试的丢弃)
for line in f1:
    if "测式" in line:
        continue
    f2.write(line)

f1.close()
f2.close()
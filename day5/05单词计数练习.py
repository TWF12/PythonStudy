f = open("word.txt", "r", encoding="utf-8")
text = f.read()
# words = text.split() # 按空白字符分割成单词列表
# itheima_count = words.count("itheima") # 统计单词 "itheima" 出现的次数
# print("单词 'itheima' 出现的次数:", itheima_count)

# itheima_count = text.count("itheima")  # 统计子字符串 "itheima" 出现的次数
# print("子字符串 'itheima' 出现的次数:", itheima_count)

itheima_count = 0
f.seek(0)  # 将文件指针移动到文件开头
for line in f:
    words = line.split()  # 按空白字符分割成单词列表
    print(words)
    itheima_count += words.count("itheima")  # 统计单词 "itheima" 出现的次数
print("单词 'itheima' 出现的次数:", itheima_count)

f.close()

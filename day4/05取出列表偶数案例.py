mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
newlist1 = []
newlist2 = []

i = 0
while i < len(mylist):
    if mylist[i] % 2 == 0:
        newlist1.append(mylist[i])
    i += 1
print("newlist:", newlist1)

for item in mylist:
    if item % 2 == 0:
        newlist2.append(item)
print("newlist2:", newlist2)
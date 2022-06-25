list1 = [1, 5, 10, 12, 16, 20]
list2 = [1, 2, 10, 13, 16]
list3=[]
for i in list1:
    if i not in list2:
        list3.append(i)
for j in list2:
    if j not in list3:
        list3.append(j)
        list3.sort()
print(list3)
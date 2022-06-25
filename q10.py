big_list = [[1,2,3], [5,8,9], [4,3,77,521,31,311]]
counter1 = 0
while counter1 < len(big_list):
    small_list_length = len(big r_list[counter1])
    counter2 = 0
    while counter2 < small_list_length:
        print (big_list[counter1][counter2]) 
        counter2 = counter2 + 1
    counter1 = counter1 + 1                                                                                                           
    print ('-----')

marks = [[45, 21, 42, 63], [12, 42, 42, 53], [42, 90, 78, 13], [94, 89, 78, 76], [87, 55, 98, 99]]
list2=[]
def get_max(marks):
    for i in marks:
        if type(i)==list:
            get_max(i)
        else:
            list2.append(i)
    return max(list2)
marks = [[45, 21, 42, 63], [12, 42, 42, 53], [42, 90, 78, 13], [94, 89, 78, 76], [87, 55, 98, 99]]
print(get_max(marks))



a=[[45, 21, 42, 63], [12, 42, 42, 53], [42, 90, 78, 13], [94, 89, 78, 76], [87, 55, 98, 99]]
n=len(a)
i=0
max=a[0]
while i<n:
    if type(a[i]) is list:
        num=a[i]
        if num>max:
            max=num
            j=0
            m=max(a[i])
            while j<m:
                print(i,j,a[i][j],max)
                j=j+1
    else:
        print(i,a[i])
    i=i+1
print(max)


list1=[[45, 21, 42, 63], [12, 42, 42, 53], [42, 90, 78, 13], [94, 89, 78, 76], [87, 55, 98, 99]]
list2=[]
list3=[]
for i in list1:
    if i not in list2:
        list3.append(i)
for j in list2:
    if j not in list3:
        list3.append(j)
        list3.sort()
print("list3=",list3)

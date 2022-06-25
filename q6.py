data=[10,20,30,40,40,30,20,10,0,90,70,]
def remove_duplicates(duplist):
    noduplist=[]
    for element in duplist:
        if element not in noduplist:
            noduplist.append(element)
    return noduplist
print(remove_duplicates(data))


string_list = ["Rishabh", "Rishabh", "Abhishek", "Rishabh", "Divyashish", "Divyashish"]
new=[]
for element in string_list :
    if element not in new:
        new.append(element)
print(new)


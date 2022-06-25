n=int(input("enter the number"))
fact=1
while(n>=2):
    fact=fact*n
    n-=1
print("factorial:",fact)

n=int(input("enter the number"))
result=1
for i in range(n,0,-1):
    result=result*i
print("facorial of",n,"is",result)
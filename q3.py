


password=input("enter the password:")
if (len(password)>6 and len(password)<16 )and  ("2" or "8"  in password) and ("A" or "Z" in password)  and ("$"  in password):
    print("valid password")
else:
    print("password denied")
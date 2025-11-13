a=b=c=0
for i in range(1,11):
    a=int(input("enter the number1"))
    b=int(input("enter the number2"))
    if b==0:
        print("misssion abort")
        break
    else:
        c=a/b
    print(c)
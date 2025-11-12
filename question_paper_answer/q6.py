inp=input("enter the string")
count=0
sum=0
avg=0
a='1234567890'
for i in inp:
    if i in a:
        count=count+1
        sum=sum+int(i)
avg=sum/count
print(sum,'\n',avg)
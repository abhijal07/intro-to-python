inp=input("enter the string:")
count=0
for i in inp:
    if i in '1,2,3,4,5,6,7,8,9,0':
        count=count+1
print(count)
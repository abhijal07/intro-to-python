n=list(eval(input("enter the elements")))
count=0
m=int(input("enter the element to be checked"))
for i in n:
    if i==m:
        count+=1
print("the element occurs in the list",count,' times')

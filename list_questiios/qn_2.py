x=list(eval(input("enter the list elements")))
y=[]
for i in range(len(x)-1,-1,-1):
   y.append(x[i])
print(y)
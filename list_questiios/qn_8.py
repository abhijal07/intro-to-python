n=input("enter the list elements").split()
m=input("enter the 2nd list elements").split()
combined=[]
for i in n:
    combined.append(i)
    for j in m:
        combined.append(j)
        break
print(combined)
l=[]
d={}
l=(input("enter the list values:")).split(',')
print(l)
for i in l:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
print(d)
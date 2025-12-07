d={}
n=input("enter the string:")
lst=n.split(',')
for i in lst:
    v,j=i.split(':')
    d[v]=j
print(d)
#we have to convert a list of tuples into a dictionary
n=int(input("enter the number of tuples:"))
l=[]
d={}
for i in range(n):
    tup=tuple(input("enter the tuple values:").split(','))
    l.append(tup)
for i in l:
    v,k=i
    d[v]=int(k)
print(d)

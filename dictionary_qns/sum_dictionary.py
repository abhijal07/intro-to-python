d={}
sum=0
key=input("enter the keys:").split(',')
value=list(map(int,input("enter the values:").split(',')))
for i in range(len(key)):
    d[key[i]]=value[i]
    sum+=d[key[i]]
print(sum)

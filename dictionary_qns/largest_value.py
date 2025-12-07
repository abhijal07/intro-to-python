#we have to find the largest key and the value at that position in the dictionary
d={}
key=input("enter the keys:").split(',')
value=list(map(int,input("enter the values:").split(',')))
for i in range(len(key)):
    d[key[i]]=value[i]
large=max(d)
print(large,d[large])
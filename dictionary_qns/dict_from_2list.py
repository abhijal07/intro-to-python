#creating a dictionary from 2 list
# key=[]
# value=[]
d={}
key=input("enter the keys:").split(',')
value=input("enter the values:").split(',')
for i in range(len(key)):
    if value[i].isdigit():
        d[key[i]]=int(value[i])
    else:
        d[key[i]]=value[i]
print(d)
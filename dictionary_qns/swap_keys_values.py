#create a dictionary and swap the keys and values
d1={}
d2={}
key=input("enter the keys:").split(',')
value=input("enter the values:").split(',')
for i in range(len(key)):
    if value[i].isdigit():
        d1[key[i]]=int(value[i])
    else:
        d1[key[i]]=value[i]
for i,j in d1.items():
    d2[j]=i
print(d2)
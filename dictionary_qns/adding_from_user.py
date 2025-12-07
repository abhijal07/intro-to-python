d={'a':2,'b':3,'c':4}
n=input("enter the key to be add")
m=input("enter the value to be added:")
if m.isdigit():
    d[n]=int(m)
else:
    d[n]=m
print(d)
inp=input("enter a string:")
for i in inp:
    if i.isalnum():
        print(i,end='')
    else:
        print(i.replace(i,'#'),end='')
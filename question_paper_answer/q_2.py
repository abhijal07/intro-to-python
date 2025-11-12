n=int(input("enter the limit:"))
flag=True
for i in range(2,n+1):
    for j in range(2,i):
        if i%j==0:
            flag=False
            break
        else:
            flag=True
    if flag==True:
        print(i)
    

            
      


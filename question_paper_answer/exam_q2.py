num=int(input("enter the no of users"))
i=1
count=count1=count2=count3=count4=0
while i<=num:
    i+=1
    n=int(input("enter the month number"))
    if n>=3 and n<=4:
       # print("Wheat")
       count+=1
    if n>=9 and n<=10:
       # print("Rice")
       count1+=1
    if n>=10 and n<=11:
       # print("Soybean")
       count2+=1
    if n>=5 and n<=6:
        #print("watermelon")
        count3+=1
    if n>=2 and n<=3:
        #print("Onion")
        count4+=1
    else:
        print("invalid month")
print("wheat",count)
print("rice",count1)
print("Soybean",count2)
print("Watermelon",count3)
print("Onion",count4)



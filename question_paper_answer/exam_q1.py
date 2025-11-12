n=int(input("enter the number of temperatures"))
i=1
count,count1,count2,count3,count4=0,0,0,0,0
while i<=n:
    temp=int(input("enter the temperature"))
    i+=1
    if temp>=60:
       # print("hyperthermophile")
       count+=1
    if temp>=45 and temp<=122:
       # print("Thermophile")
       count1+=1
    if temp>=20 and temp<=45:
       # print("Mesophile")
       count2+=1
    if (temp==0) or (temp>=20 and temp<=45):
       # print("Psychotrops")
       count3+=1
    if temp>=-15 and temp<=10:
        #print("Psychophile")
        count4+=1
    if temp<-15:
        print('out of range')
print("hyperthermophile",count,'')
print("Thermopihile",count1)
print("mesophile",count2)
print("psychotrops",count3)
print("psychophile",count4)

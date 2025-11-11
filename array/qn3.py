#to count the number of even and odd
import array as arr
ar=[]
n=int(input("enter the no of array elements"))
for i in range(n):
    a=int(input("enter the array elements"))
    ar.append(a)
    a=arr.array('i',ar)
count1=0
count2=0
for i in a:
    if i%2==0:
        count1+=1
    else:
        count2+=1
print(count1,count2)       
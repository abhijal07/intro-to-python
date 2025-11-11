#to find the highest product from a given array
import array as arr
ar=[]
n=int(input("enter the no of array elemnts"))
for i in range(n):
    a=int(input("enter the array elements"))
    ar.append(a)
    a=arr.array('i',ar)
max=0
for i in a:
    if i>max:
        max=i
a.remove(max)
max2=0
for i in a:
    if i>max2:
        max2=i
print(max*max2)
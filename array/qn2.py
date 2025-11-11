##to find the largest and smallest without using the min() and max()
import array as arr
ar=[]
inp=int(input("enter the number of array elemnts"))
for i in range(0,inp):
    n=int(input("enter the array elements"))
    ar.append(n)
a=arr.array('i',ar)
max=0
min=a[0]
for i in ar:
    if i>max:
        max=i
    if i<min:
        min=i
print(max,min)
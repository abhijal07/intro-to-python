#to remove the duplicate elements from the array and return a new array
'''import array as arr
ar=[]
n=int(input("enter the no of array elements"))
for i in range(n):
    a=int(input("enter the array elements:"))
    ar.append(a)
a=arr.array('i',ar)
print("old array",a)
z=[]
for i in a:
    if i not in z:
        z.append(i)
z=arr.array('i',z)
print(z)'''

#same with string
import array as arr
ar=[]
n=int(input("enter the no of array elements"))
for i in range(n):
    a=input("enter the values:")
    ar.append(a)
print("og array",ar)
new=[]
for i in ar:
    if i not in new:
        new.append(i)
print(new)
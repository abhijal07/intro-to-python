#to find the sum of all elements in an array
import array as arr
ar=[]
n=int(input("enter the no of elements"))
for i in range(n):
    a=int(input(f"enter the array elements{i+1}:"))
    ar.append(a)
    a=arr.array('i',ar)
print(sum(a))
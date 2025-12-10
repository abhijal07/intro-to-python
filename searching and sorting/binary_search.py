#binary search to search an already sorted list
def binary(lst,n):
    lower=0
    upper=len(lst)-1
    while lower<=upper:
        mid=(lower+upper)//2
        if lst[mid]==n:
            return mid
        elif lst[mid]<n:
            lower=mid+1
        else:
            upper=mid-1
    return -1
arr=[]
a=int(input("enter the number of elements:"))
for i in range(a):
    b=int(input("enter the values:"))
    arr.append(b)
n=int(input("enter the number to be searched:"))
print(binary(arr,n))
pos=-1
def linear(lst,n):
    for i in range(len(lst)):
        if lst[i]==n:
            return i
    return pos
lst=[1,3,5,7,9,2,4,6,8]
n=int(input("enter the number to be searched."))
result=linear(lst,n)
if result!=pos:
    print("the element is found at",result)
else:
    print("elements not found")
def bubble(lst):
    swapped=False
    for i in range(len(lst)-1,0,-1):
        for j in range(i):
            if lst[j]>lst[j+1]:
                swapped=True
                lst[j],lst[j+1]=lst[j+1],lst[j]
        if not swapped:
            break
    return lst
lst=[64, 34, 25, 12, 22, 11, 90]
result=bubble(lst)
print(result)

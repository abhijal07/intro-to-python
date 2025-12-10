# #insertion sorting technique
# def insertion(lst):
#     for i in range(1,len(lst)):
#         j=i
#         while lst[j-1]>lst[j] and j>0:
#             lst[j-1],lst[j]=lst[j],lst[j-1]
#             j-=1
#     return lst
# lst=[12, 11, 13, 5, 6]
# result=insertion(lst)
# print(result)

















def insertion(lst):
    for i in range(len(lst)):
        j=i
        while lst[j-1]>lst[j] and j>0:
            lst[j-1],lst[j]=lst[j],lst[j-1]
            j-=1
    return lst
lst=[12, 11, 13, 5, 6]
result=insertion(lst)
print(result)



nums=[1,2,3,4,5,6]
names=['navin','kevin','awin']
mil=[nums,names]
print(mil)
nums.append(77)#to insert an element an the end of the string
nums.insert(2,76)# to insert an element in between the list with specified index value(here as 2)
nums.remove(3)#to remove an element from the list
nums.pop(0)#to delete an element from the list with specified index number
print(min(nums))
print(max(nums))
print(sum(nums))
print(nums,min,max,sum)
thislist=['apple','banana','cherry']
thislist[1]='blackcurrant'
print(thislist)#it replace banana with balckcurrant
tropical=['mango','pineapple','papaya']
thislist.extend(tropical)#to add two list
print(thislist)
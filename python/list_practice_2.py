fruits=['apple','banana','cherry','kiwi','mango']
newlist=[x for x in fruits if 'a'in x]
print(newlist)

#or
fruits=['apple','banana','cherry','kiwi','mango']
newlist=[]
for i in fruits:
    if 'a' in i:
        newlist.append(i)
print(newlist)
# this is called list comprehension where you can create a new list from an existing list
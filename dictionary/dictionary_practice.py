#create a dictionary to display the participants and their wins
n=int(input("enter the number of participants"))
dict={}
for i in range(n):
    key=input("enter the name:")
    value=int(input("enter the no of wins:"))
    dict[key]=value
print(dict)
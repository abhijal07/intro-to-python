#repeatedly input numbers until the user type done and print the sum
sum=0
n=input("enter a number or done to stop")
while n!='done':
    m=int(n)
    sum=sum+m
    n=(input("enter the number or done"))
print(sum)
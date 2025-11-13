def summ(x,sum):
        sum+=x
        return sum
num=int(input("enter the number:"))
sum=0
for x in range(num):
        n=int(input(f"enter the numbers{x+1}"))
        sum=summ(n,sum)
print((sum))
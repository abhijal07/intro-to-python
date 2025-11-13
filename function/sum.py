def sum(x,result):
    result=result+x
    return result
result=0
num=int(input("enter the no of digits."))
for x in range(num):
    n=int(input(f"enter the numbers{x+1}:"))
    result=sum(n,result)
print(result)
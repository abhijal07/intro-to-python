n=input("enter the string")
result=''
for i in n:
    if i in 'Aa':
        result+='4'
    elif i in 'Ee':
        result+='3'
    elif i in 'iI':
        result+='1'
    elif i in 'Oo':
        result+='0'
    elif i in 'Uu':
        result+='8'
    else:
        result+=i
print(result)
x=len(result)
print(x)

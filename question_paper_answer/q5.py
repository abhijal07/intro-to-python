inp=input("enter the string:")
inp1=inp[-1::-1]
if inp1==inp:
    print("entered string is a palindrome.")
else:
    print("not a palindrome")
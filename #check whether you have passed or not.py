#check whether you have passed or not
m=int(input("Enter the marks:"))
pass_mark=40
total_marks=100
if m>total_marks:
    print("invalid marks")
if m<pass_mark:
    print("You have failed the exam.")
else :
    print("You have passsed the exam")
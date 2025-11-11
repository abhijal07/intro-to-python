emp={"name":"rehan","age":20,"job":"jobless"}
a=input("enter the value to be checked")
if a in emp.values():
    for i in emp:
        if emp[i]==a:
            print("the key of given value is",i)
            break
    else:
        print("given value does not exist in dictionary")
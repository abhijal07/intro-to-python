temp=int(input("enter the temperature"))
if temp>=60:
     print("hyperthermophile")
elif temp>=45 and temp<=122:
    print("Thermophile")
elif temp>=20 and temp<=45:   
    print("Mesophile")
elif (temp==0) or (temp>=20 and temp<=45):
    print("Psychotrops")
elif temp>=-15 and temp<=10:
    print("Psychophile")
else:
    print("invalid temperature")




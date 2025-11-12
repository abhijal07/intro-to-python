count1=0 #onion 
count2=0 #rice
count3=0 #soybean
count4=0 #watermelon
y=int(input('months to enter:'))
for i in range(y):
 x=int(input('enter the months no:'))
 if x in range(3,5):
    count1+=1
 if x in range(9,11):
    count2+=1
 if x in range(10,12):
    count3+=1
 if x in range(5,7):
    count4+=1
 if x==12:
    print('No crops')
print('onion-',count1,'wheat-',count1,'rice-', count2 ,'soybean-',count3,'watermelon-',count4 )
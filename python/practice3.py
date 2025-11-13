for i in range(1,10):
    for j in range(1,10):
        prod=i*j
        if prod<10:
            print('',prod,'',end='')
        else:
            print(prod,'',end='')
    print()
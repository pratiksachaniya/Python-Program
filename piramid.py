no = int(input('Enter Number: '))
for i in range(1,no+1):
    for l in range(no-i):
        print(" ",end='')
    for j in range(i):
        print('* ',end='')
    print()
    

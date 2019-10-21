def IsPrime(no):
    for i in range(2,no):
        if no % i == 0:
            return 0
    else:
        return 1
no = int(input("Enter Range:"))
for i in range(3,no+1):
    if IsPrime(i):
        print(i,end=',')
        

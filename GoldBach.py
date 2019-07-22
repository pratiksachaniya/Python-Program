def isPrime(n):
    for i in range(2,n):
        if n%i == 0:
            return 0
    return 1
no = int(input("Enter Number: "))
for i in range(3,no):
    if isPrime(i) == 1:
        for l in range(i,no):
            if isPrime(l) == 1:
                if no == (i+l):
                    print(i,"+",l,"=",no)
                    
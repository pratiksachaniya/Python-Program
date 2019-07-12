def isPrime(n):
    for i in range(2,n):
        if no%i == 0:
            return 0
    return 1

no = int(input("Enter Number: "))

if isPrime(no)== 0:
    print("Number Is Not Prime")
else:
    print("Number Is Prime")
    

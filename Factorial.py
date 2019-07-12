def fact(no):
    fact = 1
    for i in range(1,no+1):
        fact *= i
    return fact

no = int(input("Enter Number: "))
print("Factorial Is ",fact(no))

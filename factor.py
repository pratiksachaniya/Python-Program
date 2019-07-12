def printFact(n):
    for i in range(1,n):
        if n%i == 0:
            print(i,end=",")

no = int(input("Enter Number: "))
printFact(no)

def printFibo(n):
    n1 = 0
    n2 = 1
    print(n1,n2,sep=",",end=",")
    for i in range(n-2):
        n3 = n1 + n2
        print(n3,end=",")
        n1,n2 = n2,n3

n = int(input("Enter Number: "))
printFibo(n)

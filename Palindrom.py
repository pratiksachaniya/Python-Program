def pali(no):
    rev = 0
    ori = no
    while no!=0:
        rev = rev*10
        rev += no%10
        no = int(no/10)
    if ori==rev:
        print("Number is palindrom")
    else:
        print("Number is not palindrom")

no = int(input("Enter Number: "))
pali(no)            
            
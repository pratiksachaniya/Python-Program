def labNum(no):
    for i in range(2,no):
        if no%i == 0:
            if no%(i*i) == 0:
                print("True(",i," is a prime divisor of ",no,", and ",i,"x",i,"=",(i*i)," is also a divisor of ",no,")")
                return
    print("Not a lab number")
    
no = int(input("Enter Number:"))
labNum(no)
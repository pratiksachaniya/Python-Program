class Bank:
    def __init__(self,name,bal=0):
        self.name = name
        self.bal = bal
    def deposit(self,amnt):
        self.bal += amnt
    def withdrawal(self,amnt):
        self.bal -= amnt

    def show(self):
        print("Name:",self.name)
        print("Bal :",self.bal)

cus1 = Bank("Pratik")
cus1.deposit(5000)
cus1.withdrawal(500)
cus1.show()

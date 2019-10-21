class Student:
    Year = "FY"
    def __init__(self,div,no):
        self.div = div
        self.no = no
    def display(self):
        print("Year:",self.Year)
        print("Division:",self.div)
        print("Roll:",self.no)
s1 = Student("B",41)
s1.display()

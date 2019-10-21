class Student:
    def __init__(self,name,age,marks):
        self.name = name
        self.age = age
        self.marks = marks
    def display(self):
        print("Name :",self.name)
        print("Age  :",self.age)
        print("Marks:",self.marks)
S1 = Student("Pratik",19,80)
S1.display()

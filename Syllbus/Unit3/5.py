class Student:
    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
    def getResult(stu):
        return (stu.m1+stu.m2+stu.m3)/3
        
s1 = Student(60,70,80)
result = Student.getResult(s1)
print("Result Is %.2f Per." % result)

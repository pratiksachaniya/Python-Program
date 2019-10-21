class Emp:
    def __init__(self,name,sal):
        self.name = name
        self.sal = sal

class Myclass(Emp):
    def __init__(self,name,sal):
        super().__init__(name,sal)

    def show(self):
        print("Name:",self.name)
        print("Sal :",self.sal)

c1 = Myclass("Pratik",50000)
c1.show()

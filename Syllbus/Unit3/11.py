class A:
    def show(self):
        print("Class A")
    def __init__(self):
        print("class A")

class B(A):
    def show(self):
        print("Class B")
    def __init__(self):
        print("Class B")

b1 = B()
b1.show()

class A:
    def show(self):
        print("Class A")

class B(A):
    def show(self):
        print("Class B")

b1 = B()
b1.show()

class A:
    pass
class B(A):
    def __init__(self):
        print("Class B Called")
class C(A):
    def __init__(self):
        print("Class C Called")
B()
C()

class A:
    pass
class B:
    pass
class C(A,B):
    def __init__(self):
        print("Class C Called")
C()

class A:
    def __init__(self):
        print("Class A Called")

class B:
    def __init__(self):
        print("Class B Called")
        
class C(A,B):
    def __init__(self):
        print("Class C Called")
        super().__init__()
print(C.mro())

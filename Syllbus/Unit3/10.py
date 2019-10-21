class A:
    def __init__(self=0):
        print("I Am Class A")
class B(A):
    def __init__(self):
        super().__init__()  #using super()
        A.__init__()        #without using super()
    
b1 = B()

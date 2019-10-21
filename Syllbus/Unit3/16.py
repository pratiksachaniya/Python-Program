class Area:
    def __init__(self,h=0,w=0):
        self.h = h
        self.w = w
    def show(self):
        print("H:",self.h)
        print("W:",self.w)
    def __add__(self,other):
        tmp = Area()
        tmp.h = self.h + other.h
        tmp.w = self.w + other.w
        return tmp
    
a1 = Area(10,20)
a2 = Area(30,5)
a3 = a1 + a2
a3.show()

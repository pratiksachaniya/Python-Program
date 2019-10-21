class Area:
    def __init__(self,height=0,width=0):
        self.height = height
        self.width = width

    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height

    def setHeight(self,height):
        self.height = height

    def setWidth(self,width):
        self.width = width

    def area(self):
        return self.width*self.height

A = Area()
A.setWidth(10)
A.setHeight(20)
print("Width Is ",A.getWidth())
print("Height Is ",A.getHeight())
print("Area Is ",A.area())

class A:
    def ShowA(self):
        print("Class A")
a = A()
if hasattr(a,"Show"):
    a.Show()
elif hasattr(a,"ShowA"):
    a.ShowA()
else:
    print("No Method to show")
    

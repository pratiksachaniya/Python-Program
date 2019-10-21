class IamClass:
    cnt = 0
    def __init__(self):
        IamClass.cnt += 1
        print("Class Count Is ",self.cnt)
        
o1 = IamClass()
o2 = IamClass()
o3 = IamClass()

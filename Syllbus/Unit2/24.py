def GetDict(no):
    dic = dict()
    for i in range(no):
        key = input('Key:')
        val = input('Val:')
        dic[key] = val
    return dic
def ShowDict(d):
    for i in d.items():
        print("Key:",i[0])
        print("Val:",i[1])
    
no = int(input("Enter Number:"))
d = GetDict(no)
ShowDict(d)

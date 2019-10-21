lst = [int(i) for i in input().split()]
btArray = bytearray(lst)
print('Byte Array is ')
for i in btArray:
    print(i,end=",")
btArray[0] = 255
btArray[len(btArray)-1] = 0
print('\nAfter Modify:')
for i in btArray:
    print(i,end=",")



    

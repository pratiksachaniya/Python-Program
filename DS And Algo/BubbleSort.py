from array import *
x = [int(i) for i in input().split()]
x = array('i',x)
l = len(x)

i = l-1
while i>=0:
    j = l-1
    while j>0:
        if x[j] < x[j-1]:
            x[j],x[j-1] = x[j-1],x[j]
            j -= 1
        else:
            break
    i -= 1

print(x)
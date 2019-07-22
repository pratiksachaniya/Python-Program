from array import *
x = [int(i) for i in input().split()]
x = array('i',x)
l = len(x)

for i in range(l):
    mi = i
    for j in range(i,l):
        if x[mi] > x[j]:
            mi = j
    x[mi],x[i]=x[i],x[mi]

print(x)
        

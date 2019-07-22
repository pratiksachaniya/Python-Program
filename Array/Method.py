from array import *
#Array Method
a = array('i',[10,20,30,40,50,60])
b = array('i',[70,80,90])

#print
print(a)

#append
a.append(10)
print(a)

#extend
a.extend(b)
print(a)

#index
print(a.index(70))

#count
print(a.count(10))

#insert
a.insert(1,100)
print(a)

#pop
a.pop()
print(a)

#pop(x)
a.pop(1)
print(a)

#remove(x)
a.remove(10)
print(a)

#reverse
a.reverse()
print(a)

#max
print(max(a))

#min
print(min(a))

#len
print(len(a))
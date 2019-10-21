from array import array
lst = [1,2,3,4,5]
ar1 = array('i',lst)
ar1.append(100)
ar1.insert(len(ar1)+1,70)
ar1.remove(2)
print(ar1.pop())
print(ar1)
print(ar1.index(100))
lst = ar1.tolist()
print(type(lst),lst)

lst = [10,20,30,40,50,60]
b = [70,80]
#print
print(lst)

#append
lst.append(10)
print(lst)

#extend
lst.extend(b)
print(lst)

#index
print(lst.index(70))

#count
print(lst.count(10))

#insert
lst.insert(1,100)
print(lst)

#pop
lst.pop()
print(lst)

#pop(x)
lst.pop(1)
print(lst)

#remove(x)
lst.remove(10)
print(lst)

#reverse
lst.reverse()
print(lst)

#max
print(max(lst))

#min
print(min(lst))

#len
print(len(lst))

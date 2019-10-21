lst = [int(i) for i in input().split()]
lst2 = []
for i in lst:
    if lst2.count(i) < 1:
        lst2.append(i)
print(lst2)

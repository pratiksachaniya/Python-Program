lst = [int(i) for i in input().split()]
common = []
non_common = []
for i in lst:
    if lst.count(i) > 1:
        if i not in common:
            common.append(i)
    else:
        non_common.append(i)
print('Common Elments ',common)
print('Non Common Elements ',non_common)

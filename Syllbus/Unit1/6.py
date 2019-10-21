a = 10
b = 20
print('ID of a',id(a))
print('ID of b',id(b))
if a is b:
    print('A and B store at the same address')
else:
    print('A and B store at defferent address')

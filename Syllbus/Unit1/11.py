lst = [int(i) for i in input().split()]
no = int(input('Enter Element to Find:'))
for i in lst:
    if no == i:
        print('Element Found At ',lst.index(i)+1)
        break
else:
    print('Not Found')

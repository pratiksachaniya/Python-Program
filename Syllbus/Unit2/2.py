from array import array
lst = [1,2,3,4,5]
ar1 = array('i',lst)
ar1[len(ar1)-1] = 100
for i in ar1[1:5]:
    print(i)

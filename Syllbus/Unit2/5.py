from array import array
lst = [int(i) for i in input().split()]
ar = array('i',lst)
no = int(input("Enter Element To Find"))
if ar.count(no) > 0:
    print("Found At ",ar.index(no))
else:
    print("Not Found")

def B_Search(a,val,beg,end):
    n = (beg+end)//2
    if n<0 or n>len(a)-1:
        print("Not Found")
        return
    if a[n] < val:
        B_Search(a,val,n+1,end)
    elif a[n] > val:
        B_Search(a,val,beg,end-1)
    elif a[n] == val:
        print("Found At ",n)
    else:
        print("Not Found")



a = [int(i) for i in input().split()]
no = int(input("Enter Number:"))
B_Search(a,no,0,len(a))


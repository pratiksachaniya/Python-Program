no = int(input("Enter Number: "))
lst = [0]*no
for i in range(0,no):
    lst[i] = int(input("Enter Number: "))
print("Minimum is ",min(lst))
print("Maximum is ",max(lst))
print("Length is ",len(lst))

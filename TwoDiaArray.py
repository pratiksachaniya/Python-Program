def rowSum(r):
    ans = 0
    for i in r:
        for j in i:
            ans += j
    return ans

row = int(input("Enter Rows: "))
col = int(input("Enter Columns: "))
lst = [[0]*col]*row
for i in range(row):
    for j in range(col):
        lst[i][j] = int(input("Enter Number: "))
    

print(lst)
        
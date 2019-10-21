no = int(input("Enter Number:"))
dic = dict()
for i in range(no):
    key = input('Name:')
    val = input('Run:')
    dic[key] = val
key = input("Enter Player Name:")
print("Run Is",dic[key])

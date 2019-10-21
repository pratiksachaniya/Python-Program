import os
print("Current Working Directory Is ",os.getcwd())
lst = dir(os)
print('OS Modules Methods:')
for i in lst:
    print(i)

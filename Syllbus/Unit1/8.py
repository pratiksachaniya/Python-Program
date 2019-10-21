import sys
even = 0
for i in sys.argv[1:]:
    if int(i) % 2==0:
        even += int(i)
print('Sum of Even Is ',even)

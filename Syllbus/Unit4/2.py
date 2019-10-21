try:
    no1 = int(input('Enter Number 1:'))
    no2 = int(input('Enter Number 2:'))
    print('Division of %d / %d is %f' % (no1,no2,no1/no2))
except ZeroDivisionError:
    print("Can't Divide with Zero Please Enter Diff. Value")
except ValueError:
    print("Please Enter Only Int Value")

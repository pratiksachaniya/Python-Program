while 1:
    print('1.Find Area of Circle')
    print('2.Find Area of Triangle')
    print('3.Find Area of Square and Rectangle')
    print('4.Find Simple Interest')
    print('5.Exit')
    ch = int(input('Enter Your Choice:'))
    if ch == 1:
        r = int(input('Enter Radius:'))
        print('Area of Circle is %.2f ' % (3.14*r*r))
    elif ch == 2:
        s1 = float(input('Enter Side 1:'))
        s2 = float(input('Enter Side 2:'))
        s3 = float(input('Enter Side 3:'))
        s = (s1+s2+s3)/2
        area = (s*(s-s1)*(s-s2)*(s-s3)) ** 0.5
        print('Area od Triangle is %.2f'% area)
    elif ch == 3:
        l = float(input('Enter Length:'))
        b = float(input('Enter Bredth:'))
        print('Area of Square is %.2f' % (l*l))
        print('Area of Reactangle is %.2f' % (l*b))
    elif ch == 4:
        p = int(input('Enter P:'))
        r = int(input('Enter R:'))
        n = int(input('Enter N:'))
        print('Simple Interest is ',(p*r*n)/100)
    elif ch == 5:
        exit()
    else:
        print('Invalid Input')
        input()

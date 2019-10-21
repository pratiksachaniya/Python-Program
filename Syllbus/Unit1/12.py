centi = float(input('Enter Centimeter:'))
if centi < 0:
    print('Entry is Invalid')
else:
    print('Inches: %.2f' % (centi/2.54))

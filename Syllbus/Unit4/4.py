import datetime
st = input('Enter Your DOB[DD/MM/YYYY]:')
day = int(st[:2])
month = int(st[3:5])
year = int(st[6:])
dt = datetime.datetime.now()
now = datetime.date(dt.year,dt.month,dt.day)
dob = datetime.date(year,month,day)
print('Diff is ',now-dob)

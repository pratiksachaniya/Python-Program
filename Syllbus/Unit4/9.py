import mysql.connector
con = mysql.connector.connect(host="localhost",user="root",passwd="",database="Sample_DB")
cur = con.cursor()

cur.execute("SELECT * FROM `employee`")
rows = cur.fetchall()
for row in rows:
    print("Eid:",row[0])
    print("Name:",row[1])
    print("Salary:",row[2])
    print()

no = int(input('Enter Eid  You Want to Delete'))
try:
    cur.execute("DELETE FROM `employee` WHERE `eid`=%d" % no)
    print("Record Deleted")
except:
    print("Not Deleted")
con.commit()
cur.execute("SELECT * FROM `employee`")
rows = cur.fetchall()
for row in rows:
    print("Eid:",row[0])
    print("Name:",row[1])
    print("Salary:",row[2])
    print()

con.close()

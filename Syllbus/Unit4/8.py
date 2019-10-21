import mysql.connector
con = mysql.connector.connect(host="localhost",user="root",passwd="",database="Sample_DB")
cur = con.cursor()

no = int(input('Enter Number of Row You Want to Enter'))
for i in range(no):
    name = input("Enter Name:")
    sal = int(input("Enter Salary:"))
    sql = "INSERT INTO `employee` (eid,name,sal) VALUES (null,'%s','%d')" % (name,sal)
    cur.execute(sql)
    con.commit()
cur.execute("SELECT * FROM `employee`")
rows = cur.fetchall()
for row in rows:
    print("Eid:",row[0])
    print("Name:",row[1])
    print("Salary:",row[2])
    print()
con.close()

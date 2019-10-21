import mysql.connector
con = mysql.connector.connect(host="localhost",user="root",passwd="",database="Sample_DB")
cur = con.cursor()
#Create Table
cur.execute("CREATE TABLE IF NOT EXISTS `employee` ( `eid` INT(4) PRIMARY KEY, `name` VARCHAR(20), `sal` INT(10) )")
#data Inser
#cur.execute("""INSERT INTO `employee` (eid,name,sal) VALUES (null, 'Vishal', '40000')""")
#con.commit()
cur.execute("""SELECT * FROM `employee`""")
rows = cur.fetchall()
for row in rows:
    print("Eid:",row[0])
    print("Name:",row[1])
    print("Salary:",row[2])
    print()

con.close()

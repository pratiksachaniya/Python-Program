import mysql.connector
con = mysql.connector.connect(host="localhost",user="root",passwd="",database="Sample_DB")
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS `new_employee_tbl` ( `eno` INT(4) PRIMARY KEY, `ename` CHAR(30), `gender` CHAR(1),`salary` FLOAT(5) )")
print('Table Created')
con.commit()
con.close()

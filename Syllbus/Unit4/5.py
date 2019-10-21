import mysql.connector
con = mysql.connector.connect(host="localhost",user="root",passwd="")
if con.is_connected():
    cur = con.cursor()
    try:
        cur.execute("CREATE DATABASE `Sample_DB`")
        print("Database Created")
    except:
        print("Database Exists")
else:
    print("Connection are not made")

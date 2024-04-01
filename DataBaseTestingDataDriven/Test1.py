import mysql.connector
conn =mysql.connector.connect(host='localhost',database='mydb',user='root',password='Future@981')
if conn.is_connected():
    print('connected to DB and running')
cursor =conn.cursor()
try:
    cursor.execute("insert into emp values(5,'Ragini',5000),(6,'Anu',598700)")
    conn.commit()
    print('record added')
except:


    conn.rollback()

cursor.close()
conn.close()
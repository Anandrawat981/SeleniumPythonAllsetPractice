#insert,delete,update
insert_query ="insert into emp values(10,'Sita',100000),(11,'Love',1999)"
update_query="update emp set name='Love kush' WHERE id=11 and sal=1999"
delete_query =" delete from emp where id=2"
import mysql.connector
try:
    connection1 = mysql.connector.connect(host="localhost", port=3306, user="root", password="Future@981",
                                          database="mydb")
    corsor = connection1.cursor()
    corsor.execute("select *from emp")
    for rows in corsor:
        print(rows[0],rows[1],rows[2])

    corsor.close()
    connection1.close()
except:
    print("connection broken")


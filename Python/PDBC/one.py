import mysql.connector
# from mysql import connector as myConn
mydb=mysql.connector.connect(host='localhost',
                user='root',
                password='root',
                database='learncoding'
                )

db_cursor=mydb.cursor()

retrive_data=db_cursor.execute('select *from emp')
db_select=db_cursor.fetchall()
print(db_select)
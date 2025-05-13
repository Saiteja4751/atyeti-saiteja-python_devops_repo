import mysql.connector as myConn
mydb=myConn.connect(host='localhost',
                user='root',
                password='root',
                database='learncoding'
                )

db_cursor=mydb.cursor()
db_cursor.execute('show tables')
for i in db_cursor:
    print(i)
import mysql.connector as myConn
mydb=myConn.connect(host='localhost',
                user='root',
                password='root',
                database='book_shop'
                )

db_cursor=mydb.cursor()
db_cursor.execute('create table Emp(Roll int,Ename varchar(20))')

print('Table Created!!')
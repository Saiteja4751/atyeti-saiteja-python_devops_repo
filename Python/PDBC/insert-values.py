import mysql.connector as myConn
mydb=myConn.connect(host='localhost',
                user='root',
                password='root',
                database='learncoding'
                )

db_cursor=mydb.cursor()
db_insert="insert into emp(Roll,Ename) values(%s,%s)"
db_list=[(10,'renu'),(20,'mastan'),(40,'soheb'),(50,'raja')]
db_cursor.executemany(db_insert,db_list)
mydb.commit()
print(db_cursor.rowcount,'record inserted')
import mysql.connector as myConn
mydb=myConn.connect(host='localhost',
                user='root',
                password='root'
                )
print(mydb,'connection estlablished')
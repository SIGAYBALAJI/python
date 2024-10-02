import mysql.connector
con=mysql.connector.connect(host='localhost',user='root',password='system' ,database='bookdb')
print(con)
c=con.cursor()
c.execute('create table bookdetails(name varchar(20) ,price decimal,')



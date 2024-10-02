import mysql.connector
con=mysql.connector.connect(host='localhost',user='root',password='system',database='kod')
c=con.cursor()

c.execute("delete from emp where name='shiva'")
con.commit()

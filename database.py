import mysql.connector
con=mysql.connector.connect(host='localhost',user='root',password='system')
c=con.cursor()
c.execute('create database kod')

import pymysql as mq
#Server name -> localhost
#Username -> root
#Password ->''
conn=mq.conn.__init__(("localhost","root",""))
cursorobj=conn.cursor()
try:
     db="create database school"
     cursorobj.execute(db)
     print("database created")

except:
      print("database error...")

conn.commit()
conn.close()

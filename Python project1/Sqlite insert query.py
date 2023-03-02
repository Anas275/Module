# import sqlite3
# conn = sqlite3.connect("sqlite.db")
#
# ins = '''
#       insert into student (st_id, st_name, st_class, st_email) VALUES ('5', 'HM', '10th',"hm@gmail.com")
# '''
# conn.execute(ins)
# conn.commit()
# conn.close()

#
# import sqlite3
# conn = sqlite3.connect("sqlite.db")
# data = conn.execute("SELECT * FROM student")
# for n in data:
#     print(n)
# #
#
# import sqlite3
# conn = sqlite3.connect("sqlite.db")
# data = conn.execute("SELECT * FROM student")
# print("STUDENT ID","STUDENT NAME","STUDENT CLASS","STUDENT EMAIL")
# for n in data:
#     print(n)


# import sqlite3
# conn = sqlite3.connect("sqlite.db")
# data = conn.execute("SELECT * FROM student")
# print("STUDENT ID","STUDENT NAME","STUDENT CLASS","STUDENT EMAIL")
# for n in data:
#     print(n[0],"   ", n[1],"   ",n[2],"   ",n[3])


# import sqlite3
# conn = sqlite3.connect("sqlite.db")
# data = conn.execute("SELECT * FROM student")
# print("STUDENT ID","STUDENT NAME","STUDENT CLASS","STUDENT EMAIL")
# for n in data:
#     print(n[0],"   ", n[1],"   ", n[2],"   ",n[3])



# import sqlite3
# conn = sqlite3.connect("sqlite.db")
# data = conn.execute("SELECT * FROM student")
# print("STUDENT ID","STUDENT NAME","STUDENT CLASS","STUDENT EMAIL")
# for n in data:
#     print(n[0],"   ", n[1],"   ", n[2],"   ",n[3])
#
# print("")
# print("")
# data = conn.execute("SELECT * FROM student where st_name='HM' ")
# for n in data:
#     print(n[0],"   ", n[1],"   ", n[2],"   ",n[3])



import sqlite3
conn = sqlite3.connect("sqlite.db")
data = conn.execute("SELECT * FROM student")
print("STUDENT ID","STUDENT NAME","STUDENT CLASS","STUDENT EMAIL")
for n in data:
    print(n[0],"   ", n[1],"   ", n[2],"   ",n[3])

print("")
print("")

st_name=input("Enter the student name:- ")
st_class=input("Enter the student class:- ")
data = conn.execute("SELECT * FROM student where st_name like '%"+st_name+"%' or st_class='"+st_class+"'     ")
for n in data:
    print(n[0],"   ", n[1],"   ", n[2],"   ",n[3])
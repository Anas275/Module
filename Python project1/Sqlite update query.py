import sqlite3
conn = sqlite3.connect("sqlite.db")
conn.execute('''
    update student set st_id='4' where st_id=5
    
    
    ''')
conn.commit()
conn.close()
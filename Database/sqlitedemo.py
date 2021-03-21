import sqlite3
conn = sqlite3.connect('employee.db')
cursor = conn.cursor()

# cursor.execute('''create table employee(
#                 first varchar,
#                 last varchar,
#                 age integer,
#                 pay integer
#             )''')

#cursor.execute('''insert into employee values ('prathap','madala',29,90000)''')

cursor.execute("select * from employee where last = 'madala'")

print(cursor.fetchall())

conn.commit()
conn.close()
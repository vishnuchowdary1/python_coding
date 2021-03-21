import sqlite3
import json

conn = sqlite3.connect('rosterdb.sqlite')
c = conn.cursor()

c.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Member;
DROP TABLE IF EXISTS Course;

CREATE TABLE User (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT UNIQUE
);

CREATE TABLE Course (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title  TEXT UNIQUE
);

CREATE TABLE Member (
    user_id     INTEGER,
    course_id   INTEGER,
    role        INTEGER,
    PRIMARY KEY (user_id, course_id)
);

''')

fname = input('enter file name: ')
if len(fname) < 1 : 
    fname = 'roster_data.json'

str_read = open(fname).read()
json_data = json.loads(str_read)

for data in json_data :
    name = data[0]
    title = data[1]
    role = data[2]

    print(name,title,role)

    c.execute('insert or ignore into User (name) values (?)', (name, ))
    c.execute('select id from User where name = ?', (name, ))
    user_id = c.fetchone()[0]

    c.execute('insert or ignore into Course (title) values (?)', (title, ) )
    c.execute('select id from Course where title = ?', (title, ))
    course_id = c.fetchone()[0]

    c.execute('insert or replace into Member(user_id, course_id, role) values (?,?,?)',
        (user_id, course_id, role))

    conn.commit()

c.executescript(''' SELECT User.name,Course.title, Member.role FROM 
    User JOIN Member JOIN Course 
    ON User.id = Member.user_id AND Member.course_id = Course.id
    ORDER BY User.name DESC, Course.title DESC, Member.role DESC LIMIT 2;

    SELECT 'XYZZY' || hex(User.name || Course.title || Member.role ) AS X FROM 
        User JOIN Member JOIN Course 
        ON User.id = Member.user_id AND Member.course_id = Course.id
        ORDER BY X LIMIT 1;

''')

conn.commit()
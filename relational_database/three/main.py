## this script show how to code a
## many to many relationship
## we will take a data from json
import json
import sqlite3 

## connected to the database
conn = sqlite3.connect('rosterdb.sqlite')

## make a cursor
## like  afile handler
cur = conn.cursor()

## create two database
## and make a pivot tabe
cur.executescript('''

DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Member;
DROP TABLE IF EXISTS Course;

CREATE TABLE User(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT UNIQUE
);

CREATE TABLE Course(
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        title TEXT UNIQUE
);

CREATE TABLE Memeber(
        user_id INTEGER,
        course_id INTEGER,
        role INTEGER,
        PRIMARY KEY (user_id,course_id)
    );
''')


## when you use
## PRIMARY KEY (user_id,course_id) both will be unique and 
## will have to be unique


fname = input("Enter THe Full name:  ")

if (len(fname) < 1):
    fname = 'roster_data.json'

str_data = open(fname).read()

json_data = json.loads(str_data)

##print(json_data)

for entry in json_data:
    name = entry[0]
    title = entry[1]
    role = entry[2]

    #print("  {}    {}    {}".format(name,title,role))
    cur.execute('''
    INSERT OR IGNORE INTO User (name) VALUES ( ? ) ''',(name,)
    )
    ## get the user id
    cur.execute('''
    SELECT id FROM User WHERE name = ?
    ''',(name,))
    user_id = cur.fetchone()[0]
    #print(user_id)


    cur.execute("INSERT OR IGNORE INTO Course(title) VALUES ( ? ) ",(title, ))
    cur.execute('''
    SELECT id FROM Course WHERE title = ?
    ''',(title,))
    course_id = cur.fetchone()[0]
    #print(course_id)

    cur.execute(''' INSERT OR IGNORE INTO Memeber 
    (user_id,course_id,role) VALUES ( ?, ?, ?)
    ''',(user_id,course_id,role))
conn.commit()
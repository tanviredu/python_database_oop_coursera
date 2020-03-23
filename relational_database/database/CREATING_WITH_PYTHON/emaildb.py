## importing sqlite database
import sqlite3
conn = sqlite3.connect("emaildb.sqlite")


### create the cursor
### cursor is like the computer cursor it does all the things

cur = conn.cursor()

### drop all the table

cur.execute("DROP TABLE IF EXISTS Counts")

### now make a scchema
cur.execute("CREATE TABLE Counts(email TEXT,count INTEGER)")


### Create a file 
fname = input("Enter The file name : ")

## check if it is the valid name or make a default one
## or user just press enter
if(len(fname) < 1):
    fname = "mbox_short.txt"

## make a file handles like the cursor fo the file

fh = open(fname)

for line in fh:
    ## first check if we reached at the end of the file
    if not line.startswith("From: "): continue

    ### so in the file the line shoud be like "From <email>"
    ### so we split the line and take the second part
    pieces = line.split()
    email = pieces[1]
    ## now enter into the database
    ## but first we need to find if it is already in the database
    ## if not create one and if it is then increase the count
    ## remember the "?"  and the "," after the email
    ## you have to give it to it
    cur.execute("SELECT count FROM Counts WHERE email = ? ",(email,)) 
    ### now fetch the data
    row = cur.fetchone()
    ## if there is no data
    if row is None:
        ## then insert the data
        cur.execute("INSERT INTO Counts (email,count) VALUES (?,1)",(email,))
    else:
        cur.execute("UPDATE Counts SET count = count + 1 WHERE email = ? ",(email,))
    conn.commit()


## now fetch all the data

sqlstr = "SELECT email,count FROM Counts ORDER BY count DESC LIMIT 10"

for row in cur.execute(sqlstr):
    print(str(row[0]),row[1])


cur.close()
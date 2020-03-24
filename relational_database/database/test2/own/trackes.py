####
### now if you see the xml file
### you will see there is three
## <dict>
##     <dict>
##         <dict>
## and inside this all the track information
### so we need to first parse the information

import xml.etree.ElementTree as ET 
import sqlite3

conn = sqlite3.connect('track.sqlite3')

## now create the database fro scratch

cur = conn.cursor()

cur.executescript(''' 
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Genre;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;


CREATE TABLE Artist(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT UNIQUE
);


CREATE TABLE Genre (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT UNIQUE
 



);

CREATE TABLE Album(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title TEXT UNIQUE,
    artist_id INTEGER


);


CREATE TABLE Track(
    id INTEGER  NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    rating INTEGER,
    count INTEGER,
    len INTEGER,
    title TEXT UNIQUE,
    album_id INTEGER,
    genre_id INTEGER
    -- this is the rating

);
''')

#### now we take an input of the file
fname = input("Enter The File Name :")

if len(fname) < 1:
    fname = "Library.xml"


## now we write a function for looking the data 
## from the child

def find_field(track_info,wanted_field):
    ''' track_info conrain the ell the tags of  a certain
    song and wanted fild is the filed we want  '''

    ### first we make that we dont found it
    found = False
    for tag in track_info:
        if not found:
            ## looking for wanted filed
            if (tag.tag == 'key' and tag.text == wanted_field):
                found = True 
        else:
            ## we go to the end of the tree and no more branch
            ## then we simply return the inside valye of the text inside the tag
            return tag.text 

            ### now you might be asking tag.text wans in the if statement too
            ### well in the if statement it was not at the end of the tree
            ### now it is on the final branch
            ## and it will seach for every xml
            ## of a specfic track go to the last branch and return the value


data = ET.parse(fname)
all_tracks_data = data.findall('dict/dict/dict')
#print(all)

for track in all_tracks_data:
    # print("-----------------------")
    # print(find_field(track,"Name"))
    # print(find_field(track,"Artist"))
    # print(find_field(track,"Album"))
    # print(find_field(track,"Play Count"))
    # print(find_field(track,"Rating"))
    # print(find_field(track,"Total Time"))
    # print("----------------------------")
    name = find_field(track,"Name")
    artist = find_field(track,"Artist")
    album  = find_field(track,"Album")
    genre  = find_field(track,"Genre")
    count = find_field(track,"Play Count")
    rating = find_field(track,"Rating")
    length = find_field(track,"Total Time")

    # insert artist
    if artist:
        cur.execute("INSERT OR IGNORE INTO Artist (name) VALUES ( ? )",(artist,))
        ## get the id
        cur.execute("SELECT id FROM Artist WHERE name = ? ",(artist, ))
        artist_id = cur.fetchone()[0]
    if genre:
        cur.execute('''INSERT OR IGNORE INTO Genre (name) VALUES ( ? )''', ( genre, ) )
        cur.execute('SELECT id FROM Genre WHERE name = ? ', (genre, ))
        genre_id = cur.fetchone()[0]
    if album:
        cur.execute('''INSERT OR IGNORE INTO Album (title, artist_id) VALUES ( ?, ? )''', ( album, artist_id ) )
        cur.execute('SELECT id FROM Album WHERE title = ? ', (album, ))
        album_id = cur.fetchone()[0]

    if name and length and rating:
        cur.execute('''INSERT OR REPLACE INTO Track
        (title, album_id, genre_id, len, rating, count) 
        VALUES ( ?, ?, ?, ?, ?, ? )''', ( name, album_id, genre_id, length, rating, count ) )
    conn.commit()
        



sql = "select Track.title,Artist.name,Album.title,Genre.name From Track join Artist join Album join Genre WHERE Track.genre_id = Genre.id and Track.album_id = Album.id and Album.artist_id = Artist.id"
print()

for row in cur.execute(sql):
  print ("{} ----- {} ---- {} -----   {}".format(str(row[0]),str(row[1]),str(row[2]),str(row[3])))
-- first  DROP all the table that exists
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Genre;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;

-- FIRST CREATE THE TRACK TABLE
CREATE TABLE Track(
    id INTEGER  NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    -- this is the rating
    rating INTEGER,
    -- this is the count how much it is listened
    count INTEGER,
    -- length of the song
    len INTEGER,
    -- song title it will be unique and no duplication
    -- of the same song
    title TEXT UNIQUE,

    -- it will be under a album so
    -- make a foreign key for that
    album_id INTEGER,

    -- and it will be under a genre

    genre_id INTEGER

);



--  NOW CREATE AN ALBUM

CREATE TABLE Album(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title TEXT UNIQUE,
    -- this is the foreign key
    -- every artise belongs to an artist
    artist_id INTEGER


);

-- now  create the artise that is connected to the album
CREATE TABLE Artist(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT UNIQUE
);

-- EVERY TRACK IS  APART OF THE GENRE

CREATE TABLE Genre (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT UNIQUE
    -- well you can add genre to the 
    -- album and the artist too
    -- but we leave that here



);


-- remember you have to always seed the table
-- first which one has no primary key
-- then you need to fill the
-- one with the foreign key
-- other wise it will throw ERROR 


-- insert into the artist name
insert into Artist (name) values("hridoy khan");
insert into Artist (name) values ("Air supply");
insert into Artist (name) values ("Imagine Dragon");


-- insert into the Genre

insert into Genre (name) Values('melody');
insert into Genre (name) Values('Rock');


-- now fill the Album
-- it has a title
-- and a artist id

insert into Album (title,artist_id) values ('bol_na',1);
insert into Album (title,artist_id) values ('gone',2);
insert into Album (title,artist_id) values ('get hard',3);



-- now we are going to insert to the track

insert into Track (title,rating,len,count,album_id,genre_id) values ("mon tore boli joto",5,297,0,1,1);
insert into Track (title,rating,len,count,album_id,genre_id) values ("love me or i will be gone",5,200,0,2,2);
insert into Track (title,rating,len,count,album_id,genre_id) values ("what ever it takes",5,300,0,3,2);
insert into Track (title,rating,len,count,album_id,genre_id) values ("we are legion",5,400,0,3,2);




-- it is ok to have replication as long as their numbers
-- and not string
-- remember no dupicate string




-- now the data is pices in different table with numbers
-- now we use the join query 
-- then grather the full data

-- suppose we want two data from two different table

-- select the album title from the album  and  artist name from the Artist
-- but do it where the album_artist id is the same as artist id 
SELECT Album.title,Artist.name From Album join Artist WHERE Album.artist_id = Artist.id;

-- make a another query to make it clear


-- find all the track and their related album

SELECT Track.title,Album.title From Track join Album Where Track.album_id = Album.id;


-- another
select Album.title,Album.artist_id,Artist.id,Artist.name from Album join Artist where Album.artist_id = Artist.id;
SELECT * FROM Track;


-- so now we eant the tracks with the corresponding Genre


SELECT Track.title,Genre.name From Track join Genre WHERE Track.genre_id = Genre.id;


-- now the complex

select Track.title,Artist.name,Album.title,Genre.name From Track join Artist join Album join Genre WHERE Track.genre_id = Genre.id and Track.album_id = Album.id and Album.artist_id = Artist.id;

-- to preetyfy the data
.mode column
.header on
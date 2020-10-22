# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplay"
users_table_drop = " DROP TABLE if exists users"
songs_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artist"
time_table_drop = "DROP TABLE IF EXISTS time"

songplay_table_create = (""" CREATE table if not exists songplay (
songplay_id serial not null Primary key, 
start_time timestamp not null, 
user_id varchar not null, 
level varchar, 
songs_id varchar , 
artist_id varchar , 
session_id int, 
location varchar, 
user_agent varchar
) 
""")

users_table_create = (""" create table if not exists users(
user_id varchar not null primary key , 
first_name varchar not null, 
last_name varchar not null, 
gender char, 
level varchar
)  
""")

songs_table_create = (""" create table if not exists songs (
songs_id varchar not null primary key,
title varchar, 
artist_id varchar, 
year int,
duration numeric) """)

artist_table_create = (""" create table if not exists artist (
artist_id varchar not null primary key,
name varchar,
location varchar,
latitude numeric, 
longitude numeric ) """)

time_table_create = (""" create table if not exists time (
start_time timestamp not null primary key,
hour int,
day varchar,
week int,
month int, 
year int,
weekday varchar
)
""")
# INSERT RECORDS

songplay_table_insert = (""" INSERT into songplay ( start_time , user_id , level , songs_id , artist_id , session_id, location, user_agent)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s) """)

users_table_insert = ("""INSERT INTO users (user_id , first_name , last_name , gender , level) 
VALUES (%s, %s, %s, %s, %s)
ON CONFLICT(user_id) DO UPDATE SET level = excluded.level
""")

songs_table_insert = (""" INSERT INTO songs (songs_id , title , artist_id , year , duration ) 
VALUES (%s, %s, %s, %s, %s)
ON CONFLICT(songs_id) 
DO NOTHING""")

artist_table_insert = (""" insert into artist (artist_id , name , location , latitude , longitude ) 
VALUES (%s, %s, %s, %s, %s)
ON CONFLICT(artist_id) 
DO NOTHING
""")

time_table_insert = ("""insert into time (start_time , hour , day , week , month , year , weekday )  
VALUES (%s, %s, %s, %s, %s, %s, %s)
ON CONFLICT(start_time)
DO NOTHING""")

# FIND SONGS

song_select = (""" select s.songs_id, a.artist_id from songs s join artist a on
s.artist_id=a.artist_id WHERE s.title=%s AND a.name=%s AND s.duration=%s ; """)

# QUERY LISTS

create_table_queries = [songplay_table_create, users_table_create, songs_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, users_table_drop, songs_table_drop, artist_table_drop, time_table_drop]
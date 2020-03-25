# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS SONGPLAYS"
user_table_drop = "DROP TABLE IF EXISTS USERS"
song_table_drop = "DROP TABLE IF EXISTS SONGS"
artist_table_drop = "DROP TABLE IF EXISTS ARTISTS"
time_table_drop = "DROP TABLE IF EXISTS TIME"

# CREATE TABLES

songplay_table_create = ("""CREATE TABLE IF NOT EXISTS SONGPLAYS (
songplay_id serial primary key
, start_time timestamp
, user_id int
, level varchar
, song_id varchar
, artist_id varchar
, session_id int
, location varchar
, user_agent varchar);
""")

user_table_create = ("""CREATE TABLE IF NOT EXISTS USERS (
user_id int primary key
, first_name varchar
, last_name varchar
, gender varchar
, level varchar);
""")

song_table_create = ("""CREATE TABLE IF NOT EXISTS SONGS (
song_id varchar primary key
, title varchar
, artist_id varchar not null
, year int
, duration float);
""")

artist_table_create = ("""CREATE TABLE IF NOT EXISTS ARTISTS (
artist_id varchar primary key
, name varchar
, location varchar
, latitude float
, longitude float);
""")

time_table_create = ("""CREATE TABLE IF NOT EXISTS TIME (
start_time timestamp primary key
, hour int
, day int
, week int
, month int
, year int
, weekday int);
""")

# INSERT RECORDS

songplay_table_insert = ("""INSERT INTO SONGPLAYS (
songplay_id
, start_time
, user_id
, level
, song_id
, artist_id
, session_id
, location
, user_agent)
VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
ON CONFLICT (songplay_id) DO NOTHING;
""")

user_table_insert = ("""INSERT INTO USERS (
user_id
, first_name
, last_name
, gender
, level)
VALUES (%s,%s,%s,%s,%s)
ON CONFLICT (user_id) DO NOTHING;
""")

song_table_insert = ("""INSERT INTO SONGS (
song_id
, title
, artist_id
, year
, duration)
VALUES (%s,%s,%s,%s,%s)
ON CONFLICT (song_id) DO NOTHING;
""")

artist_table_insert = ("""INSERT INTO ARTISTS (
artist_id
, name
, location
, latitude
, longitude)
VALUES (%s,%s,%s,%s,%s)
ON CONFLICT DO NOTHING;
""")


time_table_insert = ("""INSERT INTO TIME (
start_time
, hour
, day
, week
, month
, year
, weekday)
VALUES (%s,%s,%s,%s,%s,%s,%s)
ON CONFLICT DO NOTHING;
""")

# FIND SONGS

song_select = ("""SELECT ss.song_id, ss.artist_id FROM SONGS ss 
JOIN ARTISTS ars on ss.artist_id = ars.artist_id
WHERE ss.title = %s
AND ars.name = %s
AND ss.duration = %s
;
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]

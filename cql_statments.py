# key space name
keyspace_name = "sparkifydb"

# create key space
create_keyspace = """CREATE KEYSPACE IF NOT EXISTS %s 
                        WITH REPLICATION={'class':'SimpleStrategy','replication_factor':'1'}
                        AND durable_writes = TRUE""" % keyspace_name

# create tables
"""
:Query Info for Music : Give me the artist, song title and song's length in the music app history that was heard 
during sessionId = 338, and itemInSession = 4 
"""

create_music = """CREATE TABLE IF NOT EXISTS music_library
                (sessionId int, itemInSession int, artist text, song text, length float, 
                    PRIMARY KEY (sessionId,itemInSession,artist))"""

"""
Query Info for Artists: Give me only the following: name of artist, song (sorted by itemInSession) 
and user (first and last name) for userid = 10, sessionid = 182
"""
create_artist = """CREATE TABLE IF NOT EXISTS artist_library
                (userId float , sessionId int, itemInSession int, artist text, song text, firstName text, lastName text, 
                    PRIMARY KEY((userId, sessionId),itemInSession))
                WITH CLUSTERING ORDER BY (itemInSession ASC);"""

"""
:Query Info Users:Query 3: Give me every user name (first and last) in my music app history who listened to the 
song 'All Hands Against His Own' 
"""
create_user = """CREATE TABLE IF NOT EXISTS user_library
                (song text, userId float , sessionId int, itemInSession int, artist text, firstName text, lastName text, 
                    PRIMARY KEY (song, userId));"""

# insert statements
insert_music = "INSERT INTO music_library (sessionId, itemInSession, artist, song, length) VALUES (%s,%s,%s,%s,%s)"

insert_artist = "INSERT INTO artist_library (userId, sessionId, itemInSession, artist, song, firstName, lastName) VALUES (%s,%s,%s,%s,%s,%s,%s)"

insert_user = "INSERT INTO user_library (song, userId, sessionId, itemInSession, artist, firstName, lastName) VALUES (%s,%s,%s,%s,%s,%s,%s)"

# select statements
select_music = "SELECT artist, song, length FROM music_library WHERE sessionid =338 and itemInSession=4;"

select_artist = "SELECT itemInSession, artist, song, firstName, LastName FROM artist_library WHERE userid = 10 and sessionid = 182;"

select_user = "SELECT firstName,lastName FROM user_library WHERE song='All Hands Against His Own';"

# drop statements
drop_music = "DROP TABLE IF EXISTS music_library;"

drop_artist = "DROP TABLE IF EXISTS artist_library;"

drop_user = "DROP TABLE IF EXISTS user_library;"

# query dict
cql_dict = {
    "system_cql": {'keyspace_name': keyspace_name, "create_keyspace": create_keyspace},
    "create_cql": {"music": create_music, "artist": create_artist, "user": create_user},
    "insert_cql": {"music": insert_music, "artist": insert_artist, "user": insert_user},
    "select_cql": {"music": select_music, "artist": select_artist, "user": select_user},
    "drop_cql": {"music": drop_music, "artist": drop_artist, "user": drop_user}
}

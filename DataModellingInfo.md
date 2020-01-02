#Sparkifydb Data Modelling Information

## Query 1:  
Give me the artist, song title and song's length in the music app history that was heard during sessionId = 338, and itemInSession = 4

### Modelling Database based on Query 1:
This query excepts Name of the artist, title of the song, and track length to be determined based on the sessionId and itemInSession. 

The excepted output is artist name, song name, and track length info. 
Based on two key information : sessionId is 338 and itemInSession is 4

From the above information the expected `cassandraql` for `SELECT` is:

`SELECT STATEMENT`
```cassandraql
SELECT artist, song, length FROM music_library WHERE sessionid =338 and itemInSession=4;
```

Based on this we can create the following table called music_library as it provides in the basic information of song being played in the music library. 

Since the `select` statement has artist,song,length, sessionId, and itemInSession information the table music library will also have the following columns. The primary key for the table is sessionId,itemInSession, and artist as the primary key. Where sessionId and itemInSession are composite key and artist is the clustering column. 

`CREATE STATEMENT`
```cassandraql
CREATE TABLE IF NOT EXISTS music_library
            (sessionId int, itemInSession int, artist text, song text, length float, PRIMARY KEY ((sessionId,itemInSession),artist))
```
`INSERT STATEMENT`
```cassandraql
INSERT INTO music_library (sessionId, itemInSession, artist, song, length) VALUES (%s,%s,%s,%s,%s)
```

## Query 2:  
Give me only the following: name of artist, song (sorted by itemInSession) and user (first and last name) for userid = 10, sessionid = 182

### Modelling Database based on Query 2:
This query excepts name of the artist, song, users first name and last name to be queried based on the userId and sessionid. Also the song needs to be displayed based on ascending order of itemInSession.

The excepted output is artist name, song name, and users first name and last name. 
Based on two key information : userId is 10, and sessionId is 182.

From the above information the expected `cassandraql` for `SELECT` is:

`SELECT STATEMENT`
```cassandraql
SELECT itemInSession, artist, song, firstName, LastName FROM artist_library WHERE userid = 10 and sessionid = 182;
```

Based on this we can create the following table called artist_library as it provides in the basic information of artist being listened by users. 

Since the `select` statement has artist,song,first name, last name, userId, and sessionId information the table artist library will also have the following columns. The primary key for the table is userId, sessionId ,and itemInSession as the primary key. Where userId and sessionId are composite key and itemInSession is the clustering column which is ordered in ascending order. 

`CREATE STATEMENT`
```cassandraql
CREATE TABLE IF NOT EXISTS artist_library (userId float , sessionId int, itemInSession int, artist text, song text, firstName text, lastName text,  PRIMARY KEY((userId, sessionId),itemInSession)) WITH CLUSTERING ORDER BY (itemInSession ASC);
```

`INSERT STATEMENT`
```cassandraql
INSERT INTO artist_library (userId, sessionId, itemInSession, artist, song, firstName, lastName) VALUES (%s,%s,%s,%s,%s,%s,%s)
```

## Query 3:  
Give me every user name (first and last) in my music app history who listened to the song 'All Hands Against His Own'

### Modelling Database based on Query 2:
This query excepts users first name and last name to be queried based on the song.

The excepted output is users first name and last name. 
Based on two key information : song name 'All Hands Against His Own' .

From the above information the expected `cassandraql` for `SELECT` is:

`SELECT STATEMENT`
```cassandraql
SELECT firstName,lastName FROM user_library WHERE song='All Hands Against His Own';
```

Based on this we can create the following table called user_library as it provides in the basic information of user being listening to songs. 

Since the `select` statement has first name, last name, and song information the table user library will also have the following columns. The primary key for the table is song and userId as the primary key. Since song isn't unique and in order to gather all the user listened to a specific song, userId is added in the primary key to making it unique. 

`CREATE STATEMENT`
```cassandraql
CREATE TABLE IF NOT EXISTS user_library (song text, userId float , sessionId int, itemInSession int, artist text, firstName text, lastName text, PRIMARY KEY (song, userId));
```

`INSERT STATEMENT`
```cassandraql
INSERT INTO user_library (song, userId, sessionId, itemInSession, artist, firstName, lastName) VALUES (%s,%s,%s,%s,%s,%s,%s)
```

# Data Modeling for Sparkify
## Background 
### Introduction
A startup called Sparkify wants to analyze the data they've been collecting on songs and user activity on their new music streaming app. The analysis team is particularly interested in understanding what songs users are listening to. Currently, there is no easy way to query the data to generate the results, since the data reside in a directory of CSV files on user activity on the app.

In order to carry out the analytics a database with Apache Cassandra must be created to ansswer the specific queries (shown below). In project creates a database schema called Sparkify and ETL pipeline for the analysis. 

##### Create queries to ask the following three questions of the data
1. Give me the artist, song title and song's length in the music app history that was heard during  sessionId = 338, and itemInSession  = 4
```cassandraql
SELECT artist, song, length FROM music_library WHERE sessionid =338 and itemInSession=4;
```
2. Give me only the following: name of artist, song (sorted by itemInSession) and user (first and last name) for userid = 10, sessionid = 182
```cassandraql
SELECT itemInSession, artist, song, firstName, LastName FROM artist_library WHERE userid = 10 and sessionid = 182;
```
3. Give me every user name (first and last) in my music app history who listened to the song 'All Hands Against His Own'

```cassandraql
SELECT firstName,lastName FROM user_library WHERE song='All Hands Against His Own';
```

`Note: Background is based on Udacity Data Engineering Nano degree Program`

## Prerequisites for running the program
The project is built in python 2.7, Java SE Runtime Environment (JRE), and Apache Cassandra 
For the files to run locally, [Java SE Runtime Environment](https://www.oracle.com/technetwork/java/javase/downloads/jre8-downloads-2133155.html) , [Python 2.7](https://www.python.org/download/releases/2.7/ "Python-2.7") , [Apache Thrift](https://thrift.apache.org/) , and [Apache Cassandra](https://cassandra.apache.org/ "Cassandra") needs to be installed.

## File Info
### Data Files:
#### Song_data
Files are arranged in CSV. Example of one dataset: `event_data` is shown below. The directory of CSV files partitioned by date. Here are examples of filepaths to two files in the dataset:

```CSV
event_data/2018-11-08-events.csv
event_data/2018-11-09-events.csv
```

Sample View of CSV ![Event Data CSV](https://github.com/mindfultime/Cassandra-DataModelling/blob/master/event_datafile_image.jpg "Event Data CSV")


`Information taken from Udacity Nano degree Programme`

### CQL Scripts:
1. cql_statements: All the Apache Cassandra statements `cassandraql` for Creating, Dropping, Inserting, and Selection. Along with data dictonary has been created to help expand the cql in the future.

### Python Scripts:
1. database.py: The script contains are the database function for connection to database, creating keyspaces, setting keyspace, creating, droping, inserting, and selecting in the database. All cql statments are executed from `cql_statements.py` file.

2. etl.py: The script used for extracting data from `event_data` folder. The script will transform the data from the file and load it into the database created by `cql_statements` and `database.py`

## Execution of the project
1. Execute in `terminal:` `python etl.py`. This will extract, transform, and finally load the data in the database as per the project requirements (questions seen above). 


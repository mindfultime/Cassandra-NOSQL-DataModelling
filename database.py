from cassandra.cluster import Cluster
from cql_statments import cql_dict


def connect():
    """
    connecting to cassandra
    """
    try:
        # establishing connection to cluster
        cluster = Cluster()

        # initializing session
        session = cluster.connect()

        # returns session
        return cluster, session

    except Exception as e:
        print(e)


def create_keyspace(session):
    """
    creating keyspace
    :PARAM: database session
    """
    try:
        # create key space for sparkify database
        session.execute(cql_dict['system_cql']['create_keyspace'])
        print("Creating %s database" % cql_dict['system_cql']['keyspace_name'])

    except Exception as e:
        print("Error in creating db ")
        print(e)


def set_keyspace(session, keySpace):
    """
    Sets keyspace from the database
    :param keySpace string value for the specified key space
    :param session database session as session object
    """
    try:
        if keySpace == (cql_dict['system_cql']['keyspace_name']):
            # set keyspace
            session.set_keyspace(cql_dict['system_cql']['keyspace_name'])
            print("Setting %s database" % cql_dict['system_cql']['keyspace_name'])
        else:
            print("keyspace name not found!!")
    except Exception as e:
        print ("Error setting keyspace")
        print(e)


def drop_keyspace(session, keySpace):
    """
    Drops keyspace
    :param keySpace string value for the specified key space
    :param session database session as session object
    """
    print("Dropping {} keyspace".format(keySpace))
    try:
        session.execute("DROP KEYSPACE IF EXISTS %s" % keySpace)
    except Exception as e:
        print(e)


def create_tables(session):
    """
    Create tables in sparkify database
    :param session database session as session object
    """
    for tableName, cql in cql_dict['create_cql'].items():
        print("Creating {} table".format(tableName))
        try:
            session.execute(cql)
        except Exception as e:
            print(e)


def drop_tables(session):
    """
    Drop tables in sparkify database
    :param session database session as session object
    """
    # create tables in sparkify database
    for tableName, cql in cql_dict['drop_cql'].items():
        print("Dropping {} table".format(tableName))
        try:
            session.execute(cql)
        except Exception as e:
            print(e)


def insert_into(session, tableName, data, rowNum, dataLength):
    """
    Inserting data from the specific cols from the dataFrame into the specified tableName within the current session
    :param session database session as session object and keySpace name as string
    :param data row of data to be added in the keySpace
    :param rowNum enumarated number for the rows in the data_list
    :param datalength total rows in the dataframe
    :param tableName name of the table the data to be inserted into
    """
    try:
        # getting cql TableName from the cql_dict and matching it with user provided tableName
        for cqlTableName, cql in cql_dict['insert_cql'].items():  # type: (str, str)
            if tableName == cqlTableName:
                session.execute(cql, data)
        print("Inserting data into {} table row {} of {} ".format(tableName, rowNum, dataLength))
    except Exception as e:
        print(e)


def select_cql(session, tablename):
    """
       Selecting cql per defined quires into the specified tableName within the current session
       :param session database session as session object and keySpace name as string
       :param tableName name of the table the data to be inserted into
       """
    for tableName, cql in cql_dict['select_cql'].items():  # type: (str, str)
        if tablename == tableName:
            print("*******************************************")
            print("EXECUTING CQL: {}".format(cql))
            print("*******************************************")
            try:
                results = session.execute(cql)
                for row in results:
                    print(row)
            except Exception as e:
                print(e)
            print("\n")


def main():
    print ("Initializing Database")


if __name__ == '__main__':
    main()

# Importing files
import glob
import os
import pandas as pd
import database


def get_files(filepath):
    """
    Gets files from filepath
    :param filepath: location to data
    """
    # set file path
    filepath = os.getcwd() + filepath
    # print(filepath)

    # Create a for loop to create a list of files and collect each filepath
    for root, dirs, files in os.walk(filepath):
        # join the file path and roots with the subdirectories using glob
        path_list = glob.glob(os.path.join(root, '*'))
        return path_list


def compile_dataframes(files, ext):
    """
    Compile all data frames from given file path into one single data frame and to output user defined extension
    :param files: list of files in the specified file path
    :param ext user can specify the output file type from the final data frame
    """
    # making data frame list
    dataframes = []

    # Iterating through the file_path_list to get filename and convert them to data frame
    for f in files:
        print("Processing file {}".format(f))

        # checking file extension
        if f.endswith('.csv'):
            dataframes.append(pd.read_csv(f))

    # concat data frames
    allFrames = pd.concat(dataframes)

    # cleaning columns that are null in dataset
    allFrames.dropna(inplace=True)

    # removing null artist from dataset
    combinedFrames = allFrames[allFrames.notnull()]

    # make file from ext
    if ext == 'csv':
        filepath = os.getcwd() + r'\event_datafile_new.csv'
        print("File created in {}".format(filepath))
        combinedFrames.to_csv(filepath)

    return combinedFrames


def insert_data(dataFrame, tableName, cols, session):
    """
        Inserting data from the specific cols from the dataFrame into the specified tableName within the current session
        :param session database session as session object and keySpace name as string
        :param dataFrame final dataFrame to be added in the keySpace
        :param tableName name of the table the data to be inserted into
        :param cols user defined cols to be used as the subset from the dataFrame, these columns matches the columns in
                    the given tableName
    """
    if tableName == "music":
        df = dataFrame[cols]
        iterate_list(df.values.tolist(), "music", session)
    elif tableName == "artist":
        df = dataFrame[cols]
        iterate_list(df.values.tolist(), "artist", session)
    elif tableName == "user":
        df = dataFrame[cols]
        iterate_list(df.values.tolist(), "user", session)


def iterate_list(dataList, tableName, session):
    """
        Iterate through the data_list and insert into the specific tablename with the active session
        :param session database session as session object and keyspace name as string
        :param dataList final dataFrame converted to list format with df.values.tolist() function
        :param tableName name of the table the data to be inserted into

        Enumerate() method adds a counter to an iterable and returns it in a form of enumerate object.
        This enumerate object can then be used directly in for loops or be converted into a list of tuples using list()
        method.
    """
    for rowNum, data in enumerate(dataList, 1):
        database.insert_into(session, tableName, data, rowNum, len(dataList))
    print("--------------------------------------------------------------------------\n")


def main():
    # initializing session
    cluster, session = database.connect()

    # drop key space
    database.drop_keyspace(session, "sparkifydb")

    # create keyspace
    database.create_keyspace(session)

    # set keyspace
    database.set_keyspace(session, "sparkifydb")

    # create tables
    database.create_tables(session)

    # compile event data from assigned file path
    files = get_files(r'/event_data')

    # overall event_data frame
    event_dataframe = compile_dataframes(files, 'csv')

    # defining columns to be used in for each table in the final dataframe
    music_cols = ["sessionId", "itemInSession", "artist", "song", "length"]
    artist_cols = ["userId", "sessionId", "itemInSession", "artist", "song", "firstName", "lastName"]
    user_cols = ["song", "userId", "sessionId", "itemInSession", "artist", "firstName", "lastName"]

    # inserting data into database
    insert_data(event_dataframe, "music", music_cols, session)
    insert_data(event_dataframe, "artist", artist_cols, session)
    insert_data(event_dataframe, "user", user_cols, session)

    # select queries
    database.select_cql(session, "music")
    database.select_cql(session, "artist")
    database.select_cql(session, "user")


if __name__ == '__main__':
    main()

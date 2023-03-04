import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn

def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def main():
    database = r"..data\retro.db"

    sql_create_game_table = """ CREATE TABLE IF NOT EXISTS game (
                                        game_id integer PRIMARY KEY,
                                        game_title text NOT NULL,
                                        platform text,
                                        year_released integer,
                                        publisher text,
                                        licensed text,
                                        game_notes text
                                        ); """

    sql_create_user_table = """CREATE TABLE IF NOT EXISTS users (
                                        user_id integer PRIMARY KEY,
                                        user_name text NOT NULL,
                                        user_email text NOT NULL,
                                        user_password text NOT NULL
                                );"""
    
    # sql_create_comments_table = """CREATE TABLE IF NOT EXISTS comments (
    #                                 entry_id integer PRIMARY KEY,
    #                                 timestamp text,
    #                                 user_id integer,
    #                                 user_name text,
    #                                 game_id integer,
    #                                 game_title text,
    #                                 played integer,
    #                                 owned integer,
    #                                 completed integer,
    #                                 playability text,
    #                                 difficulty text,
    #                                 user_notes text,
    #                                 FOREIGN KEY (user_id) REFERENCES user (user_id)
    #                                 FOREIGN KEY (user_name) REFERENCES user (user_name)
    #                                 FOREIGN KEY (game_id) REFERENCES games (game_id)
    #                                 FOREIGN KEY (game_title) REFERENCES games (game_title)
    #                             );"""

    # create a database connection
    conn = create_connection(r"data\retro.db")

    # create tables
    if conn is not None:
        # create projects table
        create_table(conn, sql_create_game_table)

        # create tasks table
        create_table(conn, sql_create_user_table)
    else:
        print("Error! cannot create the database connection.")   
    conn.close()             

if __name__ == '__main__':
    main()


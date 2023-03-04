import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


def select_all_game(conn):
    """
    Query all rows in the game table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM game")

    rows = cur.fetchall()

    for row in rows:
        print(row)


def select_game_by_publisher(conn, publisher):
    """
    Query game by publisher
    :param conn: the Connection object
    :param publisher:
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM game WHERE publisher=?", (publisher,))

    rows = cur.fetchall()

    for row in rows:
        print(row)


def main():
    database = r"data\retro.db"

    # create a database connection
    conn = create_connection(database)
    with conn:
        print("1. Query game by publisher:")
        select_game_by_publisher(conn, 'Nintendo')

        print("2. Query all game")
        select_all_game(conn)


if __name__ == '__main__':
    main()
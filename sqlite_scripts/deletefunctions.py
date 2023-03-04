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


def delete_game(conn, id):
    """
    Delete a game by game id
    :param conn:  Connection to the SQLite database
    :param id: id of the game
    :return:
    """
    sql = 'DELETE FROM game WHERE game_id=?'
    cur = conn.cursor()
    cur.execute(sql, (id,))
    conn.commit()


def delete_all_games(conn):
    """
    Delete all rows in the game table
    :param conn: Connection to the SQLite database
    :return:
    """
    sql = 'DELETE FROM game'
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()


def main():
    database = r"data\retro.db"

    # create a database connection
    conn = create_connection(database)
    with conn:
        delete_game(conn, 750);
        # delete_all_games(conn);


if __name__ == '__main__':
    main()
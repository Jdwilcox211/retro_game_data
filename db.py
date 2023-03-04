import sqlite3
from sqlite3 import Error
import openpyxl

workbook = openpyxl.load_workbook('upload.xlsx')
sheet = workbook['NES']

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

def create_game(conn, game):
    """
    Create a new project into the projects table
    :param conn:
    :param project:
    :return: game id
    """
    sql = ''' INSERT INTO game(game_title,platform,year_released,publisher,licensed,game_notes)
              VALUES(?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, game)
    conn.commit()
    print(f'{cur.lastrowid}')
    return cur.lastrowid

def update_task(conn, game):
    """
    update priority, begin_date, and end date of a task
    :param conn:
    :param task:
    :return: project id
    """
    sql = ''' UPDATE game
              SET year_released = ? ,
                  publisher = ?
              WHERE game_id = ?'''
    cur = conn.cursor()
    cur.execute(sql, game)
    conn.commit()
    conn.close()

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


def select_game_by_game_id(conn, game_id):
    """
    Query game by game_id
    :param conn: the Connection object
    :param game_id:
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM game WHERE game_id=?", (game_id,))

    rows = cur.fetchall()

    for row in rows:
        print(row)

def select_game_by_game_title(conn, game_title):
    """
    Query game by game_title
    :param conn: the Connection object
    :param game_title:
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM game WHERE game_title=?", (game_title,))

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
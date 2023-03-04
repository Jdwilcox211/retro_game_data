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

conn = create_connection(r"data\retro.db")
update_task(conn,(1991,'Nintendo',785))
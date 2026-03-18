import mysql.connector
from mysql.connector import Error
import os


def get_connection():
    """Returns a connection to the MySQL database."""
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password=os.getenv("DB_PASSWORD"),
            database="student_db"
        )
        return conn
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None

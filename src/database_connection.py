import sqlite3

connection = sqlite3.connect('pol.db')
cursor = connection.cursor()

def get_database_connection():
    return connection

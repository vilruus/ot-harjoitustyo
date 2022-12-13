from database_connection import get_database_connection

def drop_tables(connection):
    cursor = connection.cursor()

    cursor.execute('''
        drop table if exists users;
    ''')

    connection.commit()
    cursor = connection.cursor()


    cursor.execute('''
        drop table if exists exercises;
    ''')

    connection.commit()


def create_tables(connection):
    cursor = connection.cursor()

    cursor.execute('''
        create table users (
            username text primary key,
            password text
        );
    ''')

    cursor.execute('''
        create table exercises (
            name text primary key,
            id text,
            sets text,
            reps text,
            weight text,
            user text
        );
    ''')

    connection.commit()


def initialize_database():
    connection = get_database_connection()

    drop_tables(connection)
    create_tables(connection)

    connection.commit()
    connection.close()


if __name__ == "__main__":
    initialize_database()
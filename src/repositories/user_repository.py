from entities.user import User
from database_connection import get_database_connection

def get_user_from_tuple(tuple):
    (username, password) = tuple
    return User(username, password)

class UserRepository:
    def __init__(self, connection):
        self._connection = connection

    def find_all(self):
        cursor = self._connection.cursor()
        cursor.execute("select * from users")
        rows = cursor.fetchall()
        users = list(map(get_user_from_tuple, rows))
        return users

    def find_by_username(self, username):
        cursor = self._connection.cursor()
        cursor.execute("select * from users WHERE username = (:username)", {'username':username})
        row = cursor.fetchone()
        user = get_user_from_tuple(row)
        return user

    def create(self, user):
        cursor = self._connection.cursor()
        cursor.execute("INSERT INTO users VALUES (:username, :password)",{'username': user.username, 'password': user.password})
        self._connection.commit()
        return user

    def delete_all(self):
        cursor = self._connection.cursor()
        cursor.execute("DELETE FROM users")
        self._connection.commit()

user_repository = UserRepository(get_database_connection())

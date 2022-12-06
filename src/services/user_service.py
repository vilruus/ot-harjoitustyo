from entities.user import User
from repositories.user_repository import (user_repository as default_user_repository)

class UserService:
    def __init__(self, user_repository=default_user_repository):
        self._user = None
        self._user_repository = user_repository

    def create_user(self, username, password, login=True):
        user = self._user_repository.create(User(username, password))
        return user

    def print_users(self):
        users = self._user_repository.find_all()
        print(users)

    def login(self,username, password):
        user = self._user_repository.find_by_username(username)

        #TODO: Error handling
        if user.password != password:
            self._user = user
            return user
        
    def get_logged_user(self):
        return self._user

    def get_logged_username(self):
        return self._user.username
    

user_service = UserService()
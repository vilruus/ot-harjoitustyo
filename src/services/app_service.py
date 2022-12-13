from entities.user import User
from entities.exercise import Exercise
from repositories.user_repository import (user_repository as default_user_repository)
from repositories.exercise_repository import (exercise_repository as default_exercise_repository)

class AppService:
    def __init__(self, user_repository=default_user_repository, exercise_repository = default_exercise_repository):
        self._user = None
        self._user_repository = user_repository
        self._exercise_repository = exercise_repository

    def create_user(self, username, password, login=True):
        user = self._user_repository.create(User(username, password))
        return user

    def print_users(self):
        users = self._user_repository.find_all()
        print(users)

    def login(self,username, password):
        user = self._user_repository.find_by_username(username)

        #TODO: Error handling
        if user.password == password:
            self._user = user
            return user
        
    def get_logged_user(self):
        return self._user

    def get_logged_username(self):
        return self._user.username

    def create_exercise(self, name, reps, sets, weight):
        exercise = self._exercise_repository.create(Exercise(name, sets, reps,weight,self._user.username))
        return exercise
    
    def get_users_exercises(self):
        exercises = self._exercise_repository.find_by_user(self._user.username)
        return exercises
    
    def delete_exercise(self, id):
        self._exercise_repository.delete_by_id(id)


app_service = AppService()
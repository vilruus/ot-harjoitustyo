from entities.exercise import Exercise
from database_connection import get_database_connection

def get_exercise_from_tuple(tuple):
    (name, id, sets, reps, weight, user) = tuple
    return Exercise(name, sets, reps, weight, user, id)

class ExerciseRepository:
    def __init__(self, connection):
        self._connection = connection

    def create(self, exercise):
        cursor = self._connection.cursor()
        cursor.execute("INSERT INTO exercises VALUES (:name, :id, :sets, :reps, :weight, :user)",{'name': exercise.name, 'id': exercise.id, 'sets': exercise.sets, 'reps':exercise.reps, 'weight':exercise.weight, 'user':exercise.user})
        self._connection.commit()
        return exercise
    
    def find_all(self):
        cursor = self._connection.cursor()
        cursor.execute("select * from exercises")
        rows = cursor.fetchall()
        exercises = list(map(get_exercise_from_tuple, rows))
        return exercises

    def find_by_user(self, user):
        cursor = self._connection.cursor()
        cursor.execute("select * from exercises WHERE user = (:user)", {'user':user})
        rows = cursor.fetchall()
        exercises = list(map(get_exercise_from_tuple, rows))   
        return exercises

    
    def delete_by_id(self, id):
        cursor = self._connection.cursor()
        cursor.execute("DELETE from exercises WHERE id = (:id)", {'id':id})

    def delete_all(self):
        cursor = self._connection.cursor()
        cursor.execute("DELETE FROM exercises")
        self._connection.commit()

exercise_repository = ExerciseRepository(get_database_connection())
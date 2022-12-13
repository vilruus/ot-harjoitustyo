import uuid

class Exercise:
    def __init__(self,excercise_name,sets,reps,weight, user, id=None):
        self.name = excercise_name
        self.id = id or str(uuid.uuid4())
        self.sets = sets
        self.reps = reps
        self.weight = weight
        self.user = user

import uuid

class Exercise:
    def __init__(self,excercise_name,excercise_id,sets,reps,weight):
        self.name = excercise_name
        self.id = excercise_id or str(uuid.uuid4()),
        self.sets = sets
        self.reps = reps
        self.weight = weight

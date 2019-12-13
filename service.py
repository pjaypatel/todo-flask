from models import ToDoModel
class ToDoService:
    def __init__(self):
        self.model = ToDoModel()

    def create(self, params):
        return self.model.create(params["Title"], params["Description"])

    def update(self, params):
        return self.model.update(params["Title"], params["Description"])

    def select(self, params):
        return self.model.select(params["Title"])

    def delete(self, params):
        return self.model.delete(params["Title"])


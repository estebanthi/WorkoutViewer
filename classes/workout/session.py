from classes.collections.base_collection import BaseCollection


class Session(BaseCollection):

    def __init__(self, date, exercices=None):
        if not exercices:
            exercices = []
        self.items = exercices
        self.date = date

    def __repr__(self):
        return str(self.date)
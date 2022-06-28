from classes.ui.qerror_popup import QErrorPopup
from classes.ui.qinfo_popup import QInfoPopup
from classes.collections.unique_list import UniqueList


class Controller:

    def __init__(self):
        self.model = None
        self.view = None

    def connect(self):
        self.model.dataUpdatedSignal.connect(self.data_loaded)

    def load_data(self):
        self.model.load_data()

    def notify_read_data_error(self):
        QErrorPopup("Erreur lors de la lecture de vos données")

    def data_loaded(self):
        self.view.updateData()

    def get_sessions_for_day(self, day):
        return len([session for session in self.model.sessions if session.date.weekday() == day])

    def filter(self, start_date, end_date):
        self.model.load_data()
        self.model.filter(start_date, end_date)

    def reset_filter(self):
        self.model.load_data()

    def get_exercices(self):
        exercices = [session.items for session in self.model.sessions]
        flat_exercices = [item for sublist in exercices for item in sublist]
        unique_exercices = UniqueList(flat_exercices)
        return unique_exercices

    def get_exercice(self, name):
        exercices = [session.items for session in self.model.sessions]
        flat_exercices = [item for sublist in exercices for item in sublist]
        return [exercice for exercice in flat_exercices if exercice.name == name]

    def get_sessions(self):
        return self.model.sessions

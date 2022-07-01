import pandas as pd
import datetime as dt


from classes.workout.time_exercice import TimeExercice
from classes.workout.rehearsal_exercice import RehearsalExercice
from classes.config import Config
from classes.workout.session import Session
from classes.collections.unique_list import UniqueList


from PyQt5 import QtCore


class Model(QtCore.QObject):
    dataUpdatedSignal = QtCore.pyqtSignal()

    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.config = Config().get()

        self.load_data()

    def load_data(self):
        data = None
        self.sessions = None
        try:
            with open('data/data.sv', 'r', encoding='utf-8') as file:
                data = pd.read_csv(file)

        except Exception:
            self.controller.notify_read_data_error()

        if isinstance(data, pd.DataFrame):
            exercices = self.get_exercices(data)
            sessions = self.get_sessions(exercices)
            self.sessions = sessions
            self.dataUpdatedSignal.emit()


    def get_exercices(self, data):

        exercices = []

        for row in data.iterrows():

            date = dt.datetime.strptime(row[1]['DATE'], '%d-%m-%Y')
            name = row[1]['EXERCISE']
            reps = int(row[1]['NB_REPS'])
            load = float(row[1]['WEIGHT']) if row[1]['WEIGHT'] != 'BW' else self.config['weight']
            duration = row[1]['DURATION']

            if reps == 0:
                exercice = TimeExercice(name, date, duration)
            else:
                exercice = RehearsalExercice(name, date, reps, load)

            exercices.append(exercice)

        exercices = list(reversed(exercices))
        return exercices

    def get_sessions(self, exercices):
        dates = UniqueList([exercice.date for exercice in exercices])

        sessions = []
        for date in dates:
            session = Session(date, [exercice for exercice in exercices if exercice.date == date])
            sessions.append(session)

        return sorted(sessions, key=lambda session: session.date)

    def filter(self, start_date, end_date):
        filtered_sessions = list(filter(lambda session: start_date <= session.date <= end_date, self.sessions))
        self.sessions = filtered_sessions
        self.dataUpdatedSignal.emit()

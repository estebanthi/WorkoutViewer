from classes.workout.exercice import Exercice


class TimeExercice(Exercice):

    def __init__(self, name, date, duration):
        super().__init__(name, date, duration)

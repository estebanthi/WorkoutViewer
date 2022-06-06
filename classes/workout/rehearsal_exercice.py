from classes.workout.exercice import Exercice


class RehearsalExercice(Exercice):

    def __init__(self, name, date, rehearses, load):
        value = (rehearses, load)
        super().__init__(name, date, value)


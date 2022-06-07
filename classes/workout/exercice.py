from abc import ABC


class Exercice(ABC):

    def __init__(self, name, date, value):
        self.date = date
        self.name = name
        self.value = value

    def __eq__(self, other):
        return self.name == other.name

    def __repr__(self):
        return f"{self.name} : {self.value}"

    def __hash__(self):
        total = 0
        for letter in self.name:
            total += ord(letter)
        return total
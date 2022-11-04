"""
CP1404 - Trimester 3 2022 - Jacob O'Toole
Programming language exercise
estimated: 30 minutes
actual: 25 minutes
"""


class ProgrammingLanguage:

    def __init__(self, name, typing, reflection, year):
        self.name = name
        self.typing = typing
        self.refection = reflection
        self.year = year

    def is_dynamic(self):
        return self.typing == "Dynamic"

    def __str__(self):
        return f"{self.name}, {self.typing} Typing, Reflection={self.refection}, First appeared in {self.year}"

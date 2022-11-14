"""
CP1404 - Trimester 3 2022 - Jacob O'Toole
Guitar class exercise
estimation: 20 minutes
actual: 15 minutes
"""
CURRENT_YEAR = 2022
VINTAGE_AGE = 50

class Guitar:

    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year}): ${self.cost:,.2f}"

    def get_age(self):
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        return self.get_age() >= VINTAGE_AGE

    def __lt__(self, other):
        if self.cost < other.cost:
            return True
        else:
            return False

    def format_guitar(self):
        return f"{self.name},{self.year},{self.cost}"


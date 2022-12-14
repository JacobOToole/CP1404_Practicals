"""
CP1404 Trimester 3 2022 - Jacob O'Toole
Time estimate: 2 hours
Actual:
"""


class Project:
    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __str__(self):
        return f"{self.name}, start: {self.start_date}, priority {self.priority}, estimate: ${self.cost_estimate:,.2f}, " \
               f"completion: {self.completion_percentage}%"

    def is_completed(self):
        return self.completion_percentage == 100

    def format_project(self):
        return f"{self.name}\t{self.start_date}\t{self.priority}\t{self.cost_estimate}\t{self.completion_percentage}"

    def __lt__(self, other):
        if self.priority < other.priority:
            return True
        else:
            return False

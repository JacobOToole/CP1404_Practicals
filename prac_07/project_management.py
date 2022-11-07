"""
CP1404 Trimester 3 2022 - Jacob O'Toole
Time estimate: 2 hours
Actual: 3hr 25m
"""

import datetime
from prac_07.project import Project

MENU = "(L)oad projects \n" \
       "(S)ave projects \n" \
       "(D)isplay projects \n" \
       "(F)ilter projects by date \n" \
       "(A)dd new project \n" \
       "(U)pdate project \n" \
       "(Q)uit"


def main():
    file = 'projects.txt'
    projects = get_projects(file)

    print(MENU)
    choice = input(">>> ").lower()
    while choice != 'q':
        if choice == 'l':
            file = input("File: ")
            projects = get_projects(file)
        if choice == 's':
            save_projects(file, projects)
        if choice == 'd':
            display_projects(projects)
        if choice == 'f':
            filter_projects(projects)
        if choice == 'a':
            add_projects(projects)
        if choice == 'u':
            update_projects(projects)
        choice = input(">>> ").lower()
    print("Thank you for using custom-built project management software.")


def get_projects(file):
    projects = []
    with open(file, 'r') as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split('\t')
            project = Project(parts[0], parts[1], int(parts[2]), float(parts[3]), float(parts[4]))
            projects.append(project)
    return projects


def save_projects(file, projects):
    with open(file, 'w') as out_file:
        print('Name', 'Start Date', 'Priority', 'Cost Estimate', 'Completion Percentage', sep="\t", file=out_file)
        for project in projects:
            print(Project.format_project(project), file=out_file)


def display_projects(projects):
    completed = []
    incomplete = []
    projects.sort()
    for project in projects:
        if Project.is_completed(project):
            completed.append(project)
        else:
            incomplete.append(project)

    print("Incomplete projects:")
    for project in incomplete:
        print(f"\t{str(project)}")

    print("Completed projects:")
    for project in completed:
        print(f"\t{str(project)}")


# This function does not work, TypeError: 'Project' object is not subscriptable.
def filter_projects(projects):
    date_string = input("Date (d/m/yyyy): ")
    date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
    print(date)
    for project in projects:
        project_date = datetime.datetime.strptime(project[1], "%d/%m/%Y").date()
        if project_date > date:
            print(str(project))


def add_projects(projects):
    print("Let's add a new project")
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yyyy): ")
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost estimate: "))
    percent_complete = float(input("Percent complete: "))
    project = Project(name, start_date, priority, cost_estimate, percent_complete)
    projects.append(project)


# Function doesn't work, TypeError: 'Project' object is not subscriptable. Same error as in filter_projects()
def update_projects(projects):
    for i, project in enumerate(projects):
        print(f"{i} {str(project)}")
    index_choice = int(input("Project choice: "))
    new_percentage = float(input("New percentage: "))
    print(projects[index_choice][4])


main()

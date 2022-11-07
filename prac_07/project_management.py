"""
CP1404 Trimester 3 2022 - Jacob O'Toole
Time estimate: 2 hours
Actual:
"""

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


main()

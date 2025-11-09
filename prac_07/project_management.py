"""CP1404/CP5632 Practical - Project Management
Estimate: 90 min | Actual: ___ min
"""

from datetime import datetime
from project import Project

DATE_FMT = "%d/%m/%Y"
FILENAME = "projects.txt"


def main():
    """Main menu for project management program."""
    print("Welcome to Pythonic Project Management")
    projects = load_projects(FILENAME)
    print(f"Loaded {len(projects)} projects from {FILENAME}")

    MENU = (
        "- (L)oad projects  \n"
        "- (S)ave projects  \n"
        "- (D)isplay projects  \n"
        "- (F)ilter projects by date\n"
        "- (A)dd new project  \n"
        "- (U)pdate project\n"
        "- (Q)uit"
    )

    choice = input(MENU + "\n>>> ").lower()
    while choice != "q":
        if choice == "l":
            filename = input("Filename to load projects from: ")
            projects = load_projects(filename)
        elif choice == "s":
            filename = input("Filename to save projects to: ")
            save_projects(filename, projects)
        elif choice == "d":
            display_projects(projects)
        elif choice == "f":
            filter_projects_by_date(projects)
        elif choice == "a":
            add_project(projects)
        elif choice == "u":
            update_project(projects)
        else:
            print("Invalid option")

        choice = input(MENU + "\n>>> ").lower()

    save_choice = input(f"Would you like to save to {FILENAME}? ").lower()
    if save_choice in ["y", "yes"]:
        save_projects(FILENAME, projects)
    else:
        print(f"Would you like to save to {FILENAME}? no, I think not.")
    print("Thank you for using custom-built project management software.")


def load_projects(filename):
    """Load projects from a text file and return a list of Project objects."""
    projects = []
    with open(filename, "r", encoding="utf-8") as in_file:
        in_file.readline()  # skip header
        for line in in_file:
            parts = line.strip().split("\t")
            project = Project("", "", 0, 0.0, 0)
            project.from_row(parts)
            projects.append(project)
    return projects


def save_projects(filename, projects):
    """Save all projects to a text file."""
    with open(filename, "w", encoding="utf-8") as out_file:
        out_file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion\n")
        for project in projects:
            out_file.write("\t".join(project.to_row()) + "\n")

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
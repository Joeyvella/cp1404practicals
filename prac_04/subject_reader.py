"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"

def main():
    """Reads the subjects data"""
    subjects = load_subjects(FILENAME)
    display_subjects(subjects)

def load_subjects(filename=FILENAME):
    """loads that data from txt file"""
    subjects = []
    input_file = open(filename)
    for line in input_file:
        line = line.strip()
        parts = line.split(',')
        parts[2] = int(parts[2])
        subjects.append(parts)
    input_file.close()
    return subjects


def display_subjects(subjects):
    """will display the data clearly"""
    for subject in subjects:
        code, lecturer, student_count = subject
        print(f"{code} is taught by {lecturer} and has {student_count} students")



main()


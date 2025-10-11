"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    """Loads in subject records and prints a formatted report"""
    subjects = load_data(FILENAME)
    display_subjects(subjects)


def load_data(filename=FILENAME):
    """Read data from file formatted like: subject,lecturer,number of students."""

    subjects = []
    with open(filename) as input_file
        for line in input_file:
            line = line.strip()
            subject_code, lecturer, count_str = line.split(",")
            student_count = int(count_str)
            subjects.append([subject_code, lecturer, student_count])
    return subjects


def display_subjects(subjects):
    """Prints line that describes the records"""
    for subject_code, lecturer, student_count in subjects:
        print(f"{subject_code} is taught by {lecturer} and has {student_count} students")



    input_file = open(filename)
    for line in input_file:
        print(line)  # See what a line looks like
        print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        print(parts)  # See what the parts look like (notice the integer is a string)
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        print(parts)  # See if that worked
        print("----------")
    input_file.close()


main()
"""
CP1404/CP5632 Practical
File and class example - opens/reads a file, stores in objects of custom class
(contains multiple versions for demonstration: using csv and namedtuple)
"""

from programming_language import ProgrammingLanguage

def main():
    """Read file of programming language details, save as objects, display."""
    languages = []
    in_file = open('languages.csv', 'r')
    in_file.readline()

    for line in in_file:
        parts = line.strip().split(',')

        name = parts[0]
        typing = parts[1]
        reflection = (parts[2] == "Yes")
        year = int(parts[3])

        if len(parts) >= 5:
            pointer_arithmetic = (parts[4] == "Yes")
            language = ProgrammingLanguage(name, typing, reflection, year, pointer_arithmetic)
        else:
            language = ProgrammingLanguage(name, typing, reflection, year)

        languages.append(language)

    in_file.close()

    for language in languages:
        print(language)


main()

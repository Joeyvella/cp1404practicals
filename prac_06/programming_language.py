


class ProgrammingLanguage:
    """Represent programming languages"""
    def __init__(self, name, typing, reflection, year):

        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Return True if language is dynamic"""
        return self.typing.lower()== "dynamic"

    def __str__(self):
        """Neatly format a string for the language"""
        return f"{self.name}"
"""
Kivy GUI program to convert miles to kilometres
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KM = 1.60934  # conversion constant


class MilesToKilometresApp(App):
    """App for converting miles to kilometres."""
    # This is bound to the output Label's text in the kv file
    output_text = StringProperty("0.0")

    def build(self):
        """Build the Kivy app from the kv file."""
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file("convert_miles_km.kv")
        return self.root

    def handle_convert(self):
        """Convert the value in the TextInput from miles to km."""
        miles = self.get_valid_miles()
        kilometres = miles * MILES_TO_KM
        # Update the StringProperty, which updates the label automatically
        self.output_text = f"{kilometres:.5f}"


    def handle_increment(self, change):
        """
        Change the miles value up or down by 'change' (an int, e.g. +1 or -1),
        then convert again.
        """
        miles = self.get_valid_miles()
        miles += change
        # Put the new miles value back into the TextInput
        self.root.ids.input_miles.text = str(miles)
        # Recalculate the output
        self.handle_convert()
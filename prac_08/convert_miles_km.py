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

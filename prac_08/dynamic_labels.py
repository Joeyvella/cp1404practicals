from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout


class DynamicLabelsApp(App):

    def __init__(self):
        super().__init__()
        # This is the data (model)
        self.names = ["Alex", "Bob", "Ryan", "Dora", "Evan"]

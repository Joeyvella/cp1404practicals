from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout


class DynamicLabelsApp(App):

    def __init__(self):
        super().__init__()
        # This is the data (model)
        self.names = ["Alex", "Bob", "Ryan", "Dora", "Evan"]

    def build(self):
        """Build the Kivy interface and add labels."""
        self.root = Builder.load_file("dynamic_labels.kv")

        main_box = self.root.ids.main  # Get the BoxLayout with id 'main'

        # Create a Label for each name and add it to the layout
        from kivy.uix.label import Label
        for name in self.names:
            temp_label = Label(text=name)
            main_box.add_widget(temp_label)

        return self.root


DynamicLabelsApp().run()

from kivy.app import App
from kivy.lang import Builder

class BoxLayoutDemo(App):
    def build(self):
        """Build Kivy app."""
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_greet(self):
        """Handle the greet button when pressed."""
        name = self.root.ids.input_name.text
        self.root.ids.output_label.text = f"Hello {name}"

    def handle_clear(self):
        """Handle the Clear button when pressed."""
        self.root.ids.input_name.text = ""
        self.root.ids.output_label.text = ""



BoxLayoutDemo().run()

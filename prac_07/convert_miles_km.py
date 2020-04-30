from kivy.app import App
from kivy.lang import Builder
from kivy.app import StringProperty


class MilesToKilometers(App):
    def build(self):
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def calculate_kms(self):
        self.root.ids.output_label.text = "Oops, m in the screenshot is not a good abbreviation for miles."


MilesToKilometers().run()

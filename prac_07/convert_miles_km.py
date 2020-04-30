from kivy.app import App
from kivy.lang import Builder
from kivy.app import StringProperty

MILES_TO_KM = 1.609344


class MilesToKilometers(App):
    def build(self):
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def calculate_kms(self):
        value = self.get_miles()
        result = value * MILES_TO_KM
        self.root.ids.output_label.text = str(result)

    def increment_miles(self, change):
        value = self.get_miles() + change
        self.root.ids.input_miles.text = str(value)
        self.calculate_kms()

    def get_miles(self):
        try:
            value = float(self.root.ids.input_miles.text)
            return value
        except ValueError:
            return 0


MilesToKilometers().run()

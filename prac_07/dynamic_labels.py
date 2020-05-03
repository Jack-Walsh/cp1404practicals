from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabels(App):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.dynamic_names = {"Jack", "Frank", "Tom", "Bobby", "John"}

    def build(self):
        self.title = "Dynamic Labels Exercise"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_name_labels()
        return self.root

    def create_name_labels(self):
        for name in self.dynamic_names:
            label = Label(text=name, id=name)
            self.root.ids.dynamic_name_labels.add_widget(label)


DynamicLabels().run()

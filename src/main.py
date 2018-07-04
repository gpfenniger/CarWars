from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty, StringProperty
#Builder.load_file('your_filename')
from kivy.lang import Builder

class CarWars(Widget):
    label_wid = ObjectProperty()
    info = StringProperty()

    def do_action(self):
        self.label_wid.text = 'My label after button press'
        self.info = 'New info text'
        Builder.load_file('./layouts/create_record.kv')
    pass


class CarWarsApp(App):
    def build(self):
        return CarWars(info='Hello world')


if __name__ == '__main__':
    CarWarsApp().run()
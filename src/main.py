from kivy.app import App
from kivy.uix.widget import Widget

class CarWars(Widget):
    pass


class CarWarsApp(App):
    def build(self):
        return CarWars()


if __name__ == '__main__':
    CarWarsApp().run()
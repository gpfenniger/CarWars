from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import *
from kivy.properties import ObjectProperty, StringProperty
#Builder.load_file('your_filename')
from kivy.lang import Builder

class CarWars(Widget):
    label_wid = ObjectProperty()
    info = StringProperty()

    def __init__(self, **kwargs):
        super(CarWars, self).__init__(**kwargs)
        self.bind(pos=self.update_canvas)
        self.bind(size=self.update_canvas)
        self.update_canvas()

    def update_canvas(self, *args):
        grid = []
        for i in range((self.width // 20) - 1):
            grid.append([(i + 1) * 20, 20, (i + 1) * 20, self.height - 20])
        for j in range((self.height // 20) - 1):
            grid.append([20, (j + 1) * 20, self.width - 20, (j + 1) * 20])
        
        # need to reset everything
        self.canvas.clear()
        with self.canvas:
            # Context instructions
            Color(255, 255, 255, 1)
            Rectangle(size=self.size, pos=self.pos)
            # Vertex Instructions
            Color(0, 0, 0, 1)
            for ln in grid: 
                Line(points=ln, width=2)

    def do_action(self):
        self.label_wid.text = 'My label after button press'
        self.info = 'New info text'
       
        
    pass


class CarWarsApp(App):
    def build(self):
        return CarWars(info='Hello world')


if __name__ == '__main__':
    CarWarsApp().run()
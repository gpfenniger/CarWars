from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.graphics import *
from kivy.properties import ObjectProperty, StringProperty
#Builder.load_file('your_filename')
from kivy.lang import Builder

import sys
sys.path.insert(0, './modules/records')

from vehicle_record import Vehicle
from vehicle_record import VehicleBuilder
from vehicle_record import DrawInstructs

class CarWars(Widget):
    label_wid = ObjectProperty()
    info = StringProperty()
    vb = VehicleBuilder()
    v = vb.build_base()
    vehicles = [v]

    def __init__(self, **kwargs):
        super(CarWars, self).__init__(**kwargs)
        self.bind(pos=self.update_canvas)
        self.bind(size=self.update_canvas)
        self.update_canvas()
        self._keyboard = Window.request_keyboard(self._keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_keyboard_down)

    # Key Input
    def _keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard = None

    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        if keycode[1] == 'w':
            self.v.move(10, 'f')
        elif keycode[1] == 'a':
            self.v.angle += 10
        elif keycode[1] == 's':
            self.v.move(10, 'r')
        elif keycode[1] == 'd':
            self.v.angle -= 10
        self.update_canvas()
        return True

    # Canvas
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
                Line(points=ln, width=1)

            Color(255, 0, 0, 1)
            Rectangle(size=[20, 20], pos=[100, 100])

            for vehicle in self.vehicles:
                d = vehicle.draw()
                Rotate(angle=d.angle, origin=d.pos)
                Color(d.color[0], d.color[1], d.color[2], 1)
                Rectangle(size=[d.height, d.width], pos=d.pos)
                Rotate(angle=(0 - d.angle), origin=d.pos)
            

    def do_action(self):
        self.label_wid.text = 'My label after button press'
        self.info = 'New info text'
       
        
    pass


class CarWarsApp(App):
    def build(self):
        return CarWars(info='Hello world')


if __name__ == '__main__':
    CarWarsApp().run()
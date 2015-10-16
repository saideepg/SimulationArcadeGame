# A Floater is Prey; it updates by moving mostly in
#   a straight line, but with random changes to its
#   angle and speed, and displays as ufo.gif (whose
#   dimensions (width and height) are computed by
#   calling .width()/.height() on the PhotoImage


#from PIL.ImageTk import PhotoImage
from prey import Prey
import random
#from turtledemo.nim import randomrow


class Floater(Prey):
    radius = 5
    
    def __init__(self, x, y, width = 10, height = 10):
        Prey.__init__(self, x, y, width, height, 0, 5)
        self.randomize_angle()
        self._color = "red"
    
    def get_color(self):
        return self._color
    
    def change_color(self, color):
        self._color = color
    
    def update(self):
        random_change = random.randint(1,10)
        if random_change in [1,2,3]:
            random_speed = random.randint(1,2)
            if random_speed == 1:
                random_speed = -0.5
            else:
                random_speed = 0.5
            random_angle = random.randint(1,2)
            if random_angle == 1:
                random_angle = -0.5
            else:
                random_angle = 0.5
            if self.get_speed() >= 3 and self.get_speed() <= 7:
                self.set_speed(self.get_speed() + random_speed)
            self.set_angle(self.get_angle() + random_angle)
        self.move()
    
    def display(self,canvas):
        canvas.create_oval(self._x-Floater.radius      , self._y-Floater.radius,
                                self._x+Floater.radius, self._y+Floater.radius,
                                fill=self._color)
    
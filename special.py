'''
When the special button is pressed and a special simulton is added to the simulton : a pink ball of 
radius 15 is added to the simulation. The pink ball moves at a speed of 8 pixels / second and at an angle
of pi/2 radians. The main feature of this simulton is that whenever a prey instance's centre comes inside 
the pink ball i.e. the distance between the centre of the prey and the centre of the pink ball is less than
the radius of the pnik ball, the pink ball changes the color of the prey instance to "yellow" thereby making
it immune (or invisible) to the other prey_catching simultons (black_holes, pulsators and hunters). The pink
ball moves vertically in the simulation for 200 cycles and then removes itself from the simulation and also 
reverts the color of the prey instance (which it earlier changed to yellow) to its original color thereby 
taking back the temporary immunity. 

#### --------HOPE YOU LIKE IT-------------####
'''

#from simulton import Simulton
from mobilesimulton import Mobile_Simulton
#from pulsator import Pulsator
from math import radians
from prey import Prey

class Special(Mobile_Simulton):
    radius = 15
    counter = 200
    
    def __init__(self, x, y, width = 30, height = 30, angle = radians(90), speed = 8):
        Mobile_Simulton.__init__(self, x, y, width, height, angle, speed)
        self._color = '#ff1493'
        self.counter = 0
        self.changed = set()
    
    def contains(self, xy):
        return self.distance(xy) < Special.radius
    
    def update(self, model):
        find_set = model.find(lambda x: isinstance(x, Prey))
        for o in find_set:
            if self.contains(o.get_location()):
                o.change_color("yellow")
                self.changed.add(o)
        self.move()
        self.counter += 1
        if self.counter == Special.counter:
            model.specials.remove(self)
            for changed_o in self.changed:
                for b in model.balls:
                    if b == changed_o:
                        b.change_color("blue")
                        break
                for f in model.floaters:
                    if f == changed_o:
                        f.change_color("red")
                        break
            #model.specials.remove(self)
    
    def display(self,canvas):
        canvas.create_oval(self._x-Special.radius      , self._y-Special.radius,
                                self._x+Special.radius, self._y+Special.radius,
                                fill=self._color)
        
                
# A Black_Hole is a Simulton; it updates by removing
#   any Prey whose center is contained within its radius
#  (returning a set of all eaten simultons), and
#   displays as a black circle with a radius of 10
#   (width/height 20).
# Calling get_dimension for the width/height (for
#   containment and displaying) will facilitate
#   inheritance in Pulsator and Hunter

from simulton import Simulton
from prey import Prey


class Black_Hole(Simulton):
    radius = 10
    
    def __init__(self, x, y, width = 20, height = 20):
        Simulton.__init__(self, x, y, width, height)
        self._color = "black"
    
    def contains(self, xy):
        return self.distance(xy) < (self.get_dimension()[0] / 2)
    
    def update(self, model):
        eaten_set = set()
        find_set = model.find(lambda x: isinstance(x, Prey))
        for o in find_set:
            if self.contains(o.get_location()) and o.get_color() != "yellow":
                if type(o) == model.Ball:
                    model.balls.remove(o)
                elif type(o) == model.Floater:
                    model.floaters.remove(o)
                eaten_set.add(o)
        return eaten_set
        #balls_floaters = model.balls.union(model.floaters)
        #for b in balls_floaters:
        #    if self.contains(b.get_location()):
        #        if type(b) == model.Ball:
        #            model.balls.remove(b)
        #        elif type(b) == model.Floater:
        #            model.floaters.remove(b)
        #        eaten_set.add(b)
        #for f in model.floaters:
        #    if self.contains(f.get_location()):
        #        model.floaters.remove(f)
        #        eaten_set.add(f)
        #return eaten_set
    
    def display(self,canvas):
        canvas.create_oval(self._x-(self.get_dimension()[0]/2)      , self._y-(self.get_dimension()[0]/2),
                                self._x+(self.get_dimension()[0]/2), self._y+(self.get_dimension()[0]/2),
                                fill=self._color)

                
        
        
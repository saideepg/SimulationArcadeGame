# A Pulsator is a Black_Hole; it updates as a Black_Hole
#   does, but also by growing/shrinking depending on
#   whether or not it eats Prey (and removing itself from
#   the simulation if its dimension becomes 0), and displays
#   as a Black_Hole but with varying dimensions


from blackhole import Black_Hole
from prey import Prey


class Pulsator(Black_Hole):
    counter = 30
    
    def __init__(self, x, y):
        Black_Hole.__init__(self, x, y)
        self.counter = 0
    
    def update(self, model):
        eaten_set = set()
        find_set = model.find(lambda x: isinstance(x, Prey))
        for o in find_set:
            if self.contains(o.get_location()) and o.get_color() != "yellow":
                if type(o) == model.Ball:
                    model.balls.remove(o)
                elif type(o) == model.Floater:
                    model.floaters.remove(o)
                self.change_dimension(1, 1)
                self.counter = 0
                eaten_set.add(o)
        if len(eaten_set) == 0:
            self.counter += 1
            if self.counter == Pulsator.counter:
                self.change_dimension(-1, -1)
                self.counter = 0
            if self.get_dimension() == (0, 0):
                model.pulsators.remove(self)
            return set()
        else:          
            return eaten_set
        
    
    
    
    
    
    
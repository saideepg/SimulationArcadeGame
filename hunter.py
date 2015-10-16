# A Hunter is both a  Mobile_Simulton and Pulsator; it updates
#   like a Pulsator, but it also moves (either in a straight line
#   or in pursuit of Prey), and displays as a Pulsator.


from pulsator import Pulsator
from mobilesimulton import Mobile_Simulton
from prey import Prey
from math import atan2


class Hunter(Pulsator,Mobile_Simulton):
    see_distance = 200
    
    def __init__(self, x, y):
        Pulsator.__init__(self, x, y)
        Mobile_Simulton.__init__(self, x, y, 20, 20, 0, 5)
        self.randomize_angle()
    
    def update(self, model):
        eaten_set = set()
        find_set = model.find(lambda x: isinstance(x, Prey))
        dis_prey_tuple = [ ]
        for o in find_set:
            if self.distance(o.get_location()) < Hunter.see_distance and o.get_color() != "yellow":
                dis_prey_tuple.append((self.distance(o.get_location()), o))
        try:
            target = sorted(dis_prey_tuple)[0][1]
            t_x, t_y = target.get_location()
            s_x, s_y = self.get_location()
            target_angle = atan2(t_y - s_y, t_x - s_x)
            self.set_angle(target_angle)
            self.move()
                    
            if self.contains(target.get_location()):
                if type(target) == model.Ball:
                    model.balls.remove(target)
                elif type(target) == model.Floater:
                    model.floaters.remove(target)
                self.change_dimension(1, 1)
                self.counter = 0
                eaten_set.add(target)
                
        except:
            pass
        
        if len(eaten_set) == 0:
            self.counter += 1
            if self.counter == Pulsator.counter:
                self.change_dimension(-1, -1)
                self.counter = 0
            if self.get_dimension() == (0, 0):
                model.hunters.remove(self)
        return eaten_set
    
# A Ball is Prey; it updates by moving in a straight
#   line and displays as blue circle with a radius
#   of 5 (width/height 10).


from prey import Prey


class Ball(Prey):
    radius = 5
    
    def __init__(self, x, y, width = 10, height = 10):
        Prey.__init__(self, x, y, width, height, 0, 5)
        self.randomize_angle()
        self._color = "blue"
    
    def get_color(self):
        return self._color
    
    def change_color(self, color):
        self._color = color
    
    def update(self):
        self.move()
        
    def display(self,canvas):
        canvas.create_oval(self._x-Ball.radius      , self._y-Ball.radius,
                                self._x+Ball.radius, self._y+Ball.radius,
                                fill=self._color)
    
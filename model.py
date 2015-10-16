import controller, sys
import model   #strange, but we need a reference to this module to pass this module to update

from ball      import Ball
from floater   import Floater
from blackhole import Black_Hole
from pulsator  import Pulsator
from hunter    import Hunter
from special   import Special
from tkinter.test.support import simulate_mouse_click


# Global variables: declare them global in functions that assign to them: e.g., ... = or +=
running = False
cycle_count = 0
balls = set()
floaters = set()
blackholes = set()
pulsators = set()
hunters = set()
specials = set()
object_kind = ''
#simultons = set()


#return a 2-tuple of the width and height of the canvas (defined in the controller)
def world():
    return (controller.the_canvas.winfo_width(),controller.the_canvas.winfo_height())

#reset all module variables to represent an empty/stopped simulation
def reset ():
    global running, cycle_count, balls, floaters, blackholes, hunters, pulsators, object_kind, specials
    running = False
    cycle_count = 0
    balls = set()
    floaters = set()
    blackholes = set()
    pulsators = set()
    hunters = set()
    object_kind = ''
    specials = set()
    #simultons = set()


#start running the simulation
def start ():
    global running 
    running = True


#stop running the simulation (freezing it)
def stop ():
    global running
    running = False


#step just one update in the simulation
def step ():
    global cycle_count, balls, floaters, blackholes, pulsators, hunters, specials
    cycle_count += 1
    for b in balls:
        b.update()
    for f in floaters:
        f.update()
    for bh in blackholes:
        bh.update(model)
    for p in pulsators:
        p.update(model)
    for h in hunters:
        h.update(model)
    for s in specials:
        s.update(model)
    if running:
        stop()


#remember the kind of object to add to the simulation when an (x,y) coordinate in the canvas
#  is clicked next (or remember to remove an object by such a click)   
def select_object(kind):
    global object_kind
    object_kind = kind


#add the kind of remembered object to the simulation (or remove any objects that contain the
#  clicked (x,y) coordinate
def mouse_click(x,y):
    global object_kind
    if object_kind == 'Remove':
        try:
            for b in balls:
                if b.contains((x, y)):
                    remove(b)
                    return
            for f in floaters:
                if f.contains((x, y)):
                    remove(f)
                    return
            for bh in blackholes:
                if bh.contains((x, y)):
                    remove(bh)
                    return
            for p in pulsators:
                if p.contains((x,y)):
                    remove(p)
                    return
            for h in hunters:
                if h.contains((x, y)):
                    remove(h)
                    return  
            for s in specials:
                if s.contains((x, y)):
                    remove(s)
                    return
        except:
            return
    else:
        add(eval(object_kind + "(" + str(x) + "," + str(y) + ")"))


#add simulton s to the simulation
def add(s):
    global balls, floaters, blackholes, pulsators, hunters, specials
    if type(s) == Ball:
        balls.add(s)
    elif type(s) == Floater:
        floaters.add(s)
    elif type(s) == Black_Hole:
        blackholes.add(s)
    elif type(s) == Pulsator:
        pulsators.add(s)
    elif type(s) == Hunter:
        hunters.add(s)
    elif type(s) == Special:
        specials.add(s)
    #simultons.add(s)
    

# remove simulton s from the simulation    
def remove(s):
    global balls, floaters, blackholes, pulsators, hunters, specials
    if type(s) == Ball:
        balls.remove(s)
    elif type(s) == Floater:
        floaters.remove(s)
    elif type(s) == Black_Hole:
        blackholes.remove(s)
    elif type(s) == Pulsator:
        pulsators.remove(s)
    elif type(s) == Hunter:
        hunters.remove(s)
    elif type(s) == Special:
        specials.remove(s)
    #simultons.remove(s)
    
    

#find/return a set of simultons that each satisfy predicate p    
def find(p):
    global balls, floaters
    prey = balls.union(floaters)
    find_set = set()
    for o in prey:
        if p(o):
            find_set.add(o)
    return find_set


#call update for every simulton in the simulation
def update_all():
    global cycle_count, balls, floaters, blackholes, pulsators, hunters, specials
    if running:
        cycle_count += 1
        for b in balls:
            b.update()
        for f in floaters:
            f.update()
        for bh in blackholes:
            bh.update(model)
        pulsators_temp = pulsators.copy()
        while pulsators_temp:
            pulsators_temp.pop().update(model)
        hunters_temp = hunters.copy()
        while hunters_temp:
            hunters_temp.pop().update(model)
        for s in specials.copy():
            s.update(model)


#delete from the canvas every simulton in the simulation, and then call display for every
#  simulton in the simulation to add it back to the canvas possibly in a new location: to
#  animate it; also, update the progress label defined in the controller
def display_all():
    global balls, floaters, blackholes, pulsators, hunters, specials
    
    for o in controller.the_canvas.find_all():
        controller.the_canvas.delete(o)
    
    for b in balls:
        b.display(controller.the_canvas)
    
    for f in floaters:
        f.display(controller.the_canvas)
    
    for bh in blackholes:
        bh.display(controller.the_canvas)
    
    for p in pulsators:
        p.display(controller.the_canvas)
    
    for h in hunters:
        h.display(controller.the_canvas)
    
    for s in specials:
        s.display(controller.the_canvas)
    
    simultons_len = len(balls) + len(floaters) + len(blackholes) + len(pulsators) + len(hunters) + len(specials)
    controller.the_progress.config(text=str(cycle_count)+" updates/"+str(simultons_len)+" simultons")

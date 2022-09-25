from GameFrame import Level, Globals
from Objects import Controller2

class ControllerOverlay(Level):
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)
        ControllerOverlays = Controller2(self, 0, 0)
        self.add_room_object(ControllerOverlays)
    def complete(self):
        Globals.next_level = Globals.oldRoom
        self.running = False
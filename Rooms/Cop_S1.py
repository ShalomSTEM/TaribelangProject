from GameFrame import Level, EnumLevels, Globals
import os
from Objects import Cockatoo


class Cop_S1(Level):
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)

        self.set_background_image(os.path.join("CoppleS", 'Copple_Background_1.png'))
        self.load_sound("Copple_1.wav").play()
        self.set_timer(900, self.complete)

        Cockatoo_object = Cockatoo(self, 400, 300)
        self.add_room_object(Cockatoo_object)

        Globals.next_level = EnumLevels.Cop_G1

    def complete(self):
        self.running = False


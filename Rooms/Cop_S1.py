from GameFrame import Level, EnumLevels, Globals
import os
from Objects import Cockatoo


class Cop_S1(Level):
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)

        self.set_background_image(os.path.join("CoppleS", 'Copple_Background_1.png'))
        self.load_sound("Copple_1.ogg").play()
        self.set_timer(300, self.complete)

        self.cockatoo_object = Cockatoo(self, -50, 200)
        self.add_room_object(self.cockatoo_object)
        self.cockatoo_object.x_speed = 5
        self.cockatoo_object.y_speed = 1

        self.set_timer(300, self.kill_bird)

        self.set_timer(60, self.play_bird)

        Globals.next_level = EnumLevels.Cop_G1

    def play_bird(self):
        self.load_sound("BIRD_1.wav").play()

    def kill_bird(self):
        self.delete_object(self.cockatoo_object)

    def complete(self):
        self.running = False


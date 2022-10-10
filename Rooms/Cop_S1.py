from GameFrame import Level, EnumLevels, Globals
import os


class Cop_S1(Level):
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)

        self.set_background_image(os.path.join("CoppleS", 'Copple_Background_1.png'))
        self.load_sound("Copple_1.wav").play()
        self.set_timer(20, self.complete)

        Globals.next_level = EnumLevels.Cop_G1

    def complete(self):
        self.running = False


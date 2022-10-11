from GameFrame import Level, EnumLevels, Globals
import os


class Cop_S2(Level):
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)

        self.set_background_image(os.path.join("CoppleS", 'Copple_Background_2.png'))
        self.load_sound("Copple_2.wav").play()
        self.set_timer(1050, self.complete)

        Globals.next_level = EnumLevels.Cop_G2

    def complete(self):
        self.running = False

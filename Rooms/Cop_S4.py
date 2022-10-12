from GameFrame import Level, EnumLevels, Globals
import os


class Cop_S4(Level):
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)

        self.set_background_image(os.path.join("CoppleS", 'Copple_Background_4.png'))
        self.load_sound("Copple_4.ogg").play()
        self.set_timer(1050, self.complete)

        Globals.next_level = EnumLevels.Home

    def complete(self):
        self.running = False

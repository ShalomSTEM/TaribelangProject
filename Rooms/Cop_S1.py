import os

from GameFrame import Level, TextObject


class Cop_S1(Level):
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)

        self.load_sound("Copple_1.wav").play()

        self.set_background_image(
            os.path.join("Copple Story", "Cop_Background_1.png")
        )
        self.set_timer(1050, self.complete)


    def complete(self):
        self.running = False

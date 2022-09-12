import os

from GameFrame import Level, TextObject, EnumLevels, Globals


class Cop_S2(Level):
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)

        self.set_background_image(
            os.path.join("Copple Story", "Cop_Background_2.png")
        )

        self.set_timer(60, self.complete)

    def complete(self):
        self.running = False



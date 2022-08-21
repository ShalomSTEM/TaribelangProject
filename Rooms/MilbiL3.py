from GameFrame import Level, Globals
import os


class MilbiL3(Level):
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)
        self.set_background_image(
            os.path.join(Globals.milbiL3_alt_path, "PlaceHolderBackgroundMLBL3.png")
        )

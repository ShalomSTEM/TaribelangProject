from GameFrame import Tiles


class MilbiL3(Tiles):
    def __init__(self, screen, joysticks):
        Tiles.__init__(self, screen, joysticks)
        self.set_background_image("PlaceHolderBackgroundMLBL3.png")

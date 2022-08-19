from GameFrame import MLB_Tiles


class MilbiL3(MLB_Tiles):
    def __init__(self, screen, joysticks):
        MLB_Tiles.__init__(self, screen, joysticks)
        self.set_background_image("PlaceHolderBackgroundMLBL3.png")

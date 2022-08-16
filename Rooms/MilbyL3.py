from GameFrame import Level


class MilbyL3(Level):
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)
        self.set_background_image("PlaceHolderBackground.png")

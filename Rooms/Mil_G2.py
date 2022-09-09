from GameFrame import Level, TextObject, Globals, EnumLevels


class Mil_G2(Level):
    def __init__(self, screen, joysticks, direct=False):
        Level.__init__(self, screen, joysticks)

        self.direct = direct
        self.set_background_image(os.path.join("MilbiL2", "ML2_background.jpg"))

        self.set_timer(60, self.complete)

    def complete(self):
        if Globals.direct_select:
            Globals.direct_select = False
            Globals.next_level = EnumLevels.Home
        self.running = False

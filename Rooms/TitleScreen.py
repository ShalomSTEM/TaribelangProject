from GameFrame import Level
from Objects import TitleMilbiButton


class TitleScreen(Level):
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)
        self.set_background_image("MilbiL3/PlaceHolderBackgroundMLBL3.png")
        button1 = TitleMilbiButton(self, 100, 100)
        self.add_room_object(button1)

from GameFrame import Globals, Story, EnumLevels


class Mil_S5(Story):
    def __init__(self, screen, joysticks):
        
        # - Information for Controller Overlay
        self.roomNum = EnumLevels.Mil_S4

        Story.__init__(self, screen, joysticks, "milbi_5.ogg", 'MilbiS', "Milbi_Background_5.png")
        self.set_timer(540, self.complete)

    def complete(self):
        self.running = False
        Globals.next_level = EnumLevels.Home

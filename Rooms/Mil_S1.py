from GameFrame import Globals, Story, EnumLevels


class Mil_S1(Story):
    def __init__(self, screen, joysticks):
        
        # - Information for Controller Overlay
        self.roomNum = EnumLevels.Mil_S1

        Story.__init__(self, screen, joysticks, "Milbi_1.ogg", 'MilbiS', "Milbi_Background_1.png")
        self.set_timer(450, self.complete)

    def complete(self):
        Globals.next_level = EnumLevels.Mil_G1
        self.running = False

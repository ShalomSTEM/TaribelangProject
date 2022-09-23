from GameFrame import Globals, Story, EnumLevels


class Mil_S2(Story):
    def __init__(self, screen, joysticks):
        
        # - Information for Controller Overlay
        self.roomNum = EnumLevels.Mil_S2

        Story.__init__(self, screen, joysticks, "Milbi_2.wav", 'MilbiS', "Milbi_Background_2.png")
        self.set_timer(1050, self.complete)
    def complete(self):
        self.running = False
        Globals.next_level = EnumLevels.Mil_S3

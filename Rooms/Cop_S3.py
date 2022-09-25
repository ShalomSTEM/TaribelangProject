from GameFrame import Globals, Story, EnumLevels

class Cop_S3(Story):
    def __init__(self, screen, joysticks):

        # - Information for Controller Overlay
        self.roomNum = EnumLevels.Cop_S3

        Story.__init__(self, screen, joysticks, "Copple_3.wav", 'CoppleS', "Copple_Background_3.png")
        self.set_timer(900, self.complete)
    def complete(self):
        self.running = False
        Globals.next_level = EnumLevels.Cop_S4

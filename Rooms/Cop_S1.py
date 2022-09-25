from GameFrame import Story, EnumLevels, Globals


class Cop_S1(Story):
    def __init__(self, screen, joysticks):
        
        # - Information for Controller Overlay
        self.roomNum = EnumLevels.Cop_S1

        Story.__init__(self, screen, joysticks, "Copple_1.wav", 'CoppleS', "Copple_Background_1.png")
        self.set_timer(1050, self.complete)
    def complete(self):
        self.running = False
        Globals.next_level = EnumLevels.Cop_S2

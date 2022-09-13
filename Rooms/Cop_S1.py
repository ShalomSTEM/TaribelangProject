from GameFrame import Story


class Cop_S1(Story):
    def __init__(self, screen, joysticks):
        Story.__init__(self, screen, joysticks, "Copple_1.wav", 'Copple Story', "Cop_Background_1.png")
        self.set_timer(1050, self.complete)
    def complete(self):
        self.running = False

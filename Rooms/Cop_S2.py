from GameFrame import Story

class Cop_S2(Story):
    def __init__(self, screen, joysticks):
        Story.__init__(self, screen, joysticks, "Copple_2.wav", 'CoppleS', "Copple_Background_2.png")
        self.set_timer(900, self.complete)
    def complete(self):
        self.running = False



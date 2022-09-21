from GameFrame import Story

class Cop_S4(Story):
    def __init__(self, screen, joysticks):
        Story.__init__(self, screen, joysticks, "Copple_4.wav", 'CoppleS', "Copple_Background_4.png")
        self.set_timer(930, self.complete)
    def complete(self):
        self.running = False

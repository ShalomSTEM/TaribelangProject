from GameFrame import Story

class Cop_S3(Story):
    def __init__(self, screen, joysticks):
        Story.__init__(self, screen, joysticks, "Copple_3.wav", 'Copple Story', "Cop_Background_3.png")
        self.set_timer(900, self.complete)
    def complete(self):
        self.running = False

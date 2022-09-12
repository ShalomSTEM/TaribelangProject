from GameFrame import Story


class Mil_S3(Story):
    def __init__(self, screen, joysticks):
        Story.__init__(self, screen, joysticks, "Milbi_3.wav", 'MilbiS', "Milbi_Background_3.png")
        self.set_timer(1050, self.complete)
    def complete(self):
        self.running = False

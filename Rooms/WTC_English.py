from GameFrame import Level, Globals


class WTC_English(Level):
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)

        self.set_background_image("EnglsihWTC.png")

        self.set_timer(300, self.completed)

    def completed(self):
        self.running = False

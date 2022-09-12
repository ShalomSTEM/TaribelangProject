import os

from GameFrame import Level, TextObject


class Story(Level):
    def __init__(self, screen, joysticks, sound, folder, image):
        Level.__init__(self, screen, joysticks)

        self.load_sound("Milbi_4.wav").play()

        self.set_background_image(
            os.path.join("MilbiS", "Milbi_Background_4.png")
        )
        self.set_timer(1050, self.complete)


    def complete(self):
        self.running = False

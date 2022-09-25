import os

from GameFrame import Level, TextObject


class Story(Level):
    def __init__(self, screen, joysticks, sound, folder, image):
        Level.__init__(self, screen, joysticks)
        self.load_sound(sound).play()

        self.set_background_image(
            os.path.join(folder, image)
        )


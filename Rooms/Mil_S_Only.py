from GameFrame import Level, Globals, EnumLevels
import os

class Mil_S_Only(Level):
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)

        self.set_background_image(os.path.join("MilbiS", 'Milbi_Full_Story.png'))
        self.load_sound("Milbi_full_story.ogg").play()
        self.set_timer(3900, self.complete)

        Globals.next_level = EnumLevels.Home

    def complete(self):
        self.running = False

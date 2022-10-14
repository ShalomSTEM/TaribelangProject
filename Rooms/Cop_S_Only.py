from GameFrame import Level, Globals, EnumLevels
import os


class Cop_S_Only(Level):
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)

        # Replace image with one that has the whole storyt
        self.set_background_image(os.path.join("CoppleS", 'Copple_StoryOnly_Background.png'))
        self.load_sound("Copple_full.ogg").play()
        self.set_timer(4890, self.complete)

        Globals.next_level = EnumLevels.Home

    def complete(self):
        self.running = False

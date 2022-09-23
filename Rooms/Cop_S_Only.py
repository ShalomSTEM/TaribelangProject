from GameFrame import Level, Globals, EnumLevels
import os

class Cop_S_Only(Level):
    # DONE BY SAM
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)
        self.index = 0
        self.times = [0, 1050, 900, 900, 930]
        self.updateStory()

        # - Information for Controller Overlay
        self.roomNum = EnumLevels.Cop_S_Only

    def updateStory(self):
        self.index += 1
        self.load_sound(f"Copple_{self.index}.wav").play()
        self.set_background_image(os.path.join("CoppleS", f"Copple_Background_{self.index}.png"))
        if self.index == 4:
            self.set_timer(self.times[self.index], self.complete)
        else:
            self.set_timer(self.times[self.index], self.updateStory)
            
    def complete(self):
        Globals.next_level = EnumLevels.Home
        self.running = False

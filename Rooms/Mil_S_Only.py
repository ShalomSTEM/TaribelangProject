from GameFrame import Level, Globals, EnumLevels
import os

class Mil_S_Only(Level):
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)
        self.index = 0
        # Replace with proper times later
        self.times = [0, 1050, 1050, 1050, 1050]
        self.updateStory()

    def updateStory(self):
        self.index += 1
        self.load_sound(f"Milbi_{self.index}.wav").play()
        self.set_background_image(os.path.join("MilbiS", f"Milbi_Background_{self.index}.png"))
        if self.index == 4:
            self.set_timer(self.times[self.index], self.complete)
        else:
            self.set_timer(self.times[self.index], self.updateStory)
            
    def complete(self):
        Globals.next_level = EnumLevels.Home
        self.running = False

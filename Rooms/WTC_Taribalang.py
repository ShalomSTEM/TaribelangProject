from GameFrame import Level, Globals
import os


class WTC_Taribalang(Level):
    def __init__(self, screen, joystick):
        Level.__init__(self, screen, joystick)
        self.set_background_image(os.path.join(Globals.WTC_path, "WTC_Taribelang.png"))

        self.set_timer(300, self.completed)

    def completed(self):
        self.running = False

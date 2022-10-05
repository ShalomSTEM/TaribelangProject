from GameFrame import RoomObject, Globals
import os


class CopSwimBG(RoomObject):
    def __init__(self, room, x, y):
        super().__init__(room, x, y)

        image = self.load_image(os.path.join("CopG3", "G3_bg.png"))
        self.set_image(image, Globals.SCREEN_WIDTH, Globals.SCREEN_HEIGHT)

        self.depth = -150

        self.x_speed = -4

    def step(self):
        if self.x <= -Globals.SCREEN_WIDTH:
            self.x = Globals.SCREEN_WIDTH

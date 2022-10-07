import random
import os
from GameFrame import RoomObject
from GameFrame import Globals


class CopG1_Tree (RoomObject):
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)

        self.image = self.load_image(os.path.join('CoppleL1', "Eucalytpus Tree.png"))
        self.set_image(self.image, 224, 169)
        self.image_set = True

        self.depth = 50

        self.y_speed = 4

        self.hitbox = (self.x, self.y, 64, 64)


    def step(self):
        if self.y >= Globals.SCREEN_HEIGHT:
            self.y = 0 - self.height*2
            self.x = random.randint(0, Globals.SCREEN_WIDTH - self.width)

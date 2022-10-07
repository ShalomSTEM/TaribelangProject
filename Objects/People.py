from GameFrame import RoomObject, Globals
import os
from Objects.Dance_MLBL3 import DanceArrows_MLBL3, DanceBG_MLBL3, Dance_MLBL3


class ML2_People(RoomObject):
    def __init__(self, room, x, y, img):
        RoomObject.__init__(self, room, x, y)
        self.set_image(os.path.join("Images", "MilbiL2", img), height=100, width=100)
        print(self.x, self.y)

    def update(self):
        self.y_speed = self.y_speed + self.gravity
        self.x += self.x_speed
        self.y += self.y_speed
        self.rect.x = self.x
        self.rect.y = self.y
        if self.y == 280 and self.x == 880:
            self.x = 100
            self.y = 100
        # if self.y == 312 and self.x == 632:
        #     self.x = 350
        #     self.y = 650
        # if self.y == 280 and self.x == 632:
        #     self.x = 350
        #     self.y = 650
        # if self.y == 248 and self.x == 632:
        #     self.x = 350
        #     self.y = 650

        # elif self.y <= 330 and self.allowInput == False:
        #     self.y_speed = 0
        #     self.room.deleteObjects1(True, False)
        # else:
        #     pass

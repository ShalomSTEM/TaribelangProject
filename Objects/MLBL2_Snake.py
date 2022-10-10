from GameFrame import RoomObject, Globals
import os


class MLBL2_Snake(RoomObject):
    def __init__(self, room, x, y, img, top, bottom, start):
        RoomObject.__init__(self, room, x, y)
        image = self.load_image(os.path.join("MilbiL2", img))
        self.set_image(image, 25, 25)
        self.top = top
        self.bottom = bottom
        if self.bottom and start:
            self.x = 1360
        if self.top and start:
            self.x = 900
            self.y = 200

    def update(self):
        self.y_speed = self.y_speed + self.gravity
        self.x += self.x_speed
        self.y += self.y_speed
        self.rect.x = self.x
        self.rect.y = self.y
        if self.room.Dance:
            if self.bottom:
                self.x += 0.1
            if self.top:
                self.x -= 0.1


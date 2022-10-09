from GameFrame import RoomObject, Globals
import os
from Objects.Dance_MLBL3 import DanceArrows_MLBL3, DanceBG_MLBL3, Dance_MLBL3


class ML2_People(RoomObject):
    def __init__(self, room, x, y, img):
        RoomObject.__init__(self, room, x, y)
        #self.handle_mouse_events = True
        self.pos = 0
        self.room.calcPos(x, y, self)
        if self.x == 632 and self.y == 312:
            self.yes = True
            self.set_image(os.path.join("Images", "MilbiL1", "sprite_0.png"), 100, 100)
        else:
            self.yes = False
            self.set_image(os.path.join("Images", "MilbiL2", img), height=100, width=100)
        # print(self.x, self.y)
        self.set_timer(40, self.updatePos)
    #def mouse_event(self, mouse_x,mouse_y,button_left,button_middle,button_right):
    #    print(mouse_x, mouse_y)
    def updatePos(self):
        self.pos += 1
        if self.pos == 18:
            self.pos = 0
        if self.yes:
            print(self.room.peoplePos[self.pos][0], self.room.peoplePos[self.pos][1], self.pos)
        self.x = self.room.peoplePos[self.pos][0]
        self.y = self.room.peoplePos[self.pos][1]
        self.set_timer(40, self.updatePos)
    def update(self):
        self.y_speed = self.y_speed + self.gravity
        self.x += self.x_speed
        self.y += self.y_speed
        self.rect.x = self.x
        self.rect.y = self.y
        if self.y == 280 and self.x == 880:
            self.x = 100
            self.y = 100
from GameFrame import RoomObject, Globals
import os
from Objects.Dance_MLBL3 import DanceArrows_MLBL3, DanceBG_MLBL3, Dance_MLBL3


class ML2_People(RoomObject):
    def __init__(self, room, x, y, num):
        RoomObject.__init__(self, room, x, y)
        self.num = num
        self.pos = 0
        self.aniIndex = 1
        self.room.calcPos(x, y, self)
        self.setnum()
        
    
    def setnum(self):
        if self.num == 1:
            self.set_image(os.path.join("Images", "MilbiL2", "MLB2_1_1.png"), height=100, width=100)
        if self.num == 2:
            self.set_image(os.path.join("Images", "MilbiL2", "MLB2_2_1.png"), height=100, width=100)
        if self.num == 3:
            self.set_image(os.path.join("Images", "MilbiL2", "MLB2_3_1.png"), height=100, width=100)
        if self.num == 4:
            self.set_image(os.path.join("Images", "MilbiL2", "MLB2_4_1.png"), height=100, width=100)
        if self.num == 5:
            self.set_image(os.path.join("Images", "MilbiL2", "MLB2_5_1.png"), height=100, width=100)
        self.set_timer(40, self.updatePos)
        self.set_timer(10, self.animate)

    def updatePos(self):
        if not self.room.danceEnd:
            if self.room.startMoving:
                self.pos += 1
                if self.pos == 18:
                    self.pos = 0
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
    def animate(self):
        if self.room.startMoving and not self.room.danceEnd:
            self.set_image(os.path.join("Images", "MilbiL2", f"MLB2_{self.num}_{self.aniIndex}.png"), 100, 100)
            self.aniIndex += 1
            if self.aniIndex == 5:
                self.aniIndex = 1
        self.set_timer(10, self.animate)
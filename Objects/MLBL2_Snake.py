from GameFrame import RoomObject, Globals
import os


class MLBL2_SnakeTurtle(RoomObject):
    def __init__(self, room, x, y, img, top, bottom, start, turtle):
        RoomObject.__init__(self, room, x, y)
        image = self.load_image(os.path.join("MilbiL2", img))
        self.set_image(image, 25, 25)
        self.turtle = turtle
        self.top = top
        self.bottom = bottom
        self.img_index = 0
        if self.top and start:
            self.x = 1100
            self.y = 200
        if self.bottom and start:
            self.x = 540
            self.y = 650
        self.setup = False
        self.updatePos()
        self.animate()

    def updatePos(self):
        if self.room.Dance:
            if self.top:
                if self.x >= 550:
                    self.x_speed = -1.2
                elif self.x <= 549:
                    self.x = 540
                    self.y = 650
                    self.top = False
                    self.bottom = True
                    self.x_speed = 1.2
            if self.bottom:
                if self.x <= 1090:
                    self.x_speed = 1.2
                elif self.x >= 1090:
                    self.bottom = False
                    self.top = True
                    self.x = 1100
                    self.y = 200
                    self.x_speed = -1.2
        if self.room.danceEnd and not self.setup and self.turtle:
            self.room.Dance = False
            self.setup = True
            self.x = 815
            self.y = 150
            self.x_speed = 1.5
            self.y_speed = 0.5
        if self.room.danceEnd and not self.setup and not self.turtle:
            self.setup = True
            self.x = 275
            self.y = 200
            self.x_speed = 0
        self.set_timer(10, self.updatePos)
    def animate(self):
        if self.turtle:
            if self.top:
                self.img_index += 1
                if self.img_index == 3:
                    self.img_index = 1
                self.set_image(os.path.join("Images", "MilbiL2", f'turtle_{self.img_index}_top.png'), 32, 32)
            if self.bottom:
                self.img_index += 1
                if self.img_index == 3:
                    self.img_index = 1
                self.set_image(os.path.join("Images", "MilbiL2", f'turtle_{self.img_index}_bottom.png'), 32, 32)
        else:
            if self.top:
                self.set_image(os.path.join("Images", "MilbiL2", "ML2_Snake_top.png"), 32, 32)
            elif self.bottom:
                self.set_image(os.path.join("Images", "MilbiL2", "ML2_Snake_bottom.png"), 32, 32)
        self.set_timer(5, self.animate)
                
from random import randrange
import pygame
from GameFrame import RoomObject, Globals
import os


class Turtle_MLBL2(RoomObject):
    def __init__(self, room, x, y, img, top, bottom, start):
        RoomObject.__init__(self, room, x, y)
        image = self.load_image(os.path.join("MilbiL2", img))
        self.set_image(image, 25, 25)
        self.top = top
        self.bottom = bottom
        if self.bottom and start:
            self.x = 1100
            self.y = 200
        if self.top and start:
            self.x = 200
            self.y = 650
        self.updatePos()

    def updatePos(self):
        if self.room.Dance:
            if self.bottom:
                if self.x >= 550:
                    self.x_speed = -1.2
                elif self.x <= 549:
                    self.x = 200
                    self.y = 650
                    self.top = True
                    self.bottom = False
                    self.x_speed = 1.2
            if self.top:
                if self.x >= 1090:
                    self.x_speed = 1.2
                elif self.x >= 1090:
                    self.x = 1100
                    self.y = 200
                    self.top = False
                    self.bottom = True
                    self.x_speed = -1.2
        elif self.room.danceEnd:
            pass
        self.set_timer(10, self.updatePos)
                
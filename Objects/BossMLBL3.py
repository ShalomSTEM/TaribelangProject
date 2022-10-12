from GameFrame import RoomObject, Globals
from Objects.ORB_MLBL3 import ORB_MLBL3
import os
from random import randrange


class BossMLBL3(RoomObject):
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)
        self.range = range(1, 359)
        boss = self.load_image(os.path.join("MilbiL3", "front_1.png"))
        self.set_image(boss, 256, 256)
        self.new_orb = ORB_MLBL3(self.room, 500, 500)
        self.orbIndex = 0
        self.set_timer(5, self.startOrb)
        self.imgIndex = 0
        self.animate()


    def animate(self):
        self.imgIndex += 1
        if self.imgIndex == 3:
            self.imgIndex = 1
        self.set_image(os.path.join("Images", "MilbiL3", f'boss_{self.imgIndex}.png'), 256, 256)
        self.set_timer(15, self.animate)

    def startOrb(self):
        self.orbIndex += 1
        if self.orbIndex == 51:
            self.orbIndex = 50
        else:
            self.new_orb = ORB_MLBL3(self.room, self.rect.centerx, self.rect.centery)
            self.room.add_room_object(self.new_orb)
            angle = randrange(1, 359, 1)
            self.new_orb.rotate(angle)
            self.new_orb.x_speed, self.new_orb.y_speed = self.get_direction_coordinates(angle, 5)
            self.set_timer(5, self.startOrb)




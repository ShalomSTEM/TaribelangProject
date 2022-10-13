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
        self.imgIndex = 0
        self.images = []
        self.images.append(self.load_image(os.path.join("MilbiL3", 'boss_left_1.png')))
        self.images.append(self.load_image(os.path.join("MilbiL3", 'boss_left_2.png')))
        self.images.append(self.load_image(os.path.join("MilbiL3", 'boss_left_3.png')))
        self.images.append(self.load_image(os.path.join("MilbiL3", 'boss_left_4.png')))
        self.images.append(self.load_image(os.path.join("MilbiL3", 'boss_left_5.png')))
        self.images.append(self.load_image(os.path.join("MilbiL3", 'boss_left_6.png')))

        self.can_orb = False
        self.flipped = False

        self.animate()

    def animate(self):
        if not self.flipped:
            self.launch_orb()
            self.imgIndex += 1
            if self.imgIndex == 6:
                self.imgIndex = 0
                if self.can_orb:
                    self.can_orb = False
                    self.set_timer(30, self.launch_orb)
                else:
                    self.can_orb = True
            self.set_image(self.images[self.imgIndex], 256, 256)
            self.set_timer(15, self.animate)

    def launch_orb(self):
        new_orb = ORB_MLBL3(self.room, self.rect.centerx, self.rect.centery)

        angle = new_orb.get_rotation_to_coordinate(self.room.player_x, self.room.player_y)
        new_orb.x_speed, new_orb.y_speed = new_orb.get_direction_coordinates(angle, 5)

        self.room.add_room_object(new_orb)
        self.room.room_items.append(new_orb)

    def flip(self):
        self.flipped = True
        self.rotate(45)
        self.set_timer(10, self.flip2)

    def flip2(self):
        self.rotate(45)
        self.set_timer(10, self.flip3)

    def flip3(self):
        self.rotate(45)
        self.set_timer(10, self.flip4)

    def flip4(self):
        self.rotate(45)
        self.set_timer(60, self.room.complete)

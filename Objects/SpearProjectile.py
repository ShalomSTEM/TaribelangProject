import os

from GameFrame import RoomObject
from GameFrame import Globals


class SpearProjectile(RoomObject):
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)

        image = self.load_image(os.path.join("MilbiL3","Spear.png"))
        self.set_image(image, 64, 64)

        self.y_speed = -8

        # Register for collision with Enemy plane
        self.register_collision_object("BossMLBL3")

    def step(self):
        if self.y < 0 - self.height:
            self.room.delete_object(self)

    def handle_collision(self, other, other_type):
        if other_type == "BossMLBL3":
            self.room.explosion_sound.play()
            Globals.destroyed_count += 1
            if Globals.destroyed_count >= 10:
                self.room.running = False
                Globals.total_count = 0
                Globals.destroyed_count = 0

            self.room.delete_object(other)
            self.room.delete_object(self)

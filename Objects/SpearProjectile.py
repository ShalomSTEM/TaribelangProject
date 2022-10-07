import os

from GameFrame import RoomObject
from GameFrame import Globals


class SpearProjectile(RoomObject):
    def __init__(self, room, x, y, milbi_boss):
        RoomObject.__init__(self, room, x, y)

        image = self.load_image(os.path.join("MilbiL3", "Spear.png"))
        self.set_image(image, 12, 34)

        # Register for collision with Enemy plane
        self.register_collision_object("BossMLBL3")

        angle = self.get_rotation_to_coordinate(milbi_boss.rect.centerx, milbi_boss.rect.centery)
        self.rotate(angle)
        self.x_speed, self.y_speed = self.get_direction_coordinates(angle, 5)

    def step(self):
        if self.y < 0 - self.height:
            self.room.delete_object(self)

    def handle_collision(self, other, other_type):
        if other_type == "BossMLBL3":
            Globals.destroyed_count += 1
            if Globals.destroyed_count >= 10:
                self.room.running = False
                Globals.total_count = 0
                Globals.destroyed_count = 0

            self.room.delete_object(other)
            self.room.delete_object(self)

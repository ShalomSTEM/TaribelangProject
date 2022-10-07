import os

from GameFrame import RoomObject
from GameFrame import Globals


class SpearProjectile(RoomObject):
    def __init__(self, room, x, y, milbi_boss):
        RoomObject.__init__(self, room, x, y)

        image = self.load_image(os.path.join("MilbiL3", "Spear.png"))
        self.set_image(image, 64, 64)

        # Register for collision with Enemy plane
        self.register_collision_object("BossMLBL3")

        print(self.curr_rotation)
        print(self.angle)
        print()
        self.rotate_to_coordinate(milbi_boss.x, milbi_boss.y)
        print(self.curr_rotation)
        self.set_direction(self.curr_rotation + 180, 6)
        print(self.angle)
        print()
        print()

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

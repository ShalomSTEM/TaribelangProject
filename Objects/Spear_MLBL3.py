import os

from GameFrame import RoomObject, Globals


class Spear_MLBL3(RoomObject):
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)
        image = self.load_image(os.path.join("MilbiL3", "Spear.png"))
        self.set_image(image, 32, 32)

        self.block_right = False
        self.block_left = False
        self.block_up = False
        self.block_down = False

        self.register_collision_object("Player_MLBL3")

    def handle_collision(self, other, other_type):

        if other_type == "Player_MLBL3":

            if self.collides_at(self, 4, 0, "Player_MLBL3") and not self.block_right:
                self.block_right = True
                if self.x < 596:
                    self.remove_object(self)

            if self.collides_at(self, -4, 0, "Player_MLBL3") and not self.block_left:
                self.block_left = True
                if self.x >= 206:
                    self.remove_object(self)

            if self.collides_at(self, 0, 4, "Player_MLBL3") and not self.block_down:
                self.block_down = True
                if self.y <= 446:
                    self.remove_object(self)

            if self.collides_at(self, 0, -4, "Player_MLBL3") and not self.block_up:
                self.block_up = True
                if self.y >= 154:
                    self.remove_object(self)

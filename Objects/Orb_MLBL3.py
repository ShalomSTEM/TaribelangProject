import os

from GameFrame import RoomObject, Globals


class Orb_MLBL3(RoomObject):
    def __init__(self, room, x, y, player):
        RoomObject.__init__(self, room, x, y)
        image = self.load_image(os.path.join("MilbiL3", "Orb_MLBL3.png"))
        self.set_image(image, 32, 32)
        self.player = player
        self.img_index = 0

        self.LEFT = 0
        self.RIGHT = 1
        self.UP = 2
        self.DOWN = 3

        self.facing = 4



        self.move_to_player_count = 0

        self.block_right = False
        self.block_left = False
        self.block_up = False
        self.block_down = False

        self.moving = False

    def move(self):
        self.move_to_player_count += 1
        if self.move_to_player_count == 3 or \
                abs(self.player.x - self.x) > 400 or \
                abs(self.player.y - self.y) > 400:
            self.move_towards_player()
            self.move_to_player_count = 0

    def move_towards_player(self):
        x = self.player.x
        y = self.player.y
        if abs(x) < abs(y):
            if y > 0:
                self.move_down()
            else:
                self.move_up()
        else:
            if x > 0:
                self.move_right()
            else:
                self.move_left()

    def move_right(self):
        self.facing = self.RIGHT
        self.x_speed += Globals.ORB_move_speed

    def move_left(self):
        self.facing = self.LEFT
        self.x_speed -= Globals.ORB_move_speed

    def move_up(self):
        self.facing = self.UP
        self.y_speed -= Globals.ORB_move_speed

    def move_down(self):
        self.facing = self.DOWN
        self.y_speed += Globals.ORB_move_speed

from GameFrame import Bot, Globals
import random

from Objects import Player_MLBL3


class Red1(Bot):
    def __init__(self, x, y):
        Bot.__init__(self, x, y)
        self.initial_wait = random.randint(30, 90)
        self.wait_count = 0

    def tick(self):
        if self.wait_count < self.initial_wait:
            self.wait_count += 1

        elif self.rect.right >= Globals.SCREEN_WIDTH / 2:
            self.turn_towards(self.starting_x - 400, self.starting_y, Globals.FAST)
            self.drive_forward(Globals.FAST)
        else:
            self.turn_towards(Player_MLBL3.x, Player_MLBL3.y, Globals.FAST)
            self.drive_forward(Globals.FAST)

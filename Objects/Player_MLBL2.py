import pygame
from GameFrame import RoomObject, Globals
import os


class Player_MLBL2(RoomObject):
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)

        player = self.load_image(os.path.join("MilbiL1", "sprite_0.png"))
        self.set_image(player, 100, 100)

        # Load player animation images
        self.down = []
        self.down.append(self.load_image(os.path.join("MilbiL1", "sprite_0.png")))
        self.up = []
        self.up.append(self.load_image(os.path.join("MilbiL1", "sprite_2.png")))
        self.left = []
        self.left.append(self.load_image(os.path.join("MilbiL1", "sprite_1.png")))
        self.right = []
        self.right.append(self.load_image(os.path.join("MilbiL1", "sprite_3.png")))

        self.img_index = 0

        self.LEFT = 0
        self.RIGHT = 1
        self.UP = 2
        self.DOWN = 3

        self.facing = 4

        self.handle_key_events = True

        self.register_collision_object('Block')

        self.block_right = False
        self.block_left = False
        self.block_up = False
        self.block_down = False

        self.moving = False
        self.animate()

    def step(self):
        self.block_right = False
        self.block_left = False
        self.block_up = False
        self.block_down = False
        self.facing = 6

    def handle_collision(self, other, other_type):
        if other_type == 'Block':

            if self.collides_at(self, 4, 0, 'Block') and not self.block_right:
                self.block_right = True
                if self.x < 596:
                    self.x = self.prev_x
                else:
                    self.move_left()

            if self.collides_at(self, -4, 0, 'Block') and not self.block_left:
                self.block_left = True
                if self.x >= 206:
                    self.x = self.prev_x
                else:
                    self.move_right()

            if self.collides_at(self, 0, 4, 'Block'):
                self.block_down = True
                if self.y <= 446:
                    self.y = self.prev_y
                else:
                    self.move_up()

            if self.collides_at(self, 0, -4, 'Block') and not self.block_up:
                self.block_up = True
                if self.y >= 154:
                    self.y = self.prev_y
                else:
                    self.move_down()

    def key_pressed(self, key):
        if key[pygame.K_LEFT]:
            self.move_left()
            self.facing = self.LEFT
        elif key[pygame.K_RIGHT]:
            self.move_right()
            self.facing = self.RIGHT
        elif key[pygame.K_UP]:
            self.move_up()
            self.facing = self.UP
        elif key[pygame.K_DOWN]:
            self.move_down()
            self.facing = self.DOWN

    def joy_pad_signal(self, p1_buttons, p2_buttons):
        if p1_buttons[11] < -0.5:
            self.move_right()
        elif p1_buttons[11] > 0.5:
            self.move_left()

    def move_right(self):
        if self.x < 6000:
            self.x += Globals.move_speed


    def move_left(self):
        if self.x > 0:
            self.x -= Globals.move_speed


    def move_up(self):
        if self.y > 0:
            self.y -= Globals.move_speed


    def move_down(self):
        if self.y < 4500:
            self.y += Globals.move_speed


    def animate(self):
        self.img_index += 1
        self.img_index %= 4
        if self.facing == self.LEFT:
            self.set_image(self.left[self.img_index], 100, 100)
        elif self.facing == self.RIGHT:
            self.set_image(self.right[self.img_index], 100, 100)
        elif self.facing == self.UP:
            self.set_image(self.up[self.img_index], 100, 100)
        elif self.facing == self.DOWN:
            self.set_image(self.down[self.img_index], 100, 100)
        else:
            self.set_image(self.down[0], 100, 100)

        self.set_timer(3, self.animate)

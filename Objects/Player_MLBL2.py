from random import randrange
import pygame
from GameFrame import RoomObject, Globals
import os


class Player_MLBL2(RoomObject):
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)

        self.allowInput = False
        self.allowInputs = False
        player = self.load_image(os.path.join("MilbiL2", "ML2_wallaby_left.png"))
        self.set_image(player, 50, 50)

        # Load player animation images
        self.down = [self.load_image(os.path.join("MilbiL2", "ML2_wallaby_right.png")), self.load_image(os.path.join("MilbiL2", "ML2_wallaby_right.png"))]
        self.up = [self.load_image(os.path.join("MilbiL2", "ML2_wallaby_left.png")), self.load_image(os.path.join("MilbiL2", "ML2_wallaby_left.png"))]
        self.left = [self.load_image(os.path.join("MilbiL2", "ML2_wallaby_left.png")), self.load_image(os.path.join("MilbiL2", "ML2_wallaby_left.png"))]
        self.right = [self.load_image(os.path.join("MilbiL2", "ML2_wallaby_right.png")), self.load_image(os.path.join("MilbiL2", "ML2_wallaby_right.png"))]

        self.img_index = 0

        self.LEFT = 0
        self.RIGHT = 1
        self.UP = 2
        self.DOWN = 3

        self.facing = 4

        self.handle_key_events = True

        # self.register_collision_object('Block')
        self.block_right = False
        self.block_left = False
        self.block_up = False
        self.block_down = False

        self.moving = False
        self.animate()

    def prestep(self):
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

    def update(self):
        self.y_speed = self.y_speed + self.gravity
        self.x += self.x_speed
        self.y += self.y_speed
        self.rect.x = self.x
        self.rect.y = self.y
        if self.y > 330 and self.allowInput == False:
            self.y_speed = -1.2
            self.facing = self.UP
        elif self.y <= 330 and self.allowInput == False:
            self.y_speed = 0
            self.allowInput = True
            self.room.deleteObjects1(True, False)
        
    def key_pressed(self, key):
        if key[pygame.K_LEFT]:
            if self.allowInputs:
                self.x -= 4
                self.facing = self.LEFT
        elif key[pygame.K_RIGHT]:
            if self.allowInputs:
                self.x += 4
                self.facing = self.RIGHT
        elif key[pygame.K_UP]:
            if self.allowInputs: 
                self.y -= 4
                self.facing = self.UP
        elif key[pygame.K_DOWN]:
            if self.allowInputs:
                self.y += 4
                self.facing = self.DOWN

    def joy_pad_signal(self, p1_buttons, p2_buttons):
        if p1_buttons[11] < -0.5:
            pass
        elif p1_buttons[11] > 0.5:
            pass

    def animate(self):
        #self.img_index += 1
        #self.img_index %= 4
        if self.room.Dance:
            pass
        else:
            if self.facing == self.LEFT:
                self.set_image(self.left[self.img_index], 50, 50)
            elif self.facing == self.RIGHT:
                self.set_image(self.right[self.img_index], 50, 50)
            elif self.facing == self.UP:
                self.set_image(self.up[self.img_index], 50, 50)
            elif self.facing == self.DOWN:
                self.set_image(self.down[self.img_index], 50, 50)
            else:
                self.set_image(self.down[0], 50, 50)

        self.set_timer(5, self.animate)

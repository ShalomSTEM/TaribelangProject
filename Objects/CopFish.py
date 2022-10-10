import pygame

from GameFrame import RoomObject, Globals
import os


class CopFish(RoomObject):
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)

        self.facing = 1
        self.image_count = 0

        self.images = [
            [
                self.load_image(os.path.join('CopG3', 'Up1.png')),
                self.load_image(os.path.join('CopG3', 'Up2.png'))
            ],
            [
                self.load_image(os.path.join('CopG3', 'Straight1.png')),
                self.load_image(os.path.join('CopG3', 'Straight2.png'))
            ],
            [
                self.load_image(os.path.join('CopG3', 'Down1.png')),
                self.load_image(os.path.join('CopG3', 'Down2.png'))
            ]
        ]

        self.set_image(self.images[1][1], 130, 72)

        self.animate()

        self.depth = 100

        self.handle_key_events = True

        self.register_collision_object('CopRock')
        self.register_collision_object('CopLog')
        self.register_collision_object('CopLog_Short')
        self.register_collision_object('Cop_Seaweed')
        self.register_collision_object('CopStick')
        self.register_collision_object('Waterlily')

    def prestep(self):
        self.facing = 1

    def key_pressed(self, key):
        if key[pygame.K_UP]:
            if self.y > 50:
                self.y -= 4
                self.facing = 0

        if key[pygame.K_DOWN]:
            if self.y < Globals.SCREEN_HEIGHT - 150:
                self.y += 4
                self.facing = 2

        if key[pygame.K_RIGHT]:
            if self.x < Globals.SCREEN_WIDTH / 2 - 150:
                self.x += 4

        if key[pygame.K_LEFT]:
            if self.x > 10:
                self.x -= 4
        if key[pygame.K_n]:
            self.room.complete()

    def joy_pad_signal(self, p1_buttons, p2_buttons):
        if p1_buttons[11] < -0.5:
            if self.x > 10:
                self.x -= 4
        elif p1_buttons[11] > 0.5:
            if self.x < Globals.SCREEN_WIDTH / 2 - 150:
                self.x += 4
        if p1_buttons[10] < - 0.5:
            if self.y > 50:
                self.y -= 4
                self.facing = 0
        elif p1_buttons[10] > 0.5:
            if self.y < Globals.SCREEN_HEIGHT - 150:
                self.y += 4
                self.facing = 2

    def handle_collision(self, other, other_type):
        self.room.remove_points()
        self.delete_object(other)

    def animate(self):
        if self.image_count:
            self.image_count = 0
        else:
            self.image_count = 1

        width = 130
        height = 72
        if self.facing == 1:
            height = 52
        self.set_image(self.images[self.facing][self.image_count], width, height)
        self.set_timer(5, self.animate)

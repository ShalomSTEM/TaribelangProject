import pygame

from GameFrame import RoomObject, Globals
import os


class CopFish(RoomObject):
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)

        #self.img_up = self.load_image(os.path.join('CopG3', 'CopFish_Up.png'))
        self.img_flat = self.load_image(os.path.join('CopG3', 'CopFish.png'))
        #self.img_down = self.load_image(os.path.join('CopG3', 'CopFish_Down.png'))
        self.set_image(self.img_flat, 65, 36)

        self.depth = 100

        self.handle_key_events = True

        self.register_collision_object('CopRock')
        self.register_collision_object('CopLog')
        self.register_collision_object('CopLog_Short')
        self.register_collision_object('Cop_Seaweed')
        self.register_collision_object('CopStick')
        self.register_collision_object('Waterlily')

    def prestep(self):
        self.set_image(self.img_flat, 65, 36)

    def key_pressed(self, key):
        if key[pygame.K_UP]:
            if self.y > 50:
                self.y -= 4
                #self.set_image(self.img_up, 65, 36)
        if key[pygame.K_DOWN]:
            if self.y < Globals.SCREEN_HEIGHT - 150:
                self.y += 4
                #self.set_image(self.img_down, 65, 36)
        if key[pygame.K_RIGHT]:
            if self.x < Globals.SCREEN_WIDTH / 2 - 150:
                self.x += 4
        if key[pygame.K_LEFT]:
            if self.x > 10:
                self.x -= 4
        if key[pygame.K_n]:
            self.room.complete()

    def joy_pad_signal(self, p1_buttons, p2_buttons):
        if p1_buttons[10] < -0.5:
            self.y -= 4
        if p1_buttons[10] > 0.5:
            self.y += 4
        if p1_buttons[11] < 0.5:
            self.x += 0.5

    def handle_collision(self, other, other_type):
        self.room.remove_points()
        self.delete_object(other)

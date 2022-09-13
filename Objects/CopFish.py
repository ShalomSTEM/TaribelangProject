import pygame

from GameFrame import RoomObject, Globals
import os


class CopFish(RoomObject):
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)

        self.standard_image = self.load_image(os.path.join('CopG3', 'CopFish.png'))
        self.set_image(self.standard_image, 65, 36)

        self.depth = 100

        self.handle_key_events = True

    def key_pressed(self, key):
        if key[pygame.K_UP]:
            if self.y > 50:
                self.y -= 4
        elif key[pygame.K_DOWN]:
            if self.y < Globals.SCREEN_HEIGHT - 50:
                self.y += 4
        if key[pygame.K_n]:
            self.room.complete()

    def joy_pad_signal(self, p1_buttons, p2_buttons):
        if p1_buttons[10] < -0.5:
            self.y -= 4
        if p1_buttons[10] > 0.5:
            self.y += 4

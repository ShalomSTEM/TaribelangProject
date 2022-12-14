import pygame
import os
from GameFrame import Globals
from GameFrame import RoomObject


class Copple1_Player (RoomObject):
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)

        self.image1 = self.load_image(os.path.join('CoppleL1', 'Runner2.png'))
        self.image2 = self.load_image(os.path.join('CoppleL1', "Runner3.png"))
        self.image3 = self.load_image(os.path.join('CoppleL1', "Runner4.png"))
        self.set_image(self.image1, 29, 86)
        self.curr_img = 1

        self.depth = 100

        self.handle_key_events = True

        self.set_timer(5, self.update_image)

        self.scroll_stopped = False

        self.register_collision_object('CopG1_Tree')

    def step(self):
        if self.scroll_stopped:
            if not self.collides_at(self, 0, -5, "CopG1_Tree") and \
              not self.collides_at(self, 5, 0, "CopG1_Tree") and \
              not self.collides_at(self, -5, 0, "CopG1_Tree"):
                self.room.start_scroll_again()

    def handle_collision(self, other, other_type):
        if other_type == 'CopG1_kangaroo':
            self.blocked()
        elif other_type == 'CopG1_Emu':
            self.blocked()
        elif other_type == 'CopG1_Tree':
            self.room.tree_hit()
            self.scroll_stopped = True

    def update_image(self):
        self.curr_img += 1
        if self.curr_img > 2:
            self.curr_img = 0
        if self.curr_img == 0:
            self.set_image(self.image1, 29, 86)
        elif self.curr_img == 1:
            self.set_image(self.image2, 29, 86)
        elif self.curr_img == 2:
            self.set_image(self.image3, 29, 86)

        self.set_timer(5, self.update_image)

    def key_pressed(self, key):
        if key[pygame.K_LEFT]:
            if self.x > 50:
                self.x -= 4
        if key[pygame.K_RIGHT]:
            if self.x < Globals.SCREEN_WIDTH - 50 - self.width:
                self.x += 4
        if key[pygame.K_UP]:
            if self.y > Globals.SCREEN_HEIGHT / 2:
                self.y -= 4
        if key[pygame.K_DOWN]:
            if self.y < Globals.SCREEN_HEIGHT - self.height:
                self.y += 4

    def joy_pad_signal(self, p1_buttons, p2_buttons):
        if p1_buttons[11] < - 0.5:
            if self.x > 50:
                self.x -= 4
        if p1_buttons[11] > 0.5:
            if self.x < Globals.SCREEN_WIDTH - 50 - self.width:
                self.x += 4
        if p1_buttons[10] < - 0.5:
            if self.y > Globals.SCREEN_HEIGHT / 2:
                self.y -= 4
        if p1_buttons[10] > 0.5:
            if self.y < Globals.SCREEN_HEIGHT - self.height:
                self.y += 4
import os
import sys

import pygame
from pygame import MOUSEBUTTONDOWN

from GameFrame import RoomObject, Globals


class Projectile(RoomObject):
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)
        image = self.load_image(os.path.join("MilbiL3", "Spear.png"))
        self.set_image(image, 32, 32)

        self.block_right = False
        self.block_left = False
        self.block_up = False
        self.block_down = False

        self.register_collision_object("BossMLBL3")
        self.vel = 8




    def fire(self, key, bullets):

        for bullet in bullets:
            self.load_image(os.path.join("MilbiL3", "Spear.png"))


        bullets = []
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                elif event.type == [pygame.key_B]:
                    bullets.append(self.x, self.y,self.load_image(os.path.join("MilbiL3", "Spear.png")))
    clock = pygame.time.Clock()
    clock.tick(60)

    mx, my = pygame.mouse.get_pos()
    bullets = []
    for b in range(len(bullets)):
        bullets[b][0] -= 10

    # Iterate over a slice copy if you want to mutate a list.
    for bullet in bullets[:]:
        if bullet[0] < 0:
            bullets.remove(bullet)



    def handle_collision(self, other, other_type):

        if other_type == "BossMLBL3":

            if self.collides_at(self, 4, 0, "BossMLBL3") and not self.block_right:
                self.block_right = True
                if self.x < 596:
                    self.remove_object(self)

            if self.collides_at(self, -4, 0, "BossMLBL3") and not self.block_left:
                self.block_left = True
                if self.x >= 206:
                    self.remove_object(self)

            if self.collides_at(self, 0, 4, "BossMLBL3") and not self.block_down:
                self.block_down = True
                if self.y <= 446:
                    self.remove_object(self)

            if self.collides_at(self, 0, -4, "BossMLBL3") and not self.block_up:
                self.block_up = True
                if self.y >= 154:
                    self.remove_object(self)

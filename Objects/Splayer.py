import pygame, os
from GameFrame import RoomObject, Globals


class Splayer(RoomObject):
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)

        self.playerUp = self.load_image(os.path.join('Museum', 'Splayer.png'))
        self.playerDown = self.load_image(os.path.join('Museum', 'Splayer.png'))
        self.playerLeft = self.load_image(os.path.join('Museum', 'Splayer.png'))
        self.playerRight = self.load_image(os.path.join('Museum', 'Splayer.png'))
        self.set_image(self.playerDown, 32, 32)

        self.depth = 5

        self.handle_key_events = True

        # -- Register the objects with which -- #
        # -- this object handles collisions  -- #
        self.register_collision_object('MBlock')
        self.register_collision_object('MBlockDoor')

    def handle_collision(self, other, other_type):
        if other_type == 'MBlock':
            self.blocked()
        elif other_type == "MBlockDoor":
            self.room.complete()

    def key_pressed(self, key):

        if key[pygame.K_LEFT]:
            self.set_image(self.playerLeft, 32, 32)
            self.x -= 4
        elif key[pygame.K_RIGHT]:
            self.set_image(self.playerRight, 32, 32)
            self.x += 4
        elif key[pygame.K_UP]:
            self.set_image(self.playerUp, 32, 32)
            self.y -= 4
        elif key[pygame.K_DOWN]:
            self.set_image(self.playerDown, 32, 32)
            self.y += 4

    def joy_pad_signal(self, p1_buttons, p2_buttons):
        if p1_buttons[11] < -0.5:
            self.set_image(self.playerLeft, 32, 32)
            self.x -= 4
        if p1_buttons[11] > 0.5:
            self.set_image(self.playerRight, 32, 32)
            self.x += 4
        if p1_buttons[10] < -0.5:
            self.set_image(self.playerUp, 32, 32)
            self.y -= 4
        if p1_buttons[10] > 0.5:
            self.set_image(self.playerDown, 32, 32)
            self.y += 4

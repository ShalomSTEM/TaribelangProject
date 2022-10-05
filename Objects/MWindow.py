from GameFrame import RoomObject
import pygame


class MWindow(RoomObject):
    def __init__(self, room, x, y, icon_image, filename, player):
        RoomObject.__init__(self, room, x, y)

        self.original_x = x
        self.original_y = y

        self.icon_image = self.load_image(icon_image)
        self.set_image(self.icon_image, 32, 32)

        self.window_image = self.load_image(filename)

        self.player = player
        self.q_listen = False
        self.handle_key_events = True

    def load_window(self):
        self.set_image(self.window_image, 200, 200)
        self.q_listen = True
        self. x = 200
        self. y = 150

    def key_pressed(self, key):
        if key[pygame.K_q]:
            if self.q_listen:
                self.set_image(self.icon_image, 32, 32)
                self.q_listen = False
                self.player.can_window = True
                self.x = self.original_x
                self.y = self.original_y


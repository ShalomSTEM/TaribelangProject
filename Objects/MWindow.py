from GameFrame import RoomObject
import pygame


class MWindow(RoomObject):
    def __init__(self, room, x, y, icon_image, filename, player):
        RoomObject.__init__(self, room, x, y)

        self.filename = filename

        self.original_x = x
        self.original_y = y

        self.icon_image = self.load_image(icon_image)
        self.set_image(self.icon_image, 150, 150)

        self.window_image = self.load_image(filename)

        self.player = player
        self.y_listen = False
        self.handle_key_events = True

        self.depth = 100

    def load_window(self):
        self.set_image(self.window_image, 1180, 610)
        self.y_listen = True
        self. x = 50
        self. y = 50
        self.update_depth(1000)

    def key_pressed(self, key):
        if key[pygame.K_y]:
            if self.y_listen:
                self.end_window()

    def joy_pad_signal(self, p1_buttons, p2_buttons):
        if p1_buttons[3]:
            self.end_window()

    def end_window(self):
        self.set_image(self.icon_image, 150, 150)
        self.y_listen = False
        self.x = self.original_x
        self.y = self.original_y
        self.update_depth(100)
        self.player.can_window = True

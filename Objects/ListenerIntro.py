from GameFrame import RoomObject, Globals
import pygame


class ListenerIntro(RoomObject):
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)

        self.set_image(self.load_image("listener.png"), 1, 1)

        self.handle_key_events = True

        self.can_press = False

        self.set_timer(10, self.reset_press)

    def key_pressed(self, key):
        if self.can_press:
            if key[pygame.K_LEFTBRACKET]:
                Globals.direct_select=True
                Globals.next_level=4
                self.room.running=False
            if key[pygame.K_RIGHTBRACKET]:
                Globals.direct_select=True
                Globals.next_level=6
                self.room.running=False
            if key[pygame.K_BACKSLASH]:
                Globals.direct_select=True
                Globals.next_level=8
                self.room.running=False

    def pause_press(self):
        self.can_press = False
        self.set_timer(10, self.reset_press)

    def reset_press(self):
        self.can_press = True

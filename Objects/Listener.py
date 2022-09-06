from GameFrame import RoomObject
import pygame


class Listener(RoomObject):
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)

        self.set_image(self.load_image("listener.png"), 1, 1)

        self.handle_key_events = True

        self.can_press = False

        self.set_timer(10, self.reset_press)

    def key_pressed(self, key):
        if self.can_press:
            if key[pygame.K_RIGHT]:
                self.room.key_signal("right")
                self.pause_press()
            elif key[pygame.K_LEFT]:
                self.room.key_signal("left")
                self.pause_press()
            elif key[pygame.K_UP]:
                self.room.key_signal("up")
                self.pause_press()
            elif key[pygame.K_DOWN]:
                self.room.key_signal("down")
                self.pause_press()
            elif key[pygame.K_RETURN]:
                self.room.key_signal("enter")
                self.pause_press()

    def joy_pad_signal(self, p1_buttons, p2_buttons):
        if self.can_press:
            if p1_buttons[11] > 0.5:
                self.room.key_signal("right")
                self.pause_press()
            elif p1_buttons[11] < -0.5:
                self.room.key_signal("left")
                self.pause_press()
            elif p1_buttons[10] > 0.5:
                self.room.key_signal("down")
                self.pause_press()
            elif p1_buttons[10] < -0.5:
                self.room.key_signal("up")
                self.pause_press()

            elif p1_buttons[2]:
                self.room.key_signal("enter")
                self.pause_press()

    def pause_press(self):
        self.can_press = False
        self.set_timer(10, self.reset_press)

    def reset_press(self):
        self.can_press = True

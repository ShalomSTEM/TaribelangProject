import string
from GameFrame import Globals, RoomObject
import os
import pygame

class Controller(RoomObject):
    def __init__(self, room, x, y, buttons):
        RoomObject.__init__(self, room, x, y)
        self.set_image(self.load_image(os.path.join("Overlays", "Controller_b.png")), 1280, 720)
        self.mylist = buttons.split(" ")
        self.handle_key_events = True
        if "a" in self.mylist: print("a is here")
        if "b" in self.mylist: print("b is here")
        if "x" in self.mylist: print("x is here")
        if "y" in self.mylist: print("y is here")
        if "rb" in self.mylist: print("rb is here")
        if "lb" in self.mylist: print("lb is here")
        # if "left" in self.mylist: self.room.add_room_object(L_DpadOverlay(self.room, 150, 150))
        #if "right" in self.mylist: self.room.add_room_object(R_DpadOverlay(self.room, 250, 150))
        #if "up" in self.mylist: self.room.add_room_object(U_DpadOverlay(self.room, 150, 250))
        #if "down" in self.mylist: self.room.add_room_object(D_DpadOverlay(self.room, 250, 250))
        if "start" in self.mylist: print("select is here")
        if "select" in self.mylist: print("start is here")
    def key_pressed(self, key):
        if key[pygame.K_a]:
            print("a")

class L_DpadOverlay(RoomObject):
    def __init__(self, room, x, y):
        RoomObject.__init__(room, x, y)
        print("left is here")
        self.set_image(self.load_image(os.path.join("Overlays", "dpad_L.svg")))
class R_DpadOverlay(RoomObject):
    def __init__(self, room, x, y):
        RoomObject.__init__(room, x, y)
        self.set_image(self.load_image(os.path.join("Overlays", "dpad_R.svg")))
class D_DpadOverlay(RoomObject):
    def __init__(self, room, x, y):
        RoomObject.__init__(room, x, y)
        self.set_image(self.load_image(os.path.join("Overlays", "dpad_D.svg")))
class U_DpadOverlay(RoomObject):
    def __init__(self, room, x, y):
        RoomObject.__init__(room, x, y)
        self.set_image(self.load_image(os.path.join("Overlays", "dpad_U.svg")))
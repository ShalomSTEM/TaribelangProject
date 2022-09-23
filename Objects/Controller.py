import string
from GameFrame import Globals, RoomObject, EnumLevels
import os
import pygame

class Controller1(RoomObject):
    def __init__(self, room, x, y, buttons):
        RoomObject.__init__(self, room, x, y)
        Globals.oldRoom = self.room.roomNum
        self.set_image(self.load_image("listener.png"), 1, 1)
        Globals.next_level = EnumLevels.ControllerOverlay
        Globals.OverlayButtons = buttons
        self.room.running = False
class Controller2(RoomObject):
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)
        self.set_image(self.load_image(os.path.join("Overlays", "Controller_b.png")), 1280, 720)
        self.mylist = Globals.OverlayButtons.split(" ")
        self.handle_key_events = True
        if "a" in self.mylist: self.room.add_room_object(A_ButtonOverlay(self.room, 150, 150))
        if "b" in self.mylist: self.room.add_room_object(B_ButtonOverlay(self.room, 150, 150))
        if "x" in self.mylist: self.room.add_room_object(X_ButtonOverlay(self.room, 150, 150))
        if "y" in self.mylist: self.room.add_room_object(Y_ButtonOverlay(self.room, 150, 150))
        if "rb" in self.mylist: self.room.add_room_object(R_BumperOverlay(self.room, 150, 150))
        if "lb" in self.mylist: self.room.add_room_object(L_BumperOverlay(self.room, 150, 150))
        if "left" in self.mylist: self.room.add_room_object(L_DpadOverlay(self.room, 150, 150))
        if "right" in self.mylist: self.room.add_room_object(R_DpadOverlay(self.room, 250, 150))
        if "up" in self.mylist: self.room.add_room_object(U_DpadOverlay(self.room, 150, 250))
        if "down" in self.mylist: self.room.add_room_object(D_DpadOverlay(self.room, 250, 250))
        if "start" in self.mylist: self.room.add_room_object(Select_ButtonOverlay(self.room, 150, 150))
        if "select" in self.mylist: self.room.add_room_object(Start_ButtonOverlay(self.room, 150, 150))
    def key_pressed(self, key):
        if key[pygame.K_INSERT]:
            self.room.complete()

class L_DpadOverlay(RoomObject):
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)
        self.set_image(self.load_image(os.path.join("Overlays", "dpad_L.svg")), 64, 64)
class R_DpadOverlay(RoomObject):
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)
        self.set_image(self.load_image(os.path.join("Overlays", "dpad_R.svg")), 64, 64)
class D_DpadOverlay(RoomObject):
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)
        self.set_image(self.load_image(os.path.join("Overlays", "dpad_D.svg")), 64, 64)
class U_DpadOverlay(RoomObject):
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)
        self.set_image(self.load_image(os.path.join("Overlays", "dpad_U.svg")), 64, 64)  
class A_ButtonOverlay(RoomObject):
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)
        self.set_image(self.load_image(os.path.join("Overlays", "Button-Red.svg")), 64, 64)       
class B_ButtonOverlay(RoomObject):
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)
        self.set_image(self.load_image(os.path.join("Overlays", "Button-Yellow.svg")), 64, 64)
class X_ButtonOverlay(RoomObject):
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)
        self.set_image(self.load_image(os.path.join("Overlays", "Button-Blue.svg")), 64, 64)       
class Y_ButtonOverlay(RoomObject):
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)
        self.set_image(self.load_image(os.path.join("Overlays", "Button-Green.svg")), 64, 64)
class Start_ButtonOverlay(RoomObject):
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)
        self.set_image(self.load_image(os.path.join("Overlays", "Start_Select_Button.png")), 64, 64)       
class Select_ButtonOverlay(RoomObject):
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)
        self.set_image(self.load_image(os.path.join("Overlays", "Start_Select_Button.png")), 64, 64)
class L_BumperOverlay(RoomObject):
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)
        self.set_image(self.load_image(os.path.join("Overlays", "L_Bumper_Button.png")), 64, 64)       
class R_BumperOverlay(RoomObject):
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)
        self.set_image(self.load_image(os.path.join("Overlays", "R_Bumper_Button.png")), 64, 64)
import string
from GameFrame import Globals, RoomObject
import os
import pygame

class L_DpadOverlay(RoomObject):
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)
        self.set_image(self.load_image(os.path.join("Overlays", "dpad_L.svg")), 64, 64)
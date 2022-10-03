from GameFrame import Level, Globals, EnumLevels
from Objects import Splayer, MBlock, MBlockDoor

import os


class Museum(Level):
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)
        # - Set Background image - #

        self.set_background_image(os.path.join("Museum", "floor.jpg"))
        #self.background_color = (255, 255, 255)

        # - Set up maze, objects 32x32 25x17 - #
        room_objects = [
            'bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb',
            'bp____________________________________D_',
            'b_______________________________________',
            'b______________________________________b ',
            'b_______bbbbbbbb________bbbbbbbb_______b',
            'b______________________________________b',
            'b______________________________________b',
            'b__________bb______________bb__________b',
            'b______________________________________b',
            'b______________________________________b',
            'b_______bbbbbbbb________bbbbbbbb_______b',
            'b______________________________________b',
            'b______________________________________b',
            'b__________bb______________bb__________b',
            'b______________________________________b',
            'b______________________________________b',
            'b_______bbbbbbbb________bbbbbbbb_______b',
            'b______________________________________b',
            'b__________bb______________bb__________b',
            'b______________________________________b',
            'b______________________________________b',
            'bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb'
        ]

        for i, row in enumerate(room_objects):
            for j, obj in enumerate(row):
                if obj == 'b':
                    self.add_room_object(MBlock(self, j*32, i*32))
                elif obj == 'p':
                    self.add_room_object(Splayer(self, j*32, i*32))
                elif obj == 'D':
                    self.add_room_object(MBlockDoor(self, j*32, i*32))

    def complete(self):
        Globals.next_level = EnumLevels.Home
        self.running = False

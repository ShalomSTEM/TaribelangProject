from GameFrame import Level, Globals, EnumLevels
from Objects import Splayer, MBlock, MBlockDoor, MWindow

import os


class Museum(Level):
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)
        # - Set Background image - #

        self.set_background_image(os.path.join("Museum", "floor4.png"))

        self.player = None

        # - Set up maze, objects 32x32 25x17 - #
        room_objects = [
            'bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb',
            'bp____________________________________D_',
            'b_______________________________________',
            'b______________________________________b',
            'b___bbbbbbbbb______________bbbbbbbbb___b',
            'b______________________________________b',
            'b______________________________________b',
            'b__________w____bbbbbbb____w___________b',
            'b______________________________________b',
            'b______________________________________b',
            'b___bbbbbbb__________________bbbbbbb___b',
            'b______________________________________b',
            'b______________________________________b',
            'b__________w____bbbbbbb____w___________b',
            'b______________________________________b',
            'b______________________________________b',
            'b___bbbbbbbbb______________bbbbbbbbb___b',
            'b______________________________________b',
            'b__________w_______________w___________b',
            'b______________________________________b',
            'b______________________________________b',
            'bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb'
        ]

        for i, row in enumerate(room_objects):
            for j, obj in enumerate(row):
                if obj == 'b':
                    self.add_room_object(MBlock(self, j*32, i*32))
                elif obj == 'p':
                    self.player = Splayer(self, j*32, i*32)
                    self.add_room_object(self.player)
                elif obj == 'D':
                    self.add_room_object(MBlockDoor(self, j*32, i*32))

        self.add_room_object(
            MWindow(
                self,
                177,
                164,
                os.path.join('Museum', 'coople5.png'),
                os.path.join("Museum", "copplewords3.png"),
                self.player
            )
        )

        self.add_room_object(
            MWindow(
                self,
                950,
                164,
                os.path.join('Museum', 'milbibook.png'),
                os.path.join("Museum", "milbistry.png"),
                self.player
            )
        )

        self.add_room_object(
             MWindow(
                self,
                177,
                360,
                os.path.join('Museum', 'spear.png'),
                os.path.join("Museum", "spearwords.png"),
                self.player
             )
        )

        self.add_room_object(
             MWindow(
                self,
                950,
                356,
                os.path.join('Museum', 'animals.png'),
                os.path.join("Museum", "animalwords.png"),
                self.player
             )
        )

        self.add_room_object(
             MWindow(
                self,
                550,
                260,
                os.path.join('Museum', 'landscape.png'),
                os.path.join("Museum", "landscapewords.png"),
                self.player
             )
        )




    def complete(self):
        Globals.next_level = EnumLevels.Home
        self.running = False

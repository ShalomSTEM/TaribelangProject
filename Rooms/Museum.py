from GameFrame import Level, Globals, EnumLevels
from Objects import Splayer, MBlock, MBlockDoor


class Museum(Level):
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)
        # - Set Background image - #
        #self.set_background_image("background.jpg")
        self.background_color = (255, 255, 255)
        # - Set up maze, objects 32x32 25x17 - #
        room_objects = [
            'bbbbbbbbbbbbbbbbbbbbbbbbb',
            'bp______________________D',
            'b___bbbbb___bbbbbbbb__bbb',
            'b___b___bb__bb_____b___bb',
            'b___b____b__b___b___b___b',
            'b___bb___b__b___bbb__b__b',
            'b____b___b__b______b____b',
            'b____b___b__bbbb__b_____b',
            'bbbbbbbbbb_____b__b_____b',
            'b________________bbbbbbdb',
            'b____bbbb_______b_______b',
            'bbbbb_______b_b__b__bb__b',
            'b_____bbbb__b_b__b__bb__b',
            'b________b__b_b_____bb__b',
            'bbbbbb___b__b_bb____bbbbb',
            'bg_____b_________b_____gb',
            'bbbbbbbbbbbbbbbbbbbbbbbbb'
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


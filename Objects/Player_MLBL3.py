import pygame
from GameFrame import RoomObject, Globals


class Player_MLBL3(RoomObject):
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)

        player = self.load_image('front_1.png')
        self.set_image(player, 16, 24)

        # Load player animation images
        self.down = []
        self.down.append(self.load_image('Images/MilbiL1/sprite_0.png'))
        self.down.append(self.load_image('Images/MilbiL1/sprite_0.png'))
        self.down.append(self.load_image('Images/MilbiL1/sprite_0.png'))
        self.down.append(self.load_image('Images/MilbiL1/sprite_0.png'))
        self.up = []
        self.up.append(self.load_image('Images/MilbiL1/sprite_2.png'))
        self.up.append(self.load_image('Images/MilbiL1/sprite_2.png'))
        self.up.append(self.load_image('Images/MilbiL1/sprite_2.png'))
        self.up.append(self.load_image('Images/MilbiL1/sprite_2.png'))
        self.left = []
        self.left.append(self.load_image('Images/MilbiL1/sprite_1.png'))
        self.left.append(self.load_image('Images/MilbiL1/sprite_1.png'))
        self.left.append(self.load_image('Images/MilbiL1/sprite_1.png'))
        self.left.append(self.load_image('Images/MilbiL1/sprite_1.png'))
        self.right = []
        self.right.append(self.load_image('Images/MilbiL1/sprite_3.png'))
        self.right.append(self.load_image('Images/MilbiL1/sprite_3.png'))
        self.right.append(self.load_image('Images/MilbiL1/sprite_3.png'))
        self.right.append(self.load_image('Images/MilbiL1/sprite_3.png'))

        self.img_index = 0

        self.LEFT = 0
        self.RIGHT = 1
        self.UP = 2
        self.DOWN = 3

        self.facing = 4

        self.handle_key_events = True

        self.register_collision_object('Stone_MLBL3')

        self.block_right = False
        self.block_left = False
        self.block_up = False
        self.block_down = False

        self.moving = False
        self.animate()

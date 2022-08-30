import pygame

from GameFrame import Level, Globals
import os
from Objects.Dirt_MLBL3 import Dirt_MLBL3
from Objects.Stne_MLBL3 import Stne_MLBL3
from Objects.Player_MLBL3 import Player_MLBL3


class MilbiL3(Level):
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)
        Globals.mlb3_move_speed = 16
        size = 20
        self.set_background_image(
            os.path.join(Globals.milbiL3_alt_path, "PlaceHolderBackground_MLBL3.png")
        )


        self.room_items = []

        room_objects = [
            "DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD",
            "DDDDDDDDDDDDDDDDDDDDDDBBBBBBBBDDDDDDDDDDDDDDDDDDDD",
            "DDDDDDDDDDDDDDDDDDDDDDB      BDDDDDDDDDDDDDDDDDDDD",
            "DBBBBBBBBBBBBBBBBBBBBBB      BBBBBBBBBBBBBBBBBBBBD",
            "DB                                              BD",
            "DB                          P                   BD",
            "DB       BBBBBBB                                BD",
            "DB       B                         BBBBB        BD",
            "DB       B                             B        BD",
            "DB                                     B        BD",
            "DB                                              BD",
            "DB                                              BD",
            "DB             B                                BD",
            "DB             B                     B          BD",
            "DB         BBBBB                     B          BD",
            "DB                                   B          BD",
            "DB                             BBBBBBB          BD",
            "DB           B                                  BD",
            "DB           B                                  BD",
            "DB           B                                  BD",
            "DB           BBBB                               BD",
            "DB                                              BD",
            "DBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBD",
            "DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD",
        ]

        for i, row in enumerate(room_objects):
            for j, obj in enumerate(row):
                if obj == "B":
                    new_block = Stne_MLBL3(self, j * 64, i * 64)
                    self.add_room_object(new_block)
                    self.room_items.append(new_block)
                elif obj == "P":
                    player = Player_MLBL3(self, j * 64, i * 64, size)
                    self.add_room_object(player)

                elif obj == "D":
                    new_dirt = Dirt_MLBL3(self, j * 64, i * 64)
                    self.add_room_object(new_dirt)
                    self.room_items.append(new_dirt)

    def shift_room_left(self):
        for item in self.room_items:
            item.x -= Globals.mlb3_move_speed

    def shift_room_right(self):
        for item in self.room_items:
            item.x += Globals.mlb3_move_speed

    def shift_room_up(self):
        for item in self.room_items:
            item.y -= Globals.mlb3_move_speed

    def shift_room_down(self):
        for item in self.room_items:
            item.y += Globals.mlb3_move_speed



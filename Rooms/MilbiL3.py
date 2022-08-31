




from GameFrame import Level, Globals
import os

from Objects.Boss_MLBL3 import Red1
from Objects.Dirt_MLBL3 import Dirt_MLBL3
from Objects.KillB_MLBL3 import KillB_MLBL3
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

            "DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD",
            "DDKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKDD",
            "DDBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBDD",
            "DDB                                              BDD",
            "DDB                                              BDD",
            "DDB       BBBBBBB         O                      BDD",
            "DDB       B                         BBBBB        BDD",
            "DDB       B                             B        BDD",
            "DDB                                     B        BDD",
            "DDB                                              BDD",
            "DDB                                              BDD",
            "DDB             B                                BDD",
            "DDB             B                     B          BDD",
            "DDB         BBBBB                     B          BDD",
            "DDB                                   B          BDD",
            "DDB                             BBBBBBB          BDD",
            "DDB           B                                  BDD",
            "DDB           B                                  BDD",
            "DDB           B                                  BDD",
            "DDB           BBBB                               BDD",
            "DDB                                              BDD",
            "DDBBBBBBBBBBBBBBBBB                  BBBBBBBBBBBBBDD",
            "DDKKKKKKKKKKKKKKKKB         P        BKKKKKKKKKKKKDD",
            "DDDDDDDDDDDDDDDDDKB                  BKDDDDDDDDDDDDD",
            "DDDDDDDDDDDDDDDDDKBBBBBBBBBBBBBBBBBBBBKDDDDDDDDDDDDD",
            "DDDDDDDDDDDDDDDDDKKKKKKKKKKKKKKKKKKKKKKDDDDDDDDDDDDD",
        ]

        for i, row in enumerate(room_objects):
            for j, obj in enumerate(row):
                if obj == "B":
                    new_block = Stne_MLBL3(self, j * 32 - 200, i * 32 - 200)
                    self.add_room_object(new_block)
                    self.room_items.append(new_block)
                elif obj == "P":
                    player = Player_MLBL3(self, j * 32 - 200, i * 32 - 200, size)
                    self.add_room_object(player)

                elif obj == "D":
                    new_dirt = Dirt_MLBL3(self, j * 32 - 200, i * 32 - 200)
                    self.add_room_object(new_dirt)
                    self.room_items.append(new_dirt)

                elif obj == "K":
                    kill_block = KillB_MLBL3(self, j * 32 - 200, i * 32 - 200)
                    self.add_room_object(kill_block)
                    self.room_items.append(kill_block)

                elif obj == "O":
                    new_boss = Red1(self, j * 32 - 200, i * 32 - 200)
                    self.add_room_object(new_boss)
                    self.room_items.append(new_boss)

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



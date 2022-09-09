from GameFrame import Level, TextObject, Globals, EnumLevels
from GameFrame import Level, Globals
import os
from Objects import Dirt_MLBL3
from Objects import Stne_MLBL3
from Objects import Player_MLBL3


class Mil_G3(Level):
    def __init__(self, screen, joysticks, direct=False):
        Level.__init__(self, screen, joysticks)

        self.direct = direct
        self.move_speed = 16
        size = 20
        self.set_background_image(
            os.path.join("MilbiL3", "PlaceHolderBackground_MLBL3.png")
        )

        self.room_items = []

        room_objects = [
            "DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD",
            "DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD",
            "DDBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBDD",
            "DDB                                              BDD",
            "DDB                                              BDD",
            "DDB       BBBBBBB                                BDD",
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
            "DDDDDDDDDDDDDDDDDBB         P        BBDDDDDDDDDDDDD",
            "DDDDDDDDDDDDDDDDDBB                  BBDDDDDDDDDDDDD",
            "DDDDDDDDDDDDDDDDDBBBBBBBBBBBBBBBBBBBBBBDDDDDDDDDDDDD",
            "DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD",
        ]

        for i, row in enumerate(room_objects):
            for j, obj in enumerate(row):
                if obj == "B":
                    new_block = Stne_MLBL3(self, j * 64 - 200, i * 64 - 200)
                    self.add_room_object(new_block)
                    self.room_items.append(new_block)
                elif obj == "P":
                    player = Player_MLBL3(self, j * 32 - 200, i * 32 - 200, size)
                    self.add_room_object(player)
                elif obj == "D":
                    new_dirt = Dirt_MLBL3(self, j * 64 - 200, i * 64 - 200)
                    self.add_room_object(new_dirt)
                    self.room_items.append(new_dirt)




    def shift_room_left(self):
        for item in self.room_items:
            item.x -= self.move_speed

    def shift_room_right(self):
        for item in self.room_items:
            item.x += self.move_speed

    def shift_room_up(self):
        for item in self.room_items:
            item.y -= self.move_speed

    def shift_room_down(self):
        for item in self.room_items:
            item.y += self.move_speed
            item.y += self.move_speed



        self.set_timer(5, self.complete)

    def complete(self):
        if Globals.direct_select:
            Globals.direct_select = False
            Globals.next_level = EnumLevels.Home
        self.running = False


from GameFrame import Level, Globals, EnumLevels
import os
from Objects import Dirt_MLBL3, Stne_MLBL3, Player_MLBL3, Spear_MLBL3, BossMLBL3, Orb_MLBL3, CopG2_NPC
from Objects.Orb_MLBL3 import Orb_MLBL3

class Mil_G3(Level):
    def __init__(self, screen, joysticks, direct=False):
        Level.__init__(self, screen, joysticks)
        self.direct = direct

        # - Information for Controller Overlay
        self.roomNum = EnumLevels.Mil_G3

        self.set_background_image(os.path.join("MilbiL3", "PlaceHolderBackground_MLBL3.png"))
        self.room_items = []
        size = 20

        self.new_boss = BossMLBL3(self, Globals.SCREEN_WIDTH / 2 - 128, 6 * 32)
        self.add_room_object(self.new_boss)
        self.room_items.append(self.new_boss)

        room_objects = [
            "DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD",
            "DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD",
            "DDBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBDD",
            "DDB                       O                      BDD",
            "DDB                                              BDD",
            "DDB       BBBBBBB       O M O                    BDD",
            "DDB       B                         BBBBB        BDD",
            "DDB       B               O             B        BDD",
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
            "DDB           B              N                   BDD",
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
                    new_block = Stne_MLBL3(self, j * 32 - 200, i * 32 - 200)
                    self.add_room_object(new_block)
                    self.room_items.append(new_block)
                elif obj == "P":
                    self.player = Player_MLBL3(self, j * 32 - 200, i * 32 - 200, size, self.new_boss)
                    self.player.x = j * 32 - 200
                    self.player.y = i * 32 - 200
                    self.add_room_object(self.player)
                elif obj == "D":
                    new_dirt = Dirt_MLBL3(self, j * 32 - 200, i * 32 - 200)
                    self.add_room_object(new_dirt)
                    self.room_items.append(new_dirt)
                elif obj == "O":
                    self.new_orb = Orb_MLBL3(self, j * 32 - 200, i * 32 - 200)
                    self.set_timer(200, self.createOrb)

    def createOrb(self):
        self.add_room_object(self.new_orb)
        self.room_items.append(self.new_orb)
    def shift_room_left(self):
        for item in self.room_items:
            item.x -= Globals.move_speed

    def shift_room_right(self):
        for item in self.room_items:
            item.x += Globals.move_speed

    def shift_room_up(self):
        for item in self.room_items:
            item.y -= Globals.move_speed

    def shift_room_down(self):
        for item in self.room_items:
            item.y += Globals.move_speed

    def complete(self):
        if Globals.direct_select:
            Globals.direct_select = False
            Globals.next_level = EnumLevels.Home
        self.running = False

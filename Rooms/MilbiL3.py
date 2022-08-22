from GameFrame import Level, Globals
import os
from Objects.Dirt_MLBL3 import Dirt_MLBL3
from Objects.Stne_MLBL3 import Stne_MLBL3
from Objects.Player_MLBL3 import Player_MLBL3


class MilbiL3(Level):
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)
        self.set_background_image(
            os.path.join(Globals.milbiL3_alt_path, "PlaceHolderBackground_MLBL3.png")
        )

        self.room_items = []

        room_objects = [
            "DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD",
            "DBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBD",
            "DB                                              BD",
            "DB                                              BD",
            "DB                                              BD",
            "DB                                              BD",
            "DB                        B                     BD",
            "DB       B  BBBBBBBB      B                     BD",
            "DB       B         B      B                     BD",
            "DB       B         B      B                     BD",
            "DB       B         B      B                     BD",
            "DB       BBBBBBB   B      B                     BD",
            "DB                                              BD",
            "DB                                              BD",
            "DB           BBBBBB  BBBBBBB                    BD",
            "DB           B             B                    BD",
            "DB           B       P     B                    BD",
            "DB           B             B                    BD",
            "DB           B             B                    BD",
            "DB           BBBBBBBBBBBB  B                    BD",
            "DB                             BBBBB   BBBBBB   BD",
            "DB                                              BD",
            "DB       BB   BBBBBBBBBBB                       BD",
            "DB       B              B   BBBBBBBBBBBBBBBBB   BD",
            "DB       B              B   B                   BD",
            "DB       B    BBBBBBB   B                       BD",
            "DB       B   BBBBB     BBBBBBBBBBBBBBBBBBBBB    BD",
            "DB       B   B                             B    BD",
            "DB       B   B                             B    BD",
            "DBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBD",
            "DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD",
        ]

        for i, row in enumerate(room_objects):
            for j, obj in enumerate(row):
                if obj == "B":
                    new_block = Stne_MLBL3(self, j * 64 - 200, i * 64 - 200)
                    self.add_room_object(new_block)
                    self.room_items.append(new_block)
                elif obj == "P":
                    self.add_room_object(Player_MLBL3(self, j * 64 - 200, i * 64 - 200))
                elif obj == "D":
                    new_dirt = Dirt_MLBL3(self, j * 64 - 200, i * 64 - 200)
                    self.add_room_object(new_dirt)
                    self.room_items.append(new_dirt)

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

    def UpdateWorld(self):
        self.set_timer(2, self.UpdateWorld)
        print("Ran")
        if (
            self.prev_player_x != Globals.player_x
            or self.prev_player_y != Globals.player_y
        ):
            print("changed")
            if Globals.player_x > self.prev_player_x:
                self.prev_player_x += 1
            elif Globals.player_x < self.prev_player_x:
                self.prev_player_x -= 1
            if Globals.player_y > self.prev_player_y:
                self.prev_player_y += 1
            elif Globals.player_y < self.prev_player_y:
                self.prev_player_y -= 1
            Globals.player_x = self.prev_player_x
            Globals.player_y = self.prev_player_y
            self.ChangeVisTileMap()
            self.DisplayTilemap()
            print(Globals.player_x)

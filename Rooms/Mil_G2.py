from GameFrame import Level, TextObject, Globals, EnumLevels
from Objects import ML2_People, ML2_Elders, Player_MLBL2, MLBL2_Tree
import os
class Mil_G2(Level):
    def __init__(self, screen, joysticks, direct=False):
        Level.__init__(self, screen, joysticks)

        self.direct = direct

        room_name = TextObject(self, 200, 300, "Milbi Game Part 2", colour="white")
        self.add_room_object(room_name)

        self.set_timer(60, self.complete)

    def complete(self):
        if Globals.direct_select:
            Globals.direct_select = False
            Globals.next_level = EnumLevels.Home
        self.running = False

        self.set_background_image(os.path.join("MilbiL2", "ML2_background.jpg")        )

        self.room_items = []


        room_objects = [
            "                                                  ",
            "                                                  ",
            "                                                  ",
            "                                                  ",
            "                                                  ",
            "                                                  ",
            "BBBBBBBGTGGBBTGTBGGBBTTTBBBTBGTTGGGBBBTGGTTBBB",
            "      B                                      T",
            "      T                                      B",
            "      T                                      T",
            "      B    EEE                               G",
            "      T   E   E                              T",
            "      T    EEE         AAAAAAA               B",
            "      T               AA     AA              B",
            "      B              AA       AA             G",
            "      G              AA       AA             G",
            "      T              AA       AA             G",
            "      T               AA     AA              T",
            "      B                AAAAAAA               T",
            "      G                                      B",
            "      G                                      B",
            "      T                                      G",
            "      T                                      T",
            "      G                                      B",
            "      G       P                              T",
            "      T                                      B",
            "BBBBBBBGGTTBGGGBTTBBBBTTTTBBBBTBBBGGTBTBBBTTTBB",
            "                                              ",
        ]

        for i, row in enumerate(room_objects):
            for j, obj in enumerate(row):
                if obj == "B":
                    self.add_room_object(MLBL2_Tree(self, j * 32 - 200, i * 32 - 200, "ML2_tree.png"))
                elif obj == "T":
                    self.add_room_object(ML2_Tree(self, j * 32 - 200, i * 32 - 200, "ML2_Ttree.png"))
                elif obj == "P":
                    self.add_room_object(Player_MLBL2(self, j * 32 - 200, i * 32 - 200))
                elif obj == "A":
                    self.add_room_object(ML2_People(self, j * 32 - 200, i * 32 - 200))
                elif obj == "E":
                    self.add_room_object(ML2_Elders(self, j * 32 - 200, i * 32 - 200))
                elif obj == "G":
                    self.add_room_object(ML2_Tree(self, j * 32 - 200, i * 32 - 200, "ML2_Btree.png"))


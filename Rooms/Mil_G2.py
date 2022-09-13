from GameFrame import Level, TextObject, Globals, EnumLevels


class Mil_G2(Level):
    def __init__(self, screen, joysticks, direct=False):
        Level.__init__(self, screen, joysticks)

        self.direct = direct
        self.set_background_image(os.path.join("MilbiL2", "ML2_background.jpg"))

        room_objects = [
            "                                                  ",
            "                                                  ",
            "                                                  ",
            "                                                  ",
            "                                                  ",
            "                                                  ",
            "BBBBBBBGTGGBBTGTBGGBBTTTBBBTBGTTGGGBBBTGGTTBGBB",
            "      B                                     T",
            "      T                                     B",
            "      T                                     T",
            "      B    EEE                              G",
            "      T   E   E                             T",
            "      T    EEE         ZZZZZZZ              B",
            "      T               ZZ     ZZ             B",
            "      B              ZZ       ZZ            G",
            "      G              ZZ       ZZ            G",
            "      T              ZZ       ZZ            G",
            "      T               ZZ     ZZ             T",
            "      B                ZZZZZZZ              T",
            "      G                                     B",
            "      G                                     B",
            "      T                                     G",
            "      T                                     T",
            "      G                                     B",
            "      G       P                             T",
            "      T                                     B",
            "BBBBBBBGGTTBGGGBTTBBBBTTTTBBBBTBBBGGTBTBBBTTTBB",
            "                                              ",
        ]

        for i, row in enumerate(room_objects):
            for j, obj in enumerate(row):
                if obj == "B":
                    self.add_room_object(MLBL2_Tree(self, j * 32 - 200, i * 32 - 200, "ML2_tree.png"))
                elif obj == "T":
                    self.add_room_object(MLBL2_Tree(self, j * 32 - 200, i * 32 - 200, "ML2_Ttree.png"))
                elif obj == "P":
                    self.add_room_object(Player_MLBL2(self, j * 32 - 200, i * 32 - 200))
                elif obj == "Z":
                    self.add_room_object(ML2_People(self, j * 32 - 200, i * 32 - 200, "ML2_people1.png"))
                elif obj == "Y":
                    self.add_room_object(ML2_People(self, j * 32 - 200, i * 32 - 200, "ML2_people2.jpg"))
                elif obj == "X":
                    self.add_room_object(ML2_People(self, j * 32 - 200, i * 32 - 200, "ML2_people3.jpg"))
                elif obj == "W":
                    self.add_room_object(ML2_People(self, j * 32 - 200, i * 32 - 200, "ML2_people4.jpg"))
                elif obj == "V":
                    self.add_room_object(ML2_People(self, j * 32 - 200, i * 32 - 200, "ML2_people5.jpg"))



                elif obj == "E":
                    self.add_room_object(ML2_Elders(self, j * 32 - 200, i * 32 - 200))
                elif obj == "G":
                    self.add_room_object(MLBL2_Tree(self, j * 32 - 200, i * 32 - 200, "ML2_Btree.png"))

        # self.set_timer(60, self.complete)

    def complete(self):
        if Globals.direct_select:
            Globals.direct_select = False
            Globals.next_level = EnumLevels.Home
        self.running = False

from GameFrame import Level, TextObject, Globals, EnumLevels
from Objects import ML2_Elders, ML2_People

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





                for i, row in enumerate(room_objects):
                    for j, obj in enumerate(row):
                        if obj == 'B':
                            new_tree = MLBL2_Tree(self, j*32 - 200, i*32 - 200, "ML2_tree.png")
                            self.add_room_object(new_tree)
                            self.room_items.append(new_tree)
                        if obj == 'T':
                            new_tree = MLBL2_Tree(self, j*32 - 200, i*32 - 200, "ML2_Ttree.png")
                            self.add_room_object(new_tree)
                            self.room_items.append(new_tree)
                        if obj == 'G':
                            new_tree = MLBL2_Tree(self, j*32 - 200, i*32 - 200, "ML2_Btree.png")
                            self.add_room_object(new_tree)
                            self.room_items.append(new_tree)
                        elif obj == 'P':
                            self.add_room_object(Player_MLBL2(self, j*32 - 200, i*32 - 200))
                        elif obj == 'E':
                            new_elder = ML2_Elders(self, j*32 - 200, i*32 - 200)
                            self.add_room_object(new_elder)
                            self.room_items.append(new_elder)
                        elif obj == 'Z':
                            new_people = ML2_People(self, j*32 - 200, i*32 - 200, "ML2_people1.png")
                            self.add_room_object(new_people)
                            self.room_items.append(new_people)
                        elif obj == 'Y':
                            new_people = ML2_People(self, j*32 - 200, i*32 - 200, "ML2_people2.png")
                            self.add_room_object(new_people)
                            self.room_items.append(new_people)
                        elif obj == 'X':
                            new_people = ML2_People(self, j*32 - 200, i*32 - 200, "ML2_people3.png")
                            self.add_room_object(new_people)
                            self.room_items.append(new_people)
                        elif obj == 'W':
                            new_people = ML2_People(self, j*32 - 200, i*32 - 200, "ML2_people4.png")
                            self.add_room_object(new_people)
                            self.room_items.append(new_people)
                        elif obj == 'V':
                            new_people = ML2_People(self, j*32 - 200, i*32 - 200, "ML2_people5.png")
                            self.add_room_object(new_people)
                            self.room_items.append(new_people)




        # self.set_timer(60, self.complete)

    def complete(self):
        if Globals.direct_select:
            Globals.direct_select = False
            Globals.next_level = EnumLevels.Home
        self.running = False

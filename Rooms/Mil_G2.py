from GameFrame import Level, TextObject, Globals, EnumLevels
import os
from Objects import MLBL2_Tree, Player_MLBL2, ML2_People, ML2_Elders, Wallaby_MLBL2, scoreText_MLBL3, MLBL2_Snake
from Objects.StoryOverlay import OverlayTextBG


class Mil_G2(Level):
    def __init__(self, screen, joysticks, direct=False):
        Level.__init__(self, screen, joysticks)
        self.y_speed = -1.2
        self.startMoving = False
        self.peoplePos = [(632, 312), (632, 280), (632, 248), (664, 216), (664, 184), (696, 184), (728, 184), (760, 184), (792, 184), (824, 184), (856, 216), (888, 248), (888, 280), (888, 312), (856, 344), (824, 376), (696, 376), (664, 344)]
        self.points = 0
        self.BObj = []
        self.TObj = []
        self.GObj = []
        self.EObj = []
        self.CObj = []
        self.SObj = []
        self.ZObj = []
        self.indexT = 0
        self.indexG = 0
        self.indexB = 0
        self.indexE = 0
        self.indexS = 0
        self.indexZ = 0
        self.arrows = []
        self.Dance = False
        
        # - Information for Controller Overlay
        self.roomNum = EnumLevels.Mil_G2

        self.direct = direct
        self.set_background_image(os.path.join("MilbiL2", "ML2_background_cpy.jpg"))

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
            "      T    EEE             XXWYVY           B",
            "      T                    Y     X          B",
            "      B                   Y       Y         G",
            "      G                   X       X         G",
            "      T     S             V       V         G",
            "      T                    W     V          T",
            "      B                     Y   X           T",
            "      G                                     B",
            "      G                                     B",
            "      T                                     G",
            "      T                                     T",
            "      G                                     B",
            "      G                       K             T",
            "      T                                     B",
            "BBBBBBBGGTTBGGGBTTBBBBTTTTBBB   BBGGTBTBBBTTTBB",
            "                              P                ",
        ]

        for i, row in enumerate(room_objects):
            for j, obj in enumerate(row):
                if obj == "B":
                    B = MLBL2_Tree(self, j * 32 - 200, i * 32 - 200, "ML2_tree.png")
                    self.add_room_object(B)
                    self.BObj.append(B)
                    self.indexB += 1
                elif obj == "T":
                    T = MLBL2_Tree(self, j * 32 - 200, i * 32 - 200, "ML2_Ttree.png")
                    self.add_room_object(T)
                    self.TObj.append(T)
                    self.indexT += 1
                elif obj == "P":
                    self.player = Player_MLBL2(self, j * 32 - 200, i * 32 - 200)
                    self.add_room_object(self.player)
                elif obj == "Z":
                    self.add_room_object(ML2_People(self, j * 32 - 200, i * 32 - 200, 2))
                elif obj == "Y":
                    self.add_room_object(ML2_People(self, j * 32 - 200, i * 32 - 200, 2))
                elif obj == "X":
                    self.add_room_object(ML2_People(self, j * 32 - 200, i * 32 - 200, 3))
                elif obj == "W":
                    self.add_room_object(ML2_People(self, j * 32 - 200, i * 32 - 200, 4))
                elif obj == "V":
                    self.add_room_object(ML2_People(self, j * 32 - 200, i * 32 - 200, 5))
                elif obj == "K":
                    self.add_room_object(Wallaby_MLBL2(self, j * 32 - 200, i * 32 - 200))
                elif obj == "E":
                    E = ML2_Elders(self, j * 32 - 200, i * 32 - 200)
                    self.add_room_object(E)
                    self.EObj.append(E)
                    self.indexE += 1
                elif obj == "G":
                    G = MLBL2_Tree(self, j * 32 - 200, i * 32 - 200, "ML2_Btree.png")
                    self.add_room_object(G)
                    self.GObj.append(G)
                    self.indexG += 1
                elif obj == "S":
                    S = MLBL2_Snake(self, j * 32 - 200, i * 32 - 200, "ML2_Snake.png")
                    self.add_room_object(S)
                    self.SObj.append(S)
                    self.indexS += 1
                    self.add_room_object(S)

        # self.set_timer(60, self.complete)
    def deleteObjects1(self, create, danceArrows):
        if danceArrows:
            self.startMoving = True
            for i in range(self.indexB):
                obj = self.BObj[i]
                if obj.x >= 532 and not obj.x >= 1040:
                    pass
                else:
                    self.delete_object(obj)
            for i in range(self.indexT):
                obj = self.TObj[i]
                if obj.x >= 532 and not obj.x >= 1040:
                    pass
                else:
                    self.delete_object(obj)
            for i in range(self.indexG):
                obj = self.GObj[i]
                if obj.x >= 532 and not obj.x >= 1040:
                    pass
                else:
                    self.delete_object(obj)
            for i in range(self.indexE):
                obj = self.EObj[i]
                if obj.x >= 532 and not obj.x >= 1040:
                    pass
                else:
                    self.delete_object(obj)
            for i in range(self.indexS):
                obj = self.SObj[i]
                if obj.x >= 532 and not obj.x >= 1040:
                    pass
                else:
                    self.delete_object(obj)
        else:
            for i in range(self.indexB):
                self.delete_object(self.BObj[i])
            for i in range(self.indexT):
                self.delete_object(self.TObj[i])
            for i in range(self.indexG):
                self.delete_object(self.GObj[i])
            for i in range(self.indexE):
                self.delete_object(self.EObj[i])
        if create:
            self.OverlayBG = OverlayTextBG(self, 0, 540)
            self.add_room_object(self.OverlayBG)
            self.add_room_object(scoreText_MLBL3(self, 700, 50, f'Score: {self.points}', 60, 'Comic Sans MS', (255, 255, 255), False, True))
            self.add_room_object(scoreText_MLBL3(self, 700, 150, f'Speed: {self.y_speed}', 60, 'Comic Sans MS', (255, 255, 255), False, False))
            self.deleteObjects2(True)





    def deleteObjects2(self, create):
        for i in range(self.indexB):
            self.add_room_object(self.BObj[i])
        for i in range(self.indexT):
            self.add_room_object(self.TObj[i])
        for i in range(self.indexG):
            self.add_room_object(self.GObj[i])
        for i in range(self.indexE):
            self.add_room_object(self.EObj[i])
        if create:
            self.set_timer(10, self.addObjects)
    def calcPos(self, x, y, obj):
        pos = self.peoplePos.index((x, y))
        obj.pos = pos
    def addObjects(self):
        self.OverlayBG.updateBody()
        self.OverlayBG.updateTitle()
    def complete(self):
        if Globals.direct_select:
            Globals.direct_select = False
            Globals.next_level = EnumLevels.Home
        self.running = False


from msilib.schema import CreateFolder
from GameFrame import Level, TextObject, Globals, EnumLevels
import os
from Objects import MLBL2_Tree, Player_MLBL2, ML2_People, ML2_Elders, Wallaby, scoreText_MLBL3, MLBL2_Snake, Wallaby_MLBL2
from Objects.StoryOverlay import OverlayTextBG
class Mil_G2(Level):
    def __init__(self, screen, joysticks, direct=False):
        Level.__init__(self, screen, joysticks)
        self.y_speed = -1.2
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
            "      T    EEE              ZZZZZ           B",
            "      T                    Z     Z          B",
            "      B                   Z       Z         G",
            "      G                   Z       Z         G",
            "      T     S             Z       Z         G",             
            "      T                    Z     Z          T",
            "      B                     Z   Z           T",
            "      G                                     B",
            "      G                                     B",
            "      T                                     G",
            "      T                                     T",
            "      G                                     B",
            "      G                       P             T",
            "      T                                     B",
            "BBBBBBBGGTTBGGGBTTBBBBTTTTBBB   BBGGTBTBBBTTTBB",
            "                              K                ",
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
                    Z = ML2_People(self, j * 32 - 200, i * 32 - 200, "ML2_people1.png")
                    self.add_room_object(Z)
                    self.ZObj.append(Z)
                    self.indexZ += 1
                elif obj == "Y":
                    self.add_room_object(ML2_People(self, j * 32 - 200, i * 32 - 200, "ML2_people2.png"))
                elif obj == "X":
                    self.add_room_object(ML2_People(self, j * 32 - 200, i * 32 - 200, "ML2_people3.png"))
                elif obj == "W":
                    self.add_room_object(ML2_People(self, j * 32 - 200, i * 32 - 200, "ML2_people4.png"))
                elif obj == "V":
                    self.add_room_object(ML2_People(self, j * 32 - 200, i * 32 - 200, "ML2_people5.png"))
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
            for i in range(self.indexZ):
                obj = self.ZObj[i]
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
    
    def addObjects(self):
        self.OverlayBG.updateBody()
        self.OverlayBG.updateTitle()
    def complete(self):
        if Globals.direct_select:
            Globals.direct_select = False
            Globals.next_level = EnumLevels.Home
        self.running = False


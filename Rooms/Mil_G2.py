from msilib.schema import CreateFolder
from GameFrame import Level, TextObject, Globals, EnumLevels
import os
from Objects import MLBL2_Tree, Player_MLBL2, ML2_People, ML2_Elders
from Objects.Dance_MLBL3 import scoreText_MLBL3
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
        self.indexT = 0
        self.indexG = 0
        self.indexB = 0
        self.indexE = 0
        self.arrows = []
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
            "      T    EEE             ZZZZZZZ          B",
            "      T                   ZZ     ZZ         B",
            "      B                  ZZ       ZZ        G",
            "      G                  ZZ       ZZ        G",
            "      T                  ZZ       ZZ        G",
            "      T                   ZZ     ZZ         T",
            "      B                    ZZ   ZZ          T",
            "      G                                     B",
            "      G                                     B",
            "      T                                     G",
            "      T                                     T",
            "      G                                     B",
            "      G                       P             T",
            "      T                                     B",
            "BBBBBBBGGTTBGGGBTTBBBBTTTTBBBBTBBBGGTBTBBBTTTBB",
            "                                              ",
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
                    E = ML2_Elders(self, j * 32 - 200, i * 32 - 200)
                    self.add_room_object(E)
                    self.EObj.append(E)
                    self.indexE += 1
                elif obj == "G":
                    G = MLBL2_Tree(self, j * 32 - 200, i * 32 - 200, "ML2_Btree.png")
                    self.add_room_object(G)
                    self.GObj.append(G)
                    self.indexG += 1

        # self.set_timer(60, self.complete)
    def deleteObjects1(self, create, danceArrows):
        if danceArrows:
            for i in range(self.indexB):
                obj = self.BObj[i]
                if obj.x >= 532:
                    pass
                else:
                    self.delete_object(obj)
            for i in range(self.indexT):
                obj = self.TObj[i]
                if obj.x >= 532:
                    pass
                else:
                    self.delete_object(obj)
            for i in range(self.indexG):
                obj = self.GObj[i]
                if obj.x >= 532:
                    pass
                else:
                    self.delete_object(obj)
            for i in range(self.indexE):
                obj = self.EObj[i]
                if obj.x >= 532:
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
    
    def addObjects(self):
        self.OverlayBG.updateBody()
        self.OverlayBG.updateTitle()
    def complete(self):
        if Globals.direct_select:
            Globals.direct_select = False
            Globals.next_level = EnumLevels.Home
        self.running = False

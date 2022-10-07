import os
import random
from Objects import Copple1_Player, CopG1_Tree, CopG1_kangaroo, CopG1_Emu
from GameFrame import Level, Globals, TextObject, EnumLevels


class Cop_G1 (Level):
    def __init__(self, screen, joysticks, direct=False):
        Level.__init__(self, screen, joysticks)
        self.direct = direct
        self.LIVES = 0
        # - Information for Controller Overlay
        self.roomNum = EnumLevels.Cop_G1
        self.score_text = TextObject(self, 0, -1, 'Lives: %i' % self.LIVES)
        self.score_text.depth = 200
        self.score_text.colour = (255, 255, 255)
        self.score_text.update_text()
        self.add_room_object(self.score_text)

        self.set_background_image(os.path.join("MilbiL2", "ML2_background_cpy.jpg"))
        self.set_background_scroll(4)

        self.scrolling_objects = []

        self.add_room_object(Copple1_Player(self, Globals.SCREEN_WIDTH / 2 - 80, Globals.SCREEN_HEIGHT - 200))
        self.add_room_object(CopG1_kangaroo(self, Globals.SCREEN_WIDTH / 3 - 40, Globals.SCREEN_HEIGHT - 90))
        self.add_room_object(CopG1_Emu(self, Globals.SCREEN_WIDTH / 3 + 480, Globals.SCREEN_HEIGHT - 90))

        self.set_timer(30, self.update_lives)

        self.set_timer(60, self.add_tree)

        self.set_timer(2700, self.complete)

    def add_tree(self):
        tree = CopG1_Tree(self, random.randint(0, Globals.SCREEN_WIDTH), -200)
        self.scrolling_objects.append(tree)
        self.add_room_object(tree)
        Globals.total_count += 1
        if Globals.total_count < 5:
            self.set_timer(30, self.add_tree)

    def update_lives(self):
        if self.background_scroll_speed != 0:
            self.LIVES += 1
            self.score_text.text = 'Lives: %i' % self.LIVES
            self.score_text.update_text()
        self.set_timer(30, self.update_lives)

    def complete(self):
        if Globals.direct_select:
            Globals.direct_select = False
            Globals.next_level = EnumLevels.Home
        self.running = False

    def tree_hit(self):
        self.background_scroll_speed = 0
        for obj in self.scrolling_objects:
            obj.y_speed = 0

    def start_scroll_again(self):
        self.background_scroll_speed = 4
        for obj in self.scrolling_objects:
            obj.y_speed = 4


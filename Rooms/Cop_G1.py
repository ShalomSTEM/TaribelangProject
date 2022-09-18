import os
import random
from Objects import Copple1_Player, CopG1_Tree
from GameFrame import Level, Globals, TextObject, EnumLevels


class Cop_G1 (Level):
    def __init__(self, screen, joysticks, direct=False):
        Level.__init__(self, screen, joysticks)
        self.direct = direct
        # - Information for Controller Overlay
        self.roomNum = EnumLevels.Cop_G1
        self.score_text = TextObject(self, 0, -1, 'Lives: %i' % Globals.LIVES)
        self.score_text.depth = 200
        self.score_text.colour = (255, 255, 255)
        self.score_text.update_text()
        self.add_room_object(self.score_text)

        self.set_background_image(os.path.join("MilbiL2", "ML2_background.jpg"))
        self.set_background_scroll(4)

        self.add_room_object(Copple1_Player(self, Globals.SCREEN_WIDTH / 2 - 80, Globals.SCREEN_HEIGHT - 200))

        self.set_timer(60, self.add_tree)

    def add_tree(self):
        self.add_room_object(CopG1_Tree(self, random.randint(0, Globals.SCREEN_WIDTH), -200))
        Globals.total_count += 1
        if Globals.total_count < 5:
            self.set_timer(30, self.add_tree)

    def update_lives(self, value):
        Globals.LIVES += value
        if Globals.LIVES == 0:
            self.running = False
            self.quitting = True
        self.score_text.text = 'Lives: %i' % Globals.LIVES
        self.score_text.update_text()

        room_name = TextObject(self, 200, 300, "Copple Game Part 1", colour=(255, 255, 255))
        self.add_room_object(room_name)

        self.set_timer(60, self.complete)

    def complete(self):
        if Globals.direct_select:
            Globals.direct_select = False
            Globals.next_level = EnumLevels.Home
        self.running = False

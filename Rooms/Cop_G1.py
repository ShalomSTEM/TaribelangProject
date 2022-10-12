import os
import random
from GameFrame import Level, Globals, TextObject, EnumLevels
from Objects import Copple1_Player, CopG1_kangaroo, CopG1_Emu, CopG1_Tree


class Cop_G1 (Level):
    def __init__(self, screen, joysticks, direct=False):
        Level.__init__(self, screen, joysticks)
        self.direct = direct
        self.LIVES = 0
        # - Information for Controller Overlay
        self.roomNum = EnumLevels.Cop_G1
        self.score_text = TextObject(self, 0, -1, 'Timer: %i' % self.LIVES)
        self.score_text.depth = 200
        self.score_text.colour = (255, 255, 255)
        self.score_text.update_text()
        self.add_room_object(self.score_text)

        self.set_background_image(os.path.join("CoppleL1", "grass.png"))
        self.set_background_scroll(4)

        self.bg_music = self.load_sound("jazzyfrenchy.ogg")
        self.bg_music.play()

        self.hit_sound = self.load_sound("NPC_hit_1.ogg")

        self.can_hit_tree = True

        self.scrolling_objects = []

        self.add_room_object(Copple1_Player(self, Globals.SCREEN_WIDTH / 2 - 80, Globals.SCREEN_HEIGHT - 200))
        self.add_room_object(CopG1_kangaroo(self, Globals.SCREEN_WIDTH / 3 - 40, Globals.SCREEN_HEIGHT - 90))
        self.add_room_object(CopG1_Emu(self, Globals.SCREEN_WIDTH / 3 + 480, Globals.SCREEN_HEIGHT - 90))

        self.set_timer(30, self.update_lives)

        self.set_timer(60, self.add_tree)

        self.set_timer(1800, self.complete)

        self.set_timer(750, self.level_up)

    def add_tree(self):
        tree = CopG1_Tree(self, random.randint(0, Globals.SCREEN_WIDTH), -200)
        self.scrolling_objects.append(tree)
        self.add_room_object(tree)
        Globals.total_count += 1
        if Globals.total_count < 6:
            self.set_timer(30, self.add_tree)

    def update_lives(self):
        if self.background_scroll_speed != 0:
            self.LIVES += 1
            self.score_text.text = 'Timer: %i' % self.LIVES
            self.score_text.update_text()
        self.set_timer(30, self.update_lives)

    def complete(self):
        self.bg_music.stop()
        if Globals.direct_select:
            Globals.direct_select = False
            Globals.next_level = EnumLevels.Home
        self.running = False

    def tree_hit(self):
        if self.background_scroll_speed > 0 and self.can_hit_tree:
            self.can_hit_tree = False
            self.hit_sound.play()
        self.background_scroll_speed = 0
        for obj in self.scrolling_objects:
            obj.y_speed = 0

    def start_scroll_again(self):
        self.can_hit_tree = True
        self.background_scroll_speed = 6
        for obj in self.scrolling_objects:
            obj.y_speed = 6

    def level_up(self):
        if self.update_lives == 30:
            self.add_tree += 7
        self.set_timer(900, self.level_up)







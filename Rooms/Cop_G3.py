import pygame.mixer

from GameFrame import Level, Globals, EnumLevels, TextObject
from Objects import CopSwimBG, CopFish, CopRock, CopStick, Cop_Seaweed, CopLog, CopLog_Short, Waterlily


class Cop_G3(Level):
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)
        background_1 = CopSwimBG(self, 0, 0)
        background_2 = CopSwimBG(self, Globals.SCREEN_WIDTH, 0)
        self.add_room_object(background_1)
        self.add_room_object(background_2)
        self.add_room_object(CopFish(self, 65, Globals.SCREEN_HEIGHT / 2))

        # - Information for Controller Overlay
        self.roomNum = EnumLevels.Cop_G3

        self.active_objects = 0

        self.curr_index = 0
        self.type = ["rock", "seaweed", "rock", "log1", "stick", "seaweed", "log", "rock", "lily", "stick", "lily", "log1", "rock", "lily", "seaweed", "stick", "rock", "seaweed", "rock", "log1", "stick", "seaweed", "seaweed", "log", "rock", "stick", "rock"]
        self.location = [570, 150, 570, 360, 110, 360, 560, 570, 360, 110, 570, 360, 110, 200, 360, 160, 140, 180, 110, 570, 360, 110, 360, 160, 140, 180, 570]
        self.wait_time = [20, 30, 30, 60, 30, 30, 60, 40, 20, 50, 50, 20, 30, 30, 50, 40, 40, 50, 50, 40, 30, 50, 30, 50, 40, 40, 30]

        self.score = 0
        self.score_text = TextObject(self, 20, 0, f'Score: {self.score}')
        self.score_text.depth = 1000
        self.score_text.colour = (255, 255, 255)
        self.score_text.update_text()
        self.add_room_object(self.score_text)
        self.score_text.y = Globals.SCREEN_HEIGHT - self.score_text.height

        self.set_timer(self.wait_time[self.curr_index], self.add_obstacle)

        self.bg_music = self.load_sound("water_running.wav")
        self.sad_music = self.load_sound("LungeFishJourney.ogg")

        self.bg_music.set_volume(0.1)
        self.bg_music.play()

        self.set_timer(60, self.start_sad_music)

    def start_sad_music(self):
        self.sad_music.set_volume(1.0)
        self.sad_music.play()

    def complete(self):
        if Globals.direct_select:
            Globals.direct_select = False
            Globals.next_level = EnumLevels.Home
        self.sad_music.stop()
        self.bg_music.stop()
        self.running = False

    def add_obstacle(self):
        ob_type = self.type[self.curr_index]
        new_object = None
        if ob_type == "rock":
            new_object = CopRock(self, Globals.SCREEN_WIDTH, self.location[self.curr_index])
        elif ob_type == "stick":
            new_object = CopStick(self, Globals.SCREEN_WIDTH, self.location[self.curr_index])
        elif ob_type == "seaweed":
            new_object = Cop_Seaweed(self, Globals.SCREEN_WIDTH, self.location[self.curr_index])
        elif ob_type == "log":
            new_object = CopLog(self, Globals.SCREEN_WIDTH, self.location[self.curr_index])
        elif ob_type == "log1":
            new_object = CopLog_Short(self, Globals.SCREEN_WIDTH, self.location[self.curr_index])
        elif ob_type == "lily":
            new_object = Waterlily(self, Globals.SCREEN_WIDTH, self.location[self.curr_index])

        self.add_room_object(new_object)
        self.active_objects += 1

        self.curr_index += 1
        if self.curr_index < len(self.type):
            self.set_timer(self.wait_time[self.curr_index], self.add_obstacle)

    def add_points(self):
        self.score += 5
        self.score_text.text = f"Score {self.score}"
        self.score_text.update_text()
        self.active_objects -= 1
        if self.curr_index >= len(self.location) and self.active_objects <= 1:
            if Globals.direct_select:
                Globals.next_level = EnumLevels.Home
            self.complete()

    def remove_points(self):
        self.score -= 15
        self.score_text.text = f"Score {self.score}"
        self.score_text.update_text()
        self.active_objects -= 1
        if self.curr_index >= len(self.location) and self.active_objects <= 1:
            if Globals.direct_select:
                Globals.next_level = EnumLevels.Home
            self.complete()

from GameFrame import Level, Globals, EnumLevels
from Objects import CopSwimBG, CopFish, CopRock, CopStick



class Cop_G3(Level):
    def __init__(self, screen, joysticks, direct=False):
        Level.__init__(self, screen, joysticks)
        self.direct = direct
        background_1 = CopSwimBG(self, 0, 0)
        background_2 = CopSwimBG(self, Globals.SCREEN_WIDTH, 0)
        self.add_room_object(background_1)
        self.add_room_object(background_2)
        self.add_room_object(CopFish(self, 65, Globals.SCREEN_HEIGHT / 2))
        self.set_timer(180, self.complete)

        self.curr_index = 0
        self.type = ["rock", "rock", "rock", "rock", "stick"]
        self.location = [360, 50, 680, 360, 50]
        self.wait_time = [10, 30, 30, 60, 30]

        self.set_timer(self.wait_time[self.curr_index], self.add_obstacle)

    def complete(self):
        if Globals.direct_select:
            Globals.direct_select = False
            Globals.next_level = EnumLevels.Home
        self.running = False

    def add_obstacle(self):
        ob_type = self.type[self.curr_index]
        if ob_type == "rock":
            new_object = CopRock(self, Globals.SCREEN_WIDTH, self.location[self.curr_index])

            self.add_room_object(new_object)

            self.curr_index += 1
            if self.curr_index < len(self.type):
                self.set_timer(self.wait_time[self.curr_index], self.add_obstacle)

    """def add_obstacle(self):
        ob_type = self.type[self.curr_index]
        if ob_type == "stick":
            new_object = CopStick(self, Globals.SCREEN_WIDTH, self.location[self.curr_index])

            self.add_room_object(new_object)

        self.curr_index += 1
        if self.curr_index < len(self.type):
            self.set_timer(self.wait_time[self.curr_index], self.add_obstacle)
"""

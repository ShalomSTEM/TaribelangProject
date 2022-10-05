from GameFrame import Level, Globals, EnumLevels
from Objects import CopSwimBG, CopFish, CopRock, CopStick, Cop_Seaweed, CopLog, CopLog_Short, Waterlily


class Cop_G3(Level):
    def __init__(self, screen, joysticks, direct=False):
        Level.__init__(self, screen, joysticks)
        self.direct = direct
        background_1 = CopSwimBG(self, 0, 0)
        background_2 = CopSwimBG(self, Globals.SCREEN_WIDTH, 0)
        self.add_room_object(background_1)
        self.add_room_object(background_2)
        self.add_room_object(CopFish(self, 65, Globals.SCREEN_HEIGHT / 2))

        # - Information for Controller Overlay
        self.roomNum = EnumLevels.Cop_G3

        self.curr_index = 0
        self.type = ["rock", "seaweed", "rock", "log1", "stick", "seaweed", "log", "rock", "stick", "lily", "log1", "rock", "lily", "seaweed", "stick"]
        self.location = [360, 60, 680, 360, 70, 360, 670, 70, 110, 200, 360, 60, 140, 70, 360]
        self.wait_time = [20, 30, 30, 60, 30, 30, 60, 40, 50, 50, 20, 30, 30, 50, 40]

        self.set_timer(self.wait_time[self.curr_index], self.add_obstacle)

    def complete(self):
        if Globals.direct_select:
            Globals.direct_select = False
            Globals.next_level = EnumLevels.Home
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

        self.curr_index += 1
        if self.curr_index < len(self.type):
            self.set_timer(self.wait_time[self.curr_index], self.add_obstacle)


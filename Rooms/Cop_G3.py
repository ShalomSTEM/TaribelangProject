from GameFrame import Level, Globals, EnumLevels
from Objects import CopSwimBG


class Cop_G3(Level):
    def __init__(self, screen, joysticks, direct=False):
        Level.__init__(self, screen, joysticks)
        self.direct = direct
        background_1 = CopSwimBG(self, 0, 0)
        background_2 = CopSwimBG(self, Globals.SCREEN_WIDTH, 0)
        self.add_room_object(background_1)
        self.add_room_object(background_2)

        #self.add_room_object(CopSky(self, 0, 0))
        #self.add_room_object(CopFish(self, 200, 300))
        self.set_timer(180, self.complete)

    def complete(self):
        if Globals.direct_select:
            Globals.direct_select = False
            Globals.next_level = EnumLevels.Home
        self.running = False

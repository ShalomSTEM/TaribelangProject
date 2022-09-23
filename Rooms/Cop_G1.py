from GameFrame import Level, TextObject, Globals, EnumLevels


class Cop_G1(Level):
    def __init__(self, screen, joysticks, direct=False):
        Level.__init__(self, screen, joysticks)

        self.direct = direct

        # - Information for Controller Overlay
        self.roomNum = EnumLevels.Cop_G1

        room_name = TextObject(self, 200, 300, "Copple Game Part 1", colour=(255, 255, 255))
        self.add_room_object(room_name)

        self.set_timer(60, self.complete)

    def complete(self):
        if Globals.direct_select:
            Globals.direct_select = False
            Globals.next_level = EnumLevels.Home
        self.running = False

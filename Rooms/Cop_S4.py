from GameFrame import Level, TextObject, Globals, EnumLevels


class Cop_S4(Level):
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)

        room_name = TextObject(self, 200, 300, "Copple Story Part 4", colour="white")
        self.add_room_object(room_name)

        self.set_timer(60, self.complete)

    def complete(self):
        Globals.next_level = EnumLevels.Home
        self.running = False

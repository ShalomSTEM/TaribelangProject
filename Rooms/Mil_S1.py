from GameFrame import Level, TextObject


class Mil_S1(Level):
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)

        room_name = TextObject(self, 200, 300, "Milbi Story Part 1", colour=(255, 255, 255))
        self.add_room_object(room_name)

        self.set_timer(60, self.complete)

    def complete(self):
        self.running = False

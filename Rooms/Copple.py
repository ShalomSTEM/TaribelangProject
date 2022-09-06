from GameFrame import Globals, PlaceholderLevel

class Copple(PlaceholderLevel):
    def __init__(self, screen, joysticks):
        PlaceholderLevel.__init__(self, screen, joysticks, 'Copple', Globals.EnumLevels.Home)




"""class Copple(PlaceholderLevel):
    def __init__(self, screen, joysticks):
        PlaceHol.__init__(self, screen, joysticks)
        text = TextObject(self, Globals.SCREEN_HEIGHT/2, Globals.SCREEN_HEIGHT/2, text='Copple', size=60, font='Comic Sans MS', colour=(255, 255, 255))
        self.add_room_object(text)
        self.running = False"""
from GameFrame import Globals, PlaceholderLevel

class Intro(PlaceholderLevel):
    def __init__(self, screen, joysticks):
        PlaceholderLevel.__init__(self, screen, joysticks, 'Intro', Globals.EnumLevels.Home)
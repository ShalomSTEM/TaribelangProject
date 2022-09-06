from GameFrame import Globals, PlaceholderLevel

class Museum(PlaceholderLevel):
    def __init__(self, screen, joysticks):
        PlaceholderLevel.__init__(self, screen, joysticks, 'Museum', Globals.EnumLevels.Home)
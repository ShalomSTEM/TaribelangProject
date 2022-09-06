from GameFrame import Globals, PlaceholderLevel

class Quiz(PlaceholderLevel):
    def __init__(self, screen, joysticks):
        PlaceholderLevel.__init__(self, screen, joysticks, 'Quiz', Globals.EnumLevels.Home)
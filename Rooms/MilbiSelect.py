from GameFrame import Globals, PlaceholderLevel

class MilbiSelect(PlaceholderLevel):
    def __init__(self, screen, joysticks):
        PlaceholderLevel.__init__(self, screen, joysticks, 'MilbiSelect', Globals.EnumLevels.Home)
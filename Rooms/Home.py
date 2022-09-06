from GameFrame import Globals, Level, PlaceholderLevel
from GameFrame.TextObject import TextObject
class Home(PlaceholderLevel):
    def __init__(self, screen, joysticks):
        PlaceholderLevel.__init__(self, screen, joysticks, 'Home', Globals.EnumLevels.MilbiSelect)
        
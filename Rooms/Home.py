from GameFrame import Globals, Level, PlaceholderLevel
from GameFrame.TextObject import TextObject
from Objects import ButtonForPlaceholder
class Home(PlaceholderLevel):
    def __init__(self, screen, joysticks):
        PlaceholderLevel.__init__(self, screen, joysticks, 'Home', Globals.EnumLevels.MilbiSelect)
        button1 = ButtonForPlaceholder(self, 160, 160)
        self.add_room_object(button1)
        
from GameFrame import Globals, Level, TextObject
from time import sleep

class PlaceholderLevel(Level):
    def __init__(self, screen, joysticks, inputText, nextLevel):
        Level.__init__(self, screen, joysticks)
        text = TextObject(self, Globals.SCREEN_WIDTH/2, Globals.SCREEN_HEIGHT/2, text=inputText, size=60, font='Comic Sans MS', colour=(255, 255, 255))
        self.add_room_object(text)
        sleep(2)
        Globals.next_level = nextLevel
        self.running = False
        
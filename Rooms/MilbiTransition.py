from array import array
from time import sleep
from GameFrame import Level, Globals
from Objects.TransitionButton import TransitionButton


class MilbiTransition(Level):
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)
        self.set_background_image("MilbiL3/PlaceHolderBackgroundMLBL3.png")
        button1 = TransitionButton(
            self,
            80,
            160,
            Globals.EnumWTC_Taribelang,
            "Images/Transition/story_only.png",
            False,
        )
        button3 = TransitionButton(
            self,
            880,
            160,
            Globals.EnumWTC_Taribelang,
            "Images/Transition/games_only.png",
            True,
        )
        button2 = TransitionButton(
            self,
            480,
            160,
            Globals.EnumWTC_Taribelang,
            "Images/Transition/both_selected.png",
            False,
        )
        self.add_room_object(button1)
        self.add_room_object(button2)
        self.add_room_object(button3)
        currentSelected = 2

        @staticmethod
        def updateButton3(self, left, right):
            if left == True:
                button2.updateImage("Images/Transition/both_selected.png", True)
                button3.updateImage("Images/Transition/games_only", False)
            elif right == True:
                button3.updateImage("Images/Transition/games_only.png", True)
                button1.updateImage("Images/Transition/story_only_selected.png", True)

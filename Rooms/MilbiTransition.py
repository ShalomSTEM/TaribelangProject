from GameFrame import Level, Globals, UpdateTransition
from Objects.TransitionButton import TransitionButton


class MilbiTransition(Level):
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)
        global button1, button2, button3
        self.set_background_image("MilbiL3/PlaceHolderBackgroundMLBL3.png")
        button1 = TransitionButton(
            self,
            80,
            160,
            Globals.EnumWTC_Taribelang,
            "Images/Transition/story_only.png",
            False,
            1,
        )
        button3 = TransitionButton(
            self,
            880,
            160,
            Globals.EnumWTC_Taribelang,
            "Images/Transition/games_only.png",
            False,
            3,
        )
        button2 = TransitionButton(
            self,
            480,
            160,
            Globals.EnumWTC_Taribelang,
            "Images/Transition/both_selected.png",
            True,
            2,
        )
        self.add_room_object(button1)
        self.add_room_object(button2)
        self.add_room_object(button3)

    @staticmethod
    def updateButtons():
        print(Globals.TransitionLeft, Globals.TransitionRight)
        print("successful update transition")
        print(Globals.ran)
        if Globals.currentSelectedTransition == 2:
            print("running currenttransition")
            if Globals.ran == False:
                Globals.ran = True
                if Globals.TransitionLeft == True:
                    Globals.TransitionLeft = False
                    button2.updateImage("Images/Transition/both.png", False)
                    button1.updateImage(
                        "Images/Transition/story_only_selected.png", True
                    )
                    Globals.currentSelectedTransition = 1

                if Globals.TransitionRight == True:
                    Globals.TransitionRight = False
                    button2.updateImage("Images/Transition/both.png", False)
                    button3.updateImage(
                        "Images/Transition/games_only_selected.png", True
                    )
                    Globals.currentSelectedTransition = 3

        elif Globals.currentSelectedTransition == 1:
            print("running currenttransition")
            if Globals.ran == False:
                Globals.ran = True
                if Globals.TransitionLeft == True:
                    Globals.TransitionLeft = False
                    button1.updateImage("Images/Transition/story_only.png", False)
                    button3.updateImage(
                        "Images/Transition/games_only_selected.png", True
                    )
                    Globals.currentSelectedTransition = 3
                if Globals.TransitionRight == True:
                    Globals.TransitionRight = False
                    button2.updateImage("Images/Transition/both_selected.png", True)
                    button1.updateImage("Images/Transition/story_only.png", False)
                    Globals.currentSelectedTransition = 2
        elif Globals.currentSelectedTransition == 3:
            print("running currenttransition")
            if Globals.ran == False:
                Globals.ran = True
                if Globals.TransitionLeft == True:
                    Globals.TransitionLeft = False
                    Globals.currentSelectedTransition = 2
                    button2.updateImage("Images/Transition/both_selected.png", True)
                    button3.updateImage("Images/Transition/games_only.png", False)
                if Globals.TransitionRight == True:
                    Globals.TransitionRight = False
                    Globals.currentSelectedTransition = 1
                    button3.updateImage("Images/Transition/games_only.png", False)
                    button1.updateImage(
                        "Images/Transition/story_only_selected.png", True
                    )

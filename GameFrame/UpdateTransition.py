from GameFrame import Globals
from Rooms.MilbiTransition import MilbiTransition


class UpdateTransition:
    while Globals.currentSelected == 2:
        if Globals.TransitionLeft == True:
            Globals.TransitionLeft == False
            MilbiTransition.updateButton3()
            currentSelected == 1
        elif Globals.TransitionRight == True:
            Globals.TransitionRight == False
            button2.updateImage("Images/Transition/both.png", False)
            button3.updateImage("Images/Transition/games_only_selected.png", True)
            currentSelected == 3
    while currentSelected == 1:
        if Globals.TransitionLeft == True:
            Globals.TransitionLeft == False
            button1.updateImage("Images/Transition/story_only.png", False)
            button3.updateImage("Images/Transition/games_only_selected.png", True)
            currentSelected == 3
        elif Globals.TransitionRight == True:
            Globals.TransitionRight == False
            button2.updateImage("Images/Transition/both_selected.png", True)
            button1.updateImage("Images/Transition/story_only.png", False)
            currentSelected == 2
    while currentSelected == 3:
        if Globals.TransitionLeft == True:
            Globals.TransitionLeft == False

            currentSelected == 2
        elif Globals.TransitionRight == True:
            Globals.TransitionRight == False

            currentSelected == 1

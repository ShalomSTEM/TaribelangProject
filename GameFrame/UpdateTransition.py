from GameFrame import Globals


class updateTransition:
    @staticmethod
    def updateTransition(button1, button2, button3):
        if Globals.currentSelectedTransition == 2:
            if Globals.TransitionLeft == True:
                Globals.TransitionLeft == False
                button2.updateImage("Images/Transition/both_selected.png", True)
                button3.updateImage("Images/Transition/games_only.png", False)
                Globals.currentSelectedTransition == 1
            if Globals.TransitionRight == True:
                Globals.TransitionRight == False
                button2.updateImage("Images/Transition/both.png", False)
                button3.updateImage("Images/Transition/games_only_selected.png", True)
                Globals.currentSelectedTransition == 3
        if Globals.currentSelectedTransition == 1:
            if Globals.TransitionLeft == True:
                Globals.TransitionLeft == False
                button1.updateImage("Images/Transition/story_only.png", False)
                button3.updateImage("Images/Transition/games_only_selected.png", True)
                Globals.currentSelectedTransition == 3
            if Globals.TransitionRight == True:
                Globals.TransitionRight == False
                button2.updateImage("Images/Transition/both_selected.png", True)
                button1.updateImage("Images/Transition/story_only.png", False)
                Globals.currentSelectedTransition == 2
        if Globals.currentSelectedTransition == 3:
            if Globals.TransitionLeft == True:
                Globals.TransitionLeft == False
                Globals.currentSelectedTransition == 2
            if Globals.TransitionRight == True:
                Globals.TransitionRight == False
                Globals.currentSelectedTransition == 1

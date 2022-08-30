from time import sleep
from GameFrame import Globals, RoomObject
import pygame


class TransitionButton(RoomObject):
    def __init__(self, room, x, y, level, image, selected, impbuttonNum):
        self.buttonNum = impbuttonNum
        RoomObject.__init__(self, room, x, y)
        self.set_image(
            image,
            height=(Globals.SCREEN_HEIGHT / 2),
            width=(Globals.SCREEN_WIDTH / 2) / 2,
        )
        self.handle_key_events = True

    def updateImage(self, image, selected):
        if self.buttonNum == Globals.currentSelectedTransition:
            self.set_image(
                image,
                height=(Globals.SCREEN_HEIGHT / 2),
                width=(Globals.SCREEN_WIDTH / 2) / 2,
            )
            if selected == True:
                self.selected = True
            else:
                self.selected = False

    def joy_pad_signal(self, p1_buttons, p2_buttons):
        # print(self.buttonNum, Globals.currentSelectedTransition)
        if p1_buttons[11] > 0.5:
            if Globals.currentSelectedTransition == self.buttonNum:
                from Rooms import MilbiTransition

                if Globals.continues == True:
                    Globals.continues = False
                    print("successful 0.5")
                    Globals.TransitionRight = True
                    sleep(1)
                    MilbiTransition.updateButtons()
                else:
                    return

        if p1_buttons[11] < -0.5:
            if Globals.currentSelectedTransition == self.buttonNum:
                from Rooms import MilbiTransition

                if Globals.continues == True:
                    Globals.continues = False
                    print("successful -0.5")
                    Globals.TransitionLeft = True
                    sleep(1)
                    MilbiTransition.updateButtons()

    def key_pressed(self, key):

        if key[pygame.K_RIGHT]:
            sleep(1.5)
            # Globals.continues  = True
            if Globals.currentSelectedTransition == self.buttonNum:

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
                                MilbiTransition.button2.updateImage(
                                    "Images/Transition/both.png", False
                                )
                                MilbiTransition.button1.updateImage(
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
                                button1.updateImage(
                                    "Images/Transition/story_only.png", False
                                )
                                button3.updateImage(
                                    "Images/Transition/games_only_selected.png", True
                                )
                                Globals.currentSelectedTransition = 3
                            if Globals.TransitionRight == True:
                                Globals.TransitionRight = False
                                button2.updateImage(
                                    "Images/Transition/both_selected.png", True
                                )
                                button1.updateImage(
                                    "Images/Transition/story_only.png", False
                                )
                                Globals.currentSelectedTransition = 2
                    elif Globals.currentSelectedTransition == 3:
                        print("running currenttransition")
                        if Globals.ran == False:
                            Globals.ran = True
                            if Globals.TransitionLeft == True:
                                Globals.TransitionLeft = False
                                Globals.currentSelectedTransition = 2
                                button2.updateImage(
                                    "Images/Transition/both_selected.png", True
                                )
                                button3.updateImage(
                                    "Images/Transition/games_only.png", False
                                )
                            if Globals.TransitionRight == True:
                                Globals.TransitionRight = False
                                Globals.currentSelectedTransition = 1
                                button3.updateImage(
                                    "Images/Transition/games_only.png", False
                                )
                                button1.updateImage(
                                    "Images/Transition/story_only_selected.png", True
                                )

                from Rooms import MilbiTransition

                print(
                    "successful 0.5", self.buttonNum, Globals.currentSelectedTransition
                )
                Globals.TransitionRight = True
                MilbiTransition.updateButtons()
                Globals.ran = False
                # else:
                #     return
        if key[pygame.K_LEFT]:
            if Globals.currentSelectedTransition == self.buttonNum:
                from Rooms import MilbiTransition

                Globals.ran = False
                print("successful -0.5")
                Globals.TransitionLeft = True
                sleep(1)
                MilbiTransition.updateButtons()

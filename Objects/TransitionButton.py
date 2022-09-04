from time import sleep
from GameFrame import Globals, RoomObject
from Rooms import MilbiTransition
import pygame


class TransitionButton(RoomObject):
    def __init__(self, room, x, y, level, image, selected, impbuttonNum):
        self.buttonNum = impbuttonNum
        self.selected = selected
        RoomObject.__init__(self, room, x, y)
        self.set_image(
            image,
            height=(Globals.SCREEN_HEIGHT / 2),
            width=(Globals.SCREEN_WIDTH / 2) / 2,
        )
        self.handle_key_events = True
        self.selected = True

    def updateImage(self, image, selected):
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

                print("successful -0.5")
                Globals.TransitionLeft = True
                sleep(1)
                MilbiTransition.updateButtons()

        if p1_buttons[11] < -0.5:
            if Globals.currentSelectedTransition == self.buttonNum:
                from Rooms import MilbiTransition

                print("successful 0.5")
                Globals.TransitionRight = True
                sleep(1)
                MilbiTransition.updateButtons()
                return

    def key_pressed(self, key):
        if key[pygame.K_LEFT]:
            if self.buttonNum == 2:
                Globals.TransitionButton2.updateImage(
                    "Images/Transition/both.png", False
                )
                Globals.TransitionButton1.updateImage(
                    "Images/Transition/story_only_selected.png", True
                )
            elif self.buttonNum == 1:
                Globals.TransitionButton1.updateImage(
                    "Images/Transition/story_only.png", False
                )
                Globals.TransitionButton3.updateImage(
                    "Images/Transition/games_only_selected.png", True
                )
            elif self.buttonNum == 3:
                Globals.TransitionButton2.updateImage(
                    "Images/Transition/both_selected.png", True
                )
                Globals.TransitionButton3.updateImage(
                    "Images/Transition/games_only.png", False
                )

        if key[pygame.K_RIGHT]:
            if self.buttonNum == 2:
                Globals.TransitionButton2.updateImage(
                    "Images/Transition/both.png", False
                )
                Globals.TransitionButton3.updateImage(
                    "Images/Transition/games_only_selected.png", True
                )
            elif self.buttonNum == 1:
                Globals.TransitionButton2.updateImage(
                    "Images/Transition/both_selected.png", True
                )
                Globals.TransitionButton1.updateImage(
                    "Images/Transition/story_only.png", False
                )
            elif self.buttonNum == 3:
                Globals.TransitionButton3.updateImage(
                    "Images/Transition/games_only.png", False
                )
                Globals.TransitionButton1.updateImage(
                    "Images/Transition/story_only_selected.png", True
                )

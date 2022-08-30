from time import sleep
from GameFrame import Globals, RoomObject
from Rooms import MilbiTransition
import pygame


class TransitionButton(RoomObject):
    buttomNum = int

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
            # Globals.continues = True
            if Globals.currentSelectedTransition == self.buttonNum:
                from Rooms import MilbiTransition

                Globals.ran = False
                print("successful 0.5")
                Globals.TransitionRight = True
                sleep(1)
                MilbiTransition.updateButtons()
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

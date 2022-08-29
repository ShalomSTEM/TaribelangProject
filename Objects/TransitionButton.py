from time import sleep
from GameFrame import Globals, RoomObject
from Rooms import MilbiTransition


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
            Globals.currentSelectedTransition == True
        else:
            Globals.currentSelectedTransition == False

    def joy_pad_signal(self, p1_buttons, p2_buttons):
        # print(self.buttonNum, Globals.currentSelectedTransition)
        if p1_buttons[11] > 0.5:
            if Globals.currentSelectedTransition == self.buttonNum:
                from Rooms import MilbiTransition

                print("successful 0.5")
                Globals.TransitionRight = True
                sleep(1)
                MilbiTransition.updateButtons()

        if p1_buttons[11] < -0.5:
            if Globals.currentSelectedTransition == self.buttonNum:
                from Rooms import MilbiTransition

                print("successful -0.5")
                Globals.TransitionLeft = True
                sleep(1)
                MilbiTransition.updateButtons()

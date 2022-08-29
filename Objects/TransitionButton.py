from time import sleep
from GameFrame import Globals, RoomObject
from Rooms import MilbiTransition


class TransitionButton(RoomObject):
    isSelected = bool

    def __init__(self, room, x, y, level, image, selected):
        global isSelected
        isSelected = selected
        RoomObject.__init__(self, room, x, y)
        self.set_image(
            image,
            height=(Globals.SCREEN_HEIGHT / 2),
            width=(Globals.SCREEN_WIDTH / 2) / 2,
        )
        self.handle_key_events = True

    def updateImage(self, image, selected):
        global isSelected
        self.set_image(
            image,
            height=(Globals.SCREEN_HEIGHT / 2),
            width=(Globals.SCREEN_WIDTH / 2) / 2,
        )
        if selected == True:
            isSelected == True
        elif selected == False:
            isSelected == False

    def joy_pad_signal(self, p1_buttons, p2_buttons):
        global isSelected
        if p1_buttons[11] > 0.5:
            if isSelected == True:
                from Rooms import MilbiTransition

                print("successful 0.5")
                Globals.TransitionRight = True
                sleep(0.1)
                MilbiTransition.updateButtons()

        if p1_buttons[11] < -0.5:
            if isSelected == True:
                from Rooms import MilbiTransition

                print("successful -0.5")
                isSelected = False
                Globals.TransitionLeft = True
                sleep(0.1)
                MilbiTransition.updateButtons()

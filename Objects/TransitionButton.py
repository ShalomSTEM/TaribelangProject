from GameFrame import Globals, RoomObject


class TransitionButton(RoomObject):
    isSelected = bool

    def __init__(self, room, x, y, level, image, selected: False):
        isSelected = selected
        RoomObject.__init__(self, room, x, y)
        self.set_image(
            image,
            height=(Globals.SCREEN_HEIGHT / 2),
            width=(Globals.SCREEN_WIDTH / 2) / 2,
        )
        self.handle_key_events = True

    def updateImage(self, image, selected: False):
        self.set_image(
            image,
            height=(Globals.SCREEN_HEIGHT / 2),
            width=(Globals.SCREEN_WIDTH / 2) / 2,
        )
        if selected == True:
            self.isSelected == True
        elif selected == False:
            self.isSelected == False

    def joy_pad_signal(self, p1_buttons, p2_buttons):
        if p1_buttons[1] != 0:
            if self.isSelected == True:
                self.startTransition()
        if p1_buttons[11] > 0.5:
            if self.isSelected == True:
                self.isSelected = False
                Globals.TransitionRight = True
        if p1_buttons[11] < -0.5:
            if self.isSelected == True:
                self.isSelected = False
                Globals.TransitionLeft = True

from GameFrame import RoomObject, Globals
import os
import time


class TitleMilbiButton(RoomObject):
    def __init__(self, room, x, y, level):
        RoomObject.__init__(self, room, x, y)
        self.set_image(
            "Images/MilbiL1/Brown.png",
            height=Globals.SCREEN_HEIGHT - Globals.SCREEN_HEIGHT / 4,
            width=Globals.SCREEN_WIDTH - Globals.SCREEN_WIDTH / 4,
        )
        self.handle_key_events = True

    @staticmethod
    def updateTitle(self):
        # TitleLeftButton.updateTitle(self)
        if Globals.title_Level == 0:
            self.set_image(
                os.path.join(Globals.title_path, "wtc.png"),
                height=Globals.SCREEN_HEIGHT - Globals.SCREEN_HEIGHT / 4,
                width=Globals.SCREEN_WIDTH - Globals.SCREEN_WIDTH / 4,
            )
            time.sleep(0.25)
        elif Globals.title_Level == 1:
            self.set_image(
                os.path.join(Globals.title_path, "milbi.png"),
                height=Globals.SCREEN_HEIGHT - Globals.SCREEN_HEIGHT / 4,
                width=Globals.SCREEN_WIDTH - Globals.SCREEN_WIDTH / 4,
            )
            time.sleep(0.25)
        elif Globals.title_Level == 2:
            self.set_image(
                os.path.join(Globals.title_path, "carpet_snake.png"),
                height=Globals.SCREEN_HEIGHT - Globals.SCREEN_HEIGHT / 4,
                width=Globals.SCREEN_WIDTH - Globals.SCREEN_WIDTH / 4,
            )
            time.sleep(0.25)
        elif Globals.title_Level == 3:
            self.set_image(
                os.path.join(Globals.title_path, "museum.png"),
                height=Globals.SCREEN_HEIGHT - Globals.SCREEN_HEIGHT / 4,
                width=Globals.SCREEN_WIDTH - Globals.SCREEN_WIDTH / 4,
            )
            time.sleep(0.25)
        elif Globals.title_Level == 4:
            self.set_image(
                os.path.join(Globals.title_path, "quiz.png"),
                height=Globals.SCREEN_HEIGHT - Globals.SCREEN_HEIGHT / 4,
                width=Globals.SCREEN_WIDTH - Globals.SCREEN_WIDTH / 4,
            )
            time.sleep(0.25)
        elif Globals.title_Level == -1:
            Globals.title_Level = 4
            TitleMilbiButton.updateTitle(self)
        elif Globals.title_Level == 5:
            Globals.title_Level = 0
            TitleMilbiButton.updateTitle(self)

    def startSelection(self):
        if Globals.title_Level == 0:
            # wtc
            pass
        elif Globals.title_Level == 1:
            # milbi
            pass
        elif Globals.title_Level == 2:
            # carpet
            pass
        elif Globals.title_Level == 3:
            # museum
            pass
        elif Globals.title_Level == 4:
            # quiz
            pass
        elif Globals.title_Level == -1:
            Globals.title_Level = 4
            TitleMilbiButton.updateTitle(self)
        elif Globals.title_Level == 5:
            Globals.title_Level = 0
            TitleMilbiButton.updateTitle(self)

    def joy_pad_signal(self, p1_buttons, p2_buttons):
        if p1_buttons[11] > 0.5:
            print("10 positive")
            Globals.title_Level -= 1
            TitleMilbiButton.updateTitle(self)
        if p1_buttons[11] < -0.5:
            print("10 neg")
            Globals.title_Level += 1
            TitleMilbiButton.updateTitle(self)
        if p1_buttons[10] < -0.5:
            print("11 neg")
        if p1_buttons[10] > 0.5:
            print("11 pos")
        if p1_buttons[1] != 0:
            print("A")
            TitleMilbiButton.startSelection(self)

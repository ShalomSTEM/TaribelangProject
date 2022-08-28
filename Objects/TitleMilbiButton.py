from GameFrame import RoomObject, Globals
import os


class TitleMilbiButton(RoomObject):
    def __init__(self, room, x, y, level):
        RoomObject.__init__(self, room, x, y)
        self.set_image(
            "Images/Title/button.png",
            height=Globals.SCREEN_HEIGHT - Globals.SCREEN_HEIGHT / 4,
            width=Globals.SCREEN_WIDTH - Globals.SCREEN_WIDTH / 4,
        )
        self.handle_key_events = True
        update = updateTitle()

    def updateTitle(self):
        if Globals.title_Level == 0:
            self.set_image(
                "Images/Title/button.png",
                height=Globals.SCREEN_HEIGHT - Globals.SCREEN_HEIGHT / 4,
                width=Globals.SCREEN_WIDTH - Globals.SCREEN_WIDTH / 4,
            )
        elif Globals.title_Level == 1:
            self.set_image(
                "Images/StoryOverlay/body_example.png",
                height=Globals.SCREEN_HEIGHT - Globals.SCREEN_HEIGHT / 4,
                width=Globals.SCREEN_WIDTH - Globals.SCREEN_WIDTH / 4,
            )
        elif Globals.title_Level == 2:
            self.set_image(
                "Images/StoryOverlay/title_example.png",
                height=Globals.SCREEN_HEIGHT - Globals.SCREEN_HEIGHT / 4,
                width=Globals.SCREEN_WIDTH - Globals.SCREEN_WIDTH / 4,
            )
        elif Globals.title_Level == 3:
            self.set_image(
                "Images/Title/button.png",
                height=Globals.SCREEN_HEIGHT - Globals.SCREEN_HEIGHT / 4,
                width=Globals.SCREEN_WIDTH - Globals.SCREEN_WIDTH / 4,
            )
        elif Globals.title_Level == 4:
            self.set_image(
                "Images/Title/button.png",
                height=Globals.SCREEN_HEIGHT - Globals.SCREEN_HEIGHT / 4,
                width=Globals.SCREEN_WIDTH - Globals.SCREEN_WIDTH / 4,
            )
        elif Globals.title_Level == -1:
            Globals.title_Level = 4
            TitleMilbiButton.updateTitle(self)

    def joy_pad_signal(self, p1_buttons, p2_buttons):
        if p1_buttons[11] > 0.5:
            print("11 positive")
            Globals.title_Level -= 1
            TitleMilbiButton.updateTitle(self)
        if p1_buttons[11] < -0.5:
            print("11 neg")
            Globals.player_x += 1
            TitleMilbiButton.updateTitle(self)
        if p1_buttons[10] < -0.5:
            print("10 neg")
        if p1_buttons[10] > 0.5:
            print("10 pos")

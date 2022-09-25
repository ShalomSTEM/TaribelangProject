from GameFrame import EnumLevels, Level, TextObject, Globals
from Objects import RoomSelectButton, Listener, Controller, L_DpadOverlay
import os


class Home(Level):
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)
        # - Set a background with information - #
        self.set_background_image(os.path.join("Title", "home_bg.png"))
        self.add_room_object(Listener(self, 0, 0))

        # - Information for Controller Overlay
        self.roomNum = EnumLevels.Home

        self.buttons = []

        milbi_button = RoomSelectButton(
            self,
            Globals.SCREEN_WIDTH / 4 - 128,
            60,
            EnumLevels.MilbiSelect,
            os.path.join("Title", "milbi_selected.png"),
            os.path.join("Title", "milbi.png"))
        self.buttons.append(milbi_button)
        self.add_room_object(milbi_button)

        copple_button = RoomSelectButton(
            self,
            Globals.SCREEN_WIDTH / 4 * 2 - 128,
            60,
            EnumLevels.CoppleSelect,
            os.path.join("Title", "copple_selected.png"),
            os.path.join("Title", "copple.png"))
        self.buttons.append(copple_button)
        self.add_room_object(copple_button)

        museum_button = RoomSelectButton(
            self,
            Globals.SCREEN_WIDTH / 4 * 3 - 128,
            60,
            EnumLevels.Museum,
            os.path.join("Title", "museum_selected.png"),
            os.path.join("Title", "museum.png"))
        self.buttons.append(museum_button)
        self.add_room_object(museum_button)
        self.selected_button = 1
        self.buttons[self.selected_button].set_selected(True)
        

    def right(self):
        if self.selected_button == 0 or self.selected_button == 1:
            self.buttons[self.selected_button].set_selected(False)
            self.selected_button += 1
            self.buttons[self.selected_button].set_selected(True)

    def left(self):
        if self.selected_button == 1 or self.selected_button == 2:
            self.buttons[self.selected_button].set_selected(False)
            self.selected_button -= 1
            self.buttons[self.selected_button].set_selected(True)
    def apply_selection(self):
        self.buttons[self.selected_button].activate()

    def key_signal(self, signal):
        if signal == "right":
            self.right()
        elif signal == "left":
            self.left()
        elif signal == "enter":
            self.apply_selection()
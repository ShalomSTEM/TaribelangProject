from GameFrame import EnumLevels, Level, TextObject, Globals
from Objects import RoomSelectButton, Listener
import os


class CoppleSelect(Level):
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)

        room_name = TextObject(self, 200, 50, "Copple Select", colour="white")
        self.add_room_object(room_name)

        self.add_room_object(Listener(self, 0, 0))

        self.buttons = []

        play_through_button = RoomSelectButton(
            self,
            Globals.SCREEN_WIDTH / 4 - 128,
            160,
            EnumLevels.Cop_S1,
            os.path.join("MilbiL1", "Brown.png"),
            os.path.join("MilbiL1", "Green.png"))
        self.buttons.append(play_through_button)
        self.add_room_object(play_through_button)

        story_only_button = RoomSelectButton(
            self,
            Globals.SCREEN_WIDTH / 4 * 2 - 128,
            160,
            EnumLevels.Cop_S_Only,
            os.path.join("MilbiL1", "Brown.png"),
            os.path.join("MilbiL1", "Green.png"))
        self.buttons.append(story_only_button)
        self.add_room_object(story_only_button)

        games_only_button = RoomSelectButton(
            self,
            Globals.SCREEN_WIDTH / 4 * 3 - 128,
            160,
            EnumLevels.Cop_G_Only_Select,
            os.path.join("MilbiL1", "Brown.png"),
            os.path.join("MilbiL1", "Green.png"))
        self.buttons.append(games_only_button)
        self.add_room_object(games_only_button)

        self.selected_button = 0
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

from GameFrame import EnumLevels, Level, TextObject, Globals
from Objects import RoomSelectButton, Listener
import os


class Cop_G_Only_Select(Level):
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)

        room_name = TextObject(self, 200, 50, "Copple Game Select", colour=(255, 255, 255))
        self.add_room_object(room_name)

        self.add_room_object(Listener(self, 0, 0))

        self.buttons = []

        running_game_button = RoomSelectButton(
            self,
            Globals.SCREEN_WIDTH / 4 - 128,
            160,
            EnumLevels.Cop_G1,
            os.path.join("MilbiL1", "Brown.png"),
            os.path.join("MilbiL1", "Green.png"))
        self.buttons.append(running_game_button)
        self.add_room_object(running_game_button)

        maze_game_button = RoomSelectButton(
            self,
            Globals.SCREEN_WIDTH / 4 * 2 - 128,
            160,
            EnumLevels.Cop_G2,
            os.path.join("MilbiL1", "Brown.png"),
            os.path.join("MilbiL1", "Green.png"))
        self.buttons.append(maze_game_button)
        self.add_room_object(maze_game_button)

        swimming_game_button = RoomSelectButton(
            self,
            Globals.SCREEN_WIDTH / 4 * 3 - 128,
            160,
            EnumLevels.Cop_G3,
            os.path.join("MilbiL1", "Brown.png"),
            os.path.join("MilbiL1", "Green.png"))
        self.buttons.append(swimming_game_button)
        self.add_room_object(swimming_game_button)

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
        Globals.direct_select = True
        self.buttons[self.selected_button].activate()

    def key_signal(self, signal):
        if signal == "right":
            self.right()
        elif signal == "left":
            self.left()
        elif signal == "enter":
            self.apply_selection()

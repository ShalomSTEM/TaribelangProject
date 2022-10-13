from GameFrame import EnumLevels, Level, TextObject, Globals
from Objects import RoomSelectButton, Listener
import os


class Mil_G_Only_Select(Level):
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)

        self.set_background_image(os.path.join("Title", "home_bg.png"))
        self.add_room_object(Listener(self, 0, 0))

        # - Information for Controller Overlay
        self.roomNum = EnumLevels.Cop_G_Only_Select

        self.buttons = []

        plains_game_button = RoomSelectButton(
            self,
            Globals.SCREEN_WIDTH / 4 - 128,
            60,
            EnumLevels.Mil_G1,
            os.path.join("Transition", "Mil_G1_selected.png"),
            os.path.join("Transition", "Mil_G1.png"),
            direct=True
        )
        self.buttons.append(plains_game_button)
        self.add_room_object(plains_game_button)

        corroboree_game_button = RoomSelectButton(
            self,
            Globals.SCREEN_WIDTH / 4 * 2 - 128,
            60,
            EnumLevels.Mil_G2,
            os.path.join("Transition", "Mil_G2_selected.png"),
            os.path.join("Transition", "Mil_G2.png"),
            direct=True
        )
        self.buttons.append(corroboree_game_button)
        self.add_room_object(corroboree_game_button)

        boss_battle_game_button = RoomSelectButton(
            self,
            Globals.SCREEN_WIDTH / 4 * 3 - 128,
            60,
            EnumLevels.Mil_G3,
            os.path.join("Transition", "Mil_G3_selected.png"),
            os.path.join("Transition", "Mil_G3.png"),
            direct=True
        )
        self.buttons.append(boss_battle_game_button)
        self.add_room_object(boss_battle_game_button)

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

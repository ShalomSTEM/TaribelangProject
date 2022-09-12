from GameFrame import EnumLevels, Level, TextObject, Globals
from Objects import RoomSelectButton, Listener
import os


class Home(Level):
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)
        """
        if Globals.shownControllerLayout:
            self.set_background_image(os.path.join("Images", "Title", "controller_overlay.png"))
            self.set_timer(60, self.background_image("Images", "Title", "background.png"))
        """
        room_name = TextObject(self, 200, 50, "Home - selector", colour=(255, 255, 255))
        self.add_room_object(room_name)

        self.add_room_object(Listener(self, 0, 0))

        self.buttons = []

        milbi_button = RoomSelectButton(
            self,
            Globals.SCREEN_WIDTH / 4 - 128,
            160,
            EnumLevels.MilbiSelect,
            os.path.join("Title", "milbi_selected.png"),
            os.path.join("Title", "milbi.png"))
        self.buttons.append(milbi_button)
        self.add_room_object(milbi_button)

        copple_button = RoomSelectButton(
            self,
            Globals.SCREEN_WIDTH / 4 * 2 - 128,
            160,
            EnumLevels.CoppleSelect,
            os.path.join("Title", "copple_selected.png"),
            os.path.join("Title", "copple.png"))
        self.buttons.append(copple_button)
        self.add_room_object(copple_button)

        museum_button = RoomSelectButton(
            self,
            Globals.SCREEN_WIDTH / 4 * 3 - 128,
            160,
            EnumLevels.Museum,
            os.path.join("Title", "museum_selected.png"),
            os.path.join("Title", "museum.png"))
        self.buttons.append(museum_button)
        self.add_room_object(museum_button)
        """
        quiz_button = RoomSelectButton(
            self,
            Globals.SCREEN_WIDTH / 4 + 32,
            460,
            EnumLevels.Quiz,
            os.path.join("MilbiL1", "Brown.png"),
            os.path.join("MilbiL1", "Green.png"))
        self.buttons.append(quiz_button)
        self.add_room_object(quiz_button)

        wtc_button = RoomSelectButton(
            self,
            Globals.SCREEN_WIDTH / 4 * 2 + 32,
            460,
            EnumLevels.Intro,
            os.path.join("MilbiL1", "Brown.png"),
            os.path.join("MilbiL1", "Green.png"))
        self.buttons.append(wtc_button)
        self.add_room_object(wtc_button)
        """
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
    # Up and down 
    """     
    def down(self):
        if self.selected_button == 0 or self.selected_button == 1:
            self.buttons[self.selected_button].set_selected(False)
            self.selected_button = 3
            self.buttons[self.selected_button].set_selected(True)
        elif self.selected_button == 2:
            self.buttons[self.selected_button].set_selected(False)
            self.selected_button = 4
            self.buttons[self.selected_button].set_selected(True)
    def up(self):
        if self.selected_button == 3:
            self.buttons[self.selected_button].set_selected(False)
            self.selected_button = 0
            self.buttons[self.selected_button].set_selected(True)
        elif self.selected_button == 4:
            self.buttons[self.selected_button].set_selected(False)
            self.selected_button = 2
            self.buttons[self.selected_button].set_selected(True)
"""
    def apply_selection(self):
        self.buttons[self.selected_button].activate()

    def key_signal(self, signal):
        if signal == "right":
            self.right()
        elif signal == "left":
            self.left()
        elif signal == "enter":
            self.apply_selection()
        elif signal == "dowm":
            self.down()
        elif signal == "up":
            self.up()
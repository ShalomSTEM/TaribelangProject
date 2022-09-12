from GameFrame import RoomObject, Globals
import os


class ButtonForPlaceholder(RoomObject):
    def __init__(self, room, x, y, next_level):
        RoomObject.__init__(self, room, x, y)

        self.next_level = next_level

        image = self.load_image(os.path.join("Title", "button.png"))
        self.set_image(image, 128, 128)

        self.handle_mouse_events = True

    def clicked(self, button_number):
        Globals.next_level = self.next_level
        self.room.running = False

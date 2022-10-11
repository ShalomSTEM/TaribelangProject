from GameFrame import RoomObject, Globals


class RoomSelectButton(RoomObject):
    def __init__(self, room, x, y, next_level, selected_image, unselected_image, direct=False):
        RoomObject.__init__(self, room, x, y)

        self.next_level = next_level
        self.selected_image = self.load_image(selected_image)
        self.unselected_image = self.load_image(unselected_image)
        self.direct = direct

        self.set_image(self.unselected_image, 256, 256)

        self.handle_mouse_events = True

    def set_selected(self, selected):
        if selected:
            Globals.change_select.play()
            self.set_image(self.selected_image, 256, 256)
        else:
            self.set_image(self.unselected_image, 256, 256)

    def clicked(self, button_number):
        self.activate()

    def activate(self):
        Globals.confirm_select.play()
        if self.direct:
            Globals.direct_select = True
        Globals.next_level = self.next_level
        self.room.running = False

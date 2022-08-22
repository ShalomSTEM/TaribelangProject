from GameFrame import RoomObject


class TitleMilbiButton(RoomObject):
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)
        self.set_image("Images/Title/button.png", height=69.5, width=200)

from GameFrame import RoomObject, Globals


class Title(RoomObject):
    def __init__(self, room, x, y, image):
        RoomObject.__init__(self, room, x, y)
        self.set_image(
            image,
            width=Globals.SCREEN_WIDTH / 5.05,
            height=Globals.SCREEN_HEIGHT / 5,
        )

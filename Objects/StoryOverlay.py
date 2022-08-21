from GameFrame import RoomObject, Globals
import os


class overlays(RoomObject):
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)
        self.set_image(
            os.path.join(Globals.storyOverlay_path, "StoryOverlay.png"),
            width=Globals.SCREEN_WIDTH / 5,
            height=720,
        )


class Title(RoomObject):
    def __init__(self, room, x, y, image):
        RoomObject.__init__(self, room, x, y)
        self.set_image(
            image,
            width=Globals.SCREEN_WIDTH / 5.05,
            height=Globals.SCREEN_HEIGHT / 5,
        )


class Body(RoomObject):
    def __init__(self, room, x, y, image):
        RoomObject.__init__(self, room, x, y)
        self.set_image(
            image,
            width=Globals.SCREEN_WIDTH / 5.05,
            height=(Globals.SCREEN_HEIGHT - (Globals.SCREEN_HEIGHT / 5.05)),
        )

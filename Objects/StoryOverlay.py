from GameFrame import RoomObject, Globals
import os

stretch = False


class overlays(RoomObject):
    def __init__(self, room, x, y, stretch):
        RoomObject.__init__(self, room, x, y)
        if stretch == False:
            self.set_image(
                os.path.join(Globals.storyOverlay_path, "StoryOverlay.png"),
                width=Globals.SCREEN_WIDTH / 5,
                height=Globals.SCREEN_HEIGHT,
            )
        else:
            self.set_image(
                os.path.join(Globals.storyOverlay_path, "StoryOverlay_stretched.png"),
                width=Globals.SCREEN_WIDTH,
                height=Globals.SCREEN_HEIGHT,
            )


class Title(RoomObject):
    def __init__(self, room, x, y, image, stretch: bool):
        RoomObject.__init__(self, room, x, y)
        if stretch == False:
            self.set_image(
                image,
                width=Globals.SCREEN_WIDTH / 5.05,
                height=Globals.SCREEN_HEIGHT / 5,
            )
        else:
            self.set_image(
                image,
                width=Globals.SCREEN_WIDTH,
                height=Globals.SCREEN_HEIGHT / 5,
            )


class Body(RoomObject):
    def __init__(self, room, x, y, image, stretch: bool):
        RoomObject.__init__(self, room, x, y)
        if stretch == False:
            self.set_image(
                image,
                width=Globals.SCREEN_WIDTH / 5.05,
                height=Globals.SCREEN_HEIGHT / 5,
            )
        else:
            self.set_image(
                image,
                width=Globals.SCREEN_WIDTH,
                height=Globals.SCREEN_HEIGHT - (Globals.SCREEN_HEIGHT / 5),
            )

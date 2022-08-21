from GameFrame import RoomObject, Globals


class overlays(RoomObject):
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)
        self.set_image(
            "Images/StoryOverlay/StoryOverlay.png",
            width=Globals.SCREEN_WIDTH / 5,
            height=720,
        )

from GameFrame import Level, StoryOverlayMaker


class ExampleSmallOverlay(Level):
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)
        StoryOverlayMaker.Overlay.createSmallOverlay(
            self,
            "Images/StoryOverlay/title_example.png",
            "Images/StoryOverlay/body_example.png",
        )

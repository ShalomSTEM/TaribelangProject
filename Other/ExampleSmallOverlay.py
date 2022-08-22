from GameFrame import Level, StoryOverlayMaker, Globals
import os


class ExampleSmallOverlay(Level):
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)
        StoryOverlayMaker.Overlay.createSmallOverlay(
            self,
            os.path.join(Globals.storyOverlay_path, "title_example.png"),
            os.path.join(Globals.storyOverlay_path, "body_example.png"),
        )

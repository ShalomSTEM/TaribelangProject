from GameFrame import Level, StoryOverlayMaker, Globals
import os


class Example(Level):
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)
        StoryOverlayMaker.Overlay.createOverlay(
            self,
            os.path.join(Globals.storyOverlay_path, "title_example.png"),
            os.path.join(Globals.storyOverlay_path, "body_example.png"),
        )

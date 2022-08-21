from GameFrame import Level, Globals
from Objects import OverlayBody, OverlayTitle, StoryOverlay


class Overlay:
    @staticmethod
    def createOverlay(self, titleText, bodyText):
        overlay = StoryOverlay.overlays(self, 0, 0)
        title = OverlayTitle.Title(self, 0, 0, titleText)
        body = OverlayBody.Body(self, 0, 145, bodyText)
        self.add_room_object(body)
        self.add_room_object(title)
        self.add_room_object(overlay)

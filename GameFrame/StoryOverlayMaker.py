from Objects import StoryOverlay


class Overlay:
    @staticmethod
    def createSmallOverlay(self, titleText, bodyText):
        overlay = StoryOverlay.overlays(self, 0, 0, False)
        title = StoryOverlay.Title(self, 0, 0, titleText, False)
        body = StoryOverlay.Body(self, 0, 145, bodyText, False)
        self.add_room_object(body)
        self.add_room_object(title)
        self.add_room_object(overlay)

    @staticmethod
    def createFullOverlay(self, titleText, bodyText):
        overlay = StoryOverlay.overlays(self, 0, 0, True)
        title = StoryOverlay.Title(self, 0, 0, titleText, True)
        body = StoryOverlay.Body(self, 0, 145, bodyText, True)
        self.add_room_object(body)
        self.add_room_object(title)
        self.add_room_object(overlay)

from GameFrame import RoomObject, TextObject
import os

from Objects.Dance_MLBL3 import Dance_MLBL3, DanceBG_MLBL3, DanceArrows_MLBL3

class OverlayTextBG(RoomObject):
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)
        self.bodyText = ['elder 1 talk', 'elder 2 talk', 'elder 3 talk']
        self.titleText = ['elder 1', 'elder 2', 'elder 3']
        self.currentTextBody = self.bodyText[0]
        self.currentIndexBody = 0
        self.currentTextTitle = self.titleText[0]
        self.currentIndexTitle = 0
        self.set_image(self.load_image(os.path.join("Overlays", 'OverlayText.png')), 1, 1)
        self.Title = TextOverlay(self.room, self.x, self.y, self.currentTextTitle, 60, 'Comic Sans MS', (255, 255, 255), False)
        self.Body = TextOverlay(self.room, self.x, self.y+70, self.currentTextBody, 40, 'Comic Sans MS', (255, 255, 255), False)
        self.room.add_room_object(self.Title)
        self.room.add_room_object(self.Body)
            
    def updateTitle(self):
        self.currentIndexTitle += 1
        self.currentTextTitle = self.titleText[self.currentIndexTitle]
        self.Title.text = self.currentTextTitle
        self.set_timer(10, self.Title.update_text)
        
    def updateBody(self):
        self.currentIndexBody += 1
        self.currentTextBody = self.bodyText[self.currentIndexBody]
        self.Body.text = self.currentTextBody
        self.set_timer(10, self.Body.update_text)
    def complete(self):
        for i in range(4):
            tmp = Dance_MLBL3(self.room, 200+(64*i), 300, i)
            self.room.arrows.append(tmp)
            self.room.add_room_object(tmp)
        for i in range(4):
            tmp = DanceArrows_MLBL3(self.room, 200+(64*i), 500, i)
            self.room.arrows.append(tmp)
            self.room.add_room_object(tmp)
        self.room.add_room_object(DanceBG_MLBL3(self.room, 190, 300))
        self.room.delete_object(self.Title)
        self.room.delete_object(self.Body)
        # self.room.delete_object(self)

class TextOverlay(TextObject):
    def __init__(self, room, x, y, text, size, font, colour, bold):
        TextObject.__init__(self, room, x, y, text, size, font, colour, bold)

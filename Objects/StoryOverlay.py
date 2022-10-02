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
        self.set_image(self.load_image(os.path.join("Overlays", 'OverlayText.png')), 1280, 180)
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
    def complete1(self):
        self.room.deleteObjects1(False, True)
        self.room.set_background_image(os.path.join("MilbiL2", "ML2_background.jpg"))
        for i in range(4):
            tmp = Dance_MLBL3(self.room, 20+(128*i), 0, i)
            self.room.arrows.append(tmp)
            self.room.add_room_object(tmp)
        for i in range(4):
            tmp = DanceArrows_MLBL3(self.room, 20+(128*i), 200+(100*i), i)
            self.room.arrows.append(tmp)
            self.room.add_room_object(tmp)
        self.room.add_room_object(DanceBG_MLBL3(self.room, 0, 0))
        self.room.delete_object(self.Title)
        self.room.delete_object(self.Body)
        self.set_image(self.load_image("listener.png"), 1, 1)
    

class TextOverlay(TextObject):
    def __init__(self, room, x, y, text, size, font, colour, bold):
        TextObject.__init__(self, room, x, y, text, size, font, colour, bold)

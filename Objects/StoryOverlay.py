from asyncio.proactor_events import _ProactorBaseWritePipeTransport
import os
from GameFrame import RoomObject, TextObject
from Objects import Dance_MLBL3, DanceBG_MLBL3, DanceArrows_MLBL3

class OverlayTextBG(RoomObject):
    def __init__(self, room, x, y, end):
        RoomObject.__init__(self, room, x, y)
        self.end3 = end
        if self.end3:
            self.set_image(self.load_image(os.path.join("Overlays", 'OverlayText.png')), 1280, 180)
        self.ran = False
        # Text for the StoryOverlay
        self.bodyText = [" ", "It's time for our corroboree!", 'We have brought our fastest dancer of all, the Wallaby!', "Let's go!"]
        self.titleText = [' ', 'Elder 1', 'Elder', 'Members']
        self.bodyText1 = [' ', '*Distant Talking*', '*Chatter about Elders talking', "Milbi was seen with Water!", "*Multiple gasps*", "Hold on, where is Milbi?", "Milbi ran off into the forest! I'll chase!"]
        self.titleText1 = [' ', 'Elders', 'Members', 'Elders', 'Members', 'Member', 'You']
        self.setup = False
        # Get the amount of values in the arrays and turn it into an int
        method = self.bodyText.__len__()
        self.count = method.real-1
        method = self.bodyText1.__len__()
        self.count1 = method.real-1
        self.end = False
        self.end2 = False
        
        # Set current text and add Index for arrays
        self.currentTextBody = self.bodyText[0]
        self.currentIndexBody = 0
        self.currentTextTitle = self.titleText[0]
        self.currentIndexTitle = 0
        self.arrow = []
        self.set_timer(10, self.checkdanceend)
        # Set background image and create text overlays
        self.set_image(self.load_image(os.path.join("Overlays", 'OverlayText.png')), 1280, 180)
        if not self.room.danceEnd:
            self.Title = TextOverlay(self.room, self.x, self.y, self.currentTextTitle, 60, 'Comic Sans MS', (255, 255, 255), False)
            self.Body = TextOverlay(self.room, self.x, self.y+70, self.currentTextBody, 40, 'Comic Sans MS', (255, 255, 255), False)
            self.room.add_room_object(self.Title)
            self.room.add_room_object(self.Body)
        
    def reAddText(self):
        self.room.add_room_object(self.Title)
        self.room.add_room_object(self.Body)
        self.title()
    def updateTitle(self, end):
        self.end1 = end
        if end and not self.setup:
            self.currentTextBody = self.bodyText1[0]
            self.currentTextTitle = self.titleText1[0]
            self.Body.update_text()
            self.Body.update_text()
            self.currentIndexBody = 0
            self.currentIndexTitle = 0
            self.setup = True
            self.title()
            self.body()
        elif end and self.setup:
            if self.currentIndexTitle < self.count1:
                self.currentIndexTitle += 1
                self.currentTextTitle = self.titleText1[self.currentIndexTitle]
                self.Title.text = self.currentTextTitle
                self.set_timer(5, self.Title.update_text)
                self.set_timer(100, self.title)
        
        else:
            if self.currentIndexTitle < self.count:
                self.currentIndexTitle += 1
                self.currentTextTitle = self.titleText[self.currentIndexTitle]
                self.Title.text = self.currentTextTitle
                self.set_timer(5, self.Title.update_text)
                self.set_timer(120, self.title)
    def body(self):
        if self.room.danceEnd:
            self.end = True
        self.updateBody(self.end)
    def title(self):
        if self.room.danceEnd:
            self.end1 = True
        self.updateTitle(self.end1)
    def updateBody(self, end):
        self.end = end
        if self.end and self.setup:
            if self.currentIndexBody == 6:
                self.room.runNPC = True
                self.room.endOverlay = True
            if self.currentIndexBody < self.count1:
                self.currentIndexBody += 1
                self.currentTextBody = self.bodyText1[self.currentIndexBody]
                self.Body.text = self.currentTextBody
                self.set_timer(5, self.Body.update_text)
                self.set_timer(100, self.body)
        elif not self.room.danceEnd:
            if self.currentIndexBody == 3:
                self.startedArrows = True
                self.complete1()
            if self.currentIndexBody < self.count:
                self.currentIndexBody += 1
                self.currentTextBody = self.bodyText[self.currentIndexBody]
                self.Body.text = self.currentTextBody
                self.set_timer(5, self.Body.update_text)
                self.set_timer(120, self.body)
        else:
            self.set_timer(40, self.body)
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
    
    def update(self):
        if self.end3:
            self.y_speed = self.y_speed + self.gravity
            self.x += self.x_speed
            self.y += self.y_speed
            self.rect.x = self.x
            self.rect.y = self.y
            if self.room.gameEnd:
                self.room.delete_object(self)
            if self.room.endOverlay:
                self.delete_object(self)
    def checkdanceend(self):
        if self.room.danceEnd and not self.end3 and not self.ran:
            self.ran = True
            self.room.deleteObjects2(False, True)
            self.room.set_background_image(os.path.join("MilbiL2", "ML2_background_cpy.jpg"))
            self.room.add_room_object(OverlayTextBG(self.room, 0, 540, True))
        else:
            self.set_timer(10, self.checkdanceend)
                
class TextOverlay(TextObject):
    def __init__(self, room, x, y, text, size, font, colour, bold):
        TextObject.__init__(self, room, x, y, text, size, font, colour, bold)
    def update(self):
        if self.room.endOverlay:
            self.delete_object(self)
        return super().update()

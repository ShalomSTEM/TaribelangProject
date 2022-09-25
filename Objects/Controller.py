from GameFrame import Globals, RoomObject, EnumLevels, TextObject
import os
import pygame

class OverlayButtons():
    A = "Button-Red.svg"
    B = "Button-Yellow.svg"
    X = "Button-Blue.svg"
    Y = "Button-Green.svg"
    Start = "Start_Select_Button.png"
    Select = "Start_Select_Button.png"
    LB = "L_Bumper_Button.png"
    RB = "R_Bumper_Button.png"
    DpadU = "dpad_U.svg"
    DpadD = "dpad_D.svg"
    DpadL = "dpad_L.svg"
    DpadR = "dpad_R.svg"
class Controller1(RoomObject):
    def __init__(self, room, x, y, buttons):
        RoomObject.__init__(self, room, x, y)
        Globals.oldRoom = self.room.roomNum
        self.set_image(self.load_image("listener.png"), 1, 1)
        Globals.next_level = EnumLevels.ControllerOverlay
        Globals.OverlayButtons = buttons
        self.room.running = False
class Controller2(RoomObject):
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)
        self.set_image(self.load_image(os.path.join("Overlays", "Controller_b.png")), 1280, 720)
        self.handle_key_events = True
        self.mylist = Globals.OverlayButtons.split(" ")
        countMethod = self.mylist.__len__()
        self.leftCount = countMethod.real
        self.leftSpacing = 0
        localIndex = 1
        if self.mylist.count("RB") == 1: 
            self.leftCount -= 1
            self.room.add_room_object(ButtonOverlay(self.room, 1200, 60*localIndex, "RB"))
            localIndex += 1
            self.mylist.remove("RB")
        if self.mylist.count("LB") == 1: 
            self.leftCount -= 1
            self.room.add_room_object(ButtonOverlay(self.room, 1200, 60*localIndex, "LB"))
            localIndex += 1
            self.mylist.remove("LB")
        if self.mylist.count("START") == 1: 
            self.leftCount -= 1
            self.room.add_room_object(ButtonOverlay(self.room, 1200, 60*localIndex, "START"))
            localIndex += 1
            self.mylist.remove("START")
        if self.mylist.count("SELECT") == 1: 
            self.leftCount -= 1
            self.room.add_room_object(ButtonOverlay(self.room, 1200, 60*localIndex, "SELECT"))
            localIndex += 1
            self.mylist.remove("SELECT")
        self.leftSpacing = 660 / self.leftCount
        for i in range(self.leftCount):
            self.room.add_room_object(ButtonOverlay(self.room, 20, self.leftSpacing*i, self.mylist[i]))
        # # Press A to Continue! text
        self.room.add_room_object(ButtonText(self.room, 460, 620, ' ', 40, "Comic Sans MS", (255, 0, 255), False, True))

    def key_pressed(self, key):
        if key[pygame.K_a]:
            self.room.complete() 
class ButtonOverlay(RoomObject):
    def __init__(self, room, x, y, button):
        RoomObject.__init__(self, room, x, y)
        if button == 'LEFT':
            self.set_image(self.load_image(os.path.join("Overlays", OverlayButtons.DpadL)), 64, 64)
            self.room.add_room_object(ButtonText(self.room, self.x+80, self.y, '- Left', 40, "Comic Sans MS", (255, 0, 255), False, False))
        if button == 'RIGHT':
            self.set_image(self.load_image(os.path.join("Overlays", OverlayButtons.DpadR)), 64, 64)
            self.room.add_room_object(ButtonText(self.room, self.x+80, self.y, '- Right', 40, "Comic Sans MS", (255, 0, 255), False, False))
        if button == 'UP':
            self.set_image(self.load_image(os.path.join("Overlays", OverlayButtons.DpadU)), 64, 64)  
            self.room.add_room_object(ButtonText(self.room, self.x+80, self.y, '- Up', 40, "Comic Sans MS", (255, 0, 255), False, False))
        if button == 'DOWN':
            self.set_image(self.load_image(os.path.join("Overlays", OverlayButtons.DpadD)), 64, 64)
            self.room.add_room_object(ButtonText(self.room, self.x+80, self.y, '- Down', 40, "Comic Sans MS", (255, 0, 255), False, False))
        if button == 'A':
            self.set_image(self.load_image(os.path.join("Overlays", OverlayButtons.A)), 64, 64)    
            self.room.add_room_object(ButtonText(self.room, self.x+80, self.y, '- A', 40, "Comic Sans MS", (255, 0, 255), False, False))  
        if button == 'B':
            self.set_image(self.load_image(os.path.join("Overlays", OverlayButtons.B)), 64, 64)
            self.room.add_room_object(ButtonText(self.room, self.x+80, self.y, '- B', 40, "Comic Sans MS", (255, 0, 255), False, False))
        if button == 'X':
            self.set_image(self.load_image(os.path.join("Overlays", OverlayButtons.X)), 64, 64)     
            self.room.add_room_object(ButtonText(self.room, self.x+80, self.y, '- X', 40, "Comic Sans MS", (255, 0, 255), False, False))  
        if button == 'Y':
            self.set_image(self.load_image(os.path.join("Overlays", OverlayButtons.Y)), 64, 64)
            self.room.add_room_object(ButtonText(self.room, self.x+80, self.y, '- Y', 40, "Comic Sans MS", (255, 0, 255), False, False))
        if button == 'LB':
            self.set_image(self.load_image(os.path.join("Overlays", OverlayButtons.LB)), 64, 64)       
            self.room.add_room_object(ButtonText(self.room, self.x-265, self.y, 'Left Bumper', 40, "Comic Sans MS", (255, 0, 255), False, False))
            self.room.add_room_object(ButtonText(self.room, self.x-20, self.y, '-', 40, "Comic Sans MS", (255, 0, 255), False, False))
        if button == 'RB':
            self.set_image(self.load_image(os.path.join("Overlays", OverlayButtons.RB)), 64, 64)
            self.room.add_room_object(ButtonText(self.room, self.x-280, self.y, 'Right Bumper', 40, "Comic Sans MS", (255, 0, 255), False, False))
            self.room.add_room_object(ButtonText(self.room, self.x-20, self.y, '-', 40, "Comic Sans MS", (255, 0, 255), False, False))
        if button == 'START':
            self.set_image(self.load_image(os.path.join("Overlays", OverlayButtons.Select)), 64, 64)
            self.room.add_room_object(ButtonText(self.room, self.x-160, self.y, 'Select', 40, "Comic Sans MS", (255, 0, 255), False, False))
            self.room.add_room_object(ButtonText(self.room, self.x-20, self.y, '-', 40, "Comic Sans MS", (255, 0, 255), False, False))
        if button == 'SELECT':
            self.set_image(self.load_image(os.path.join("Overlays", OverlayButtons.Select)), 64, 64)
            self.room.add_room_object(ButtonText(self.room, self.x-160, self.y, 'Select', 40, "Comic Sans MS", (255, 0, 255), False, False))
            self.room.add_room_object(ButtonText(self.room, self.x-20, self.y, '-', 40, "Comic Sans MS", (255, 0, 255), False, False))
class ButtonText(TextObject):
    def __init__(self, room, x, y, text, size, font, colour, bold, ContinueText):
        TextObject.__init__(self, room, x, y, text, size, font, colour, bold)
        if ContinueText:
            self.text = 'Press A to Continue!'
            self.set_timer(80, self.update_text)

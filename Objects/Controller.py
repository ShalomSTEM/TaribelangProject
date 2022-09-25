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
        self.mylist = Globals.OverlayButtons.split(" ")
        self.handle_key_events = True
        if "a" in self.mylist: self.room.add_room_object(A_ButtonOverlay(self.room, 20, 20))
        if "b" in self.mylist: self.room.add_room_object(B_ButtonOverlay(self.room, 20, 100))
        if "x" in self.mylist: self.room.add_room_object(X_ButtonOverlay(self.room, 20, 180))
        if "y" in self.mylist: self.room.add_room_object(Y_ButtonOverlay(self.room, 20, 260))
        if "rb" in self.mylist: self.room.add_room_object(R_BumperOverlay(self.room, 1200, 20))
        if "lb" in self.mylist: self.room.add_room_object(L_BumperOverlay(self.room, 1200, 100))
        if "left" in self.mylist: self.room.add_room_object(L_DpadOverlay(self.room, 20, 340))
        if "right" in self.mylist: self.room.add_room_object(R_DpadOverlay(self.room, 20, 420))
        if "up" in self.mylist: self.room.add_room_object(U_DpadOverlay(self.room, 20, 500))
        if "down" in self.mylist: self.room.add_room_object(D_DpadOverlay(self.room, 20, 580))
        if "start" in self.mylist: self.room.add_room_object(Select_ButtonOverlay(self.room, 1200, 180))
        if "select" in self.mylist: self.room.add_room_object(Start_ButtonOverlay(self.room, 1200, 260))
        # Press A to Continue! text \/
        self.room.add_room_object(ButtonText(self.room, 460, 620, ' ', 40, "Comic Sans MS", (255, 0, 255), False, True))

    def key_pressed(self, key):
        if key[pygame.K_a]:
            self.room.complete() 
class L_DpadOverlay(RoomObject):
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)
        self.set_image(self.load_image(os.path.join("Overlays", OverlayButtons.DpadL)), 64, 64)
        self.room.add_room_object(ButtonText(self.room, self.x+80, self.y, '- Left', 40, "Comic Sans MS", (255, 0, 255), False, False))
class R_DpadOverlay(RoomObject):
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)
        self.set_image(self.load_image(os.path.join("Overlays", OverlayButtons.DpadR)), 64, 64)
        self.room.add_room_object(ButtonText(self.room, self.x+80, self.y, '- Right', 40, "Comic Sans MS", (255, 0, 255), False, False))
class D_DpadOverlay(RoomObject):
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)
        self.set_image(self.load_image(os.path.join("Overlays", OverlayButtons.DpadD)), 64, 64)
        self.room.add_room_object(ButtonText(self.room, self.x+80, self.y, '- Down', 40, "Comic Sans MS", (255, 0, 255), False, False))
class U_DpadOverlay(RoomObject):
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)
        self.set_image(self.load_image(os.path.join("Overlays", OverlayButtons.DpadU)), 64, 64)  
        self.room.add_room_object(ButtonText(self.room, self.x+80, self.y, '- Up', 40, "Comic Sans MS", (255, 0, 255), False, False))
class A_ButtonOverlay(RoomObject):
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)
        self.set_image(self.load_image(os.path.join("Overlays", OverlayButtons.A)), 64, 64)    
        self.room.add_room_object(ButtonText(self.room, self.x+80, self.y, '- A', 40, "Comic Sans MS", (255, 0, 255), False, False))   
class B_ButtonOverlay(RoomObject):
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)
        self.set_image(self.load_image(os.path.join("Overlays", OverlayButtons.B)), 64, 64)
        self.room.add_room_object(ButtonText(self.room, self.x+80, self.y, '- B', 40, "Comic Sans MS", (255, 0, 255), False, False))
class X_ButtonOverlay(RoomObject):
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)
        self.set_image(self.load_image(os.path.join("Overlays", OverlayButtons.X)), 64, 64)     
        self.room.add_room_object(ButtonText(self.room, self.x+80, self.y, '- X', 40, "Comic Sans MS", (255, 0, 255), False, False))  
class Y_ButtonOverlay(RoomObject):
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)
        self.set_image(self.load_image(os.path.join("Overlays", OverlayButtons.Y)), 64, 64)
        self.room.add_room_object(ButtonText(self.room, self.x+80, self.y, '- Y', 40, "Comic Sans MS", (255, 0, 255), False, False))
class Start_ButtonOverlay(RoomObject):
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)
        self.set_image(self.load_image(os.path.join("Overlays", OverlayButtons.Start)), 64, 64)     
        self.room.add_room_object(ButtonText(self.room, self.x-140, self.y, 'Start', 40, "Comic Sans MS", (255, 0, 255), False, False))  
        self.room.add_room_object(ButtonText(self.room, self.x-20, self.y, '-', 40, "Comic Sans MS", (255, 0, 255), False, False))
class Select_ButtonOverlay(RoomObject):
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)
        self.set_image(self.load_image(os.path.join("Overlays", OverlayButtons.Select)), 64, 64)
        self.room.add_room_object(ButtonText(self.room, self.x-160, self.y, 'Select', 40, "Comic Sans MS", (255, 0, 255), False, False))
        self.room.add_room_object(ButtonText(self.room, self.x-20, self.y, '-', 40, "Comic Sans MS", (255, 0, 255), False, False))
class L_BumperOverlay(RoomObject):
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)
        self.set_image(self.load_image(os.path.join("Overlays", OverlayButtons.LB)), 64, 64)       
        self.room.add_room_object(ButtonText(self.room, self.x-265, self.y, 'Left Bumper', 40, "Comic Sans MS", (255, 0, 255), False, False))
        self.room.add_room_object(ButtonText(self.room, self.x-20, self.y, '-', 40, "Comic Sans MS", (255, 0, 255), False, False))
class R_BumperOverlay(RoomObject):
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)
        self.set_image(self.load_image(os.path.join("Overlays", OverlayButtons.RB)), 64, 64)
        self.room.add_room_object(ButtonText(self.room, self.x-280, self.y, 'Right Bumper', 40, "Comic Sans MS", (255, 0, 255), False, False))
        self.room.add_room_object(ButtonText(self.room, self.x-20, self.y, '-', 40, "Comic Sans MS", (255, 0, 255), False, False))
class ButtonText(TextObject):
    def __init__(self, room, x, y, text, size, font, colour, bold, ContinueText):
        TextObject.__init__(self, room, x, y, text, size, font, colour, bold)
        if ContinueText:
            self.text = 'Press A to Continue!'
            self.set_timer(80, self.update_text)

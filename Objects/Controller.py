from GameFrame import Globals, RoomObject, EnumLevels, TextObject
import os
import pygame
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
        self.handle_key_events = True\

        # Split the strings and get a count of them
        self.mylist = Globals.OverlayButtons.split(" ")
        countMethod = self.mylist.__len__()
        self.leftCount = countMethod.real

        # Set up the variables
        self.leftSpacing = 0
        self.rightCount = 0
        self.rightList = []
        self.rightSpacing = 0
        self.rightTextSpacing = []

        # Seperate the left side from the right side
        if self.mylist.count("RB") == 1: 
            self.leftCount -= 1
            self.rightCount += 1
            self.rightList.append('Right Bumper')
            self.rightTextSpacing.append(280)
            self.mylist.remove("RB")
        if self.mylist.count("LB") == 1: 
            self.leftCount -= 1
            self.rightCount += 1
            self.rightList.append('Left Bumper')
            self.rightTextSpacing.append(265)
            self.mylist.remove("LB")
        if self.mylist.count("Start") == 1: 
            self.leftCount -= 1
            self.rightCount += 1
            self.rightList.append('Start')
            self.rightTextSpacing.append(160)
            self.mylist.remove("Start")
        if self.mylist.count("Select") == 1: 
            self.leftCount -= 1
            self.rightCount += 1
            self.rightList.append('Select')
            self.rightTextSpacing.append(160)
            self.mylist.remove("Select")

        # Make sure division by 0 isn't tried
        if self.leftCount != 0: self.leftSpacing = 660 / self.leftCount
        if self.rightCount != 0: self.rightSpacing = 330 / self.rightCount

        # Loop that creates the buttons on both sides
        for i in range(self.leftCount):
            self.room.add_room_object(ButtonOverlay(self.room, 20, self.leftSpacing*i, self.mylist[i], False, 0))
        for i in range(self.rightCount):
            self.room.add_room_object(ButtonOverlay(self.room, 1200, self.leftSpacing*i, self.rightList[i], True, self.rightTextSpacing[i]))

        # Press A to Continue! text
        self.room.add_room_object(ButtonText(self.room, 460, 620, ' ', 40, "Comic Sans MS", (255, 0, 255), False, True))

    def key_pressed(self, key):
        if key[pygame.K_a]:
            self.room.complete() 
class ButtonOverlay(RoomObject):
    def __init__(self, room, x, y, button, right, rightTextSpacing):
        RoomObject.__init__(self, room, x, y)
        if right:
            self.set_image(self.load_image(os.path.join("Overlays", f'{button}.png')), 64, 64)
            self.room.add_room_object(ButtonText(self.room, self.x-rightTextSpacing, self.y, button, 40, "Comic Sans MS", (255, 0, 255), False, False))
            self.room.add_room_object(ButtonText(self.room, self.x-20, self.y, '-', 40, "Comic Sans MS", (255, 0, 255), False, False))
        else:
            self.set_image(self.load_image(os.path.join("Overlays", f'{button}.svg')), 64, 64)
            self.room.add_room_object(ButtonText(self.room, self.x+80, self.y, f'- {button}', 40, "Comic Sans MS", (255, 0, 255), False, False))
class ButtonText(TextObject):
    def __init__(self, room, x, y, text, size, font, colour, bold, ContinueText):
        TextObject.__init__(self, room, x, y, text, size, font, colour, bold)
        if ContinueText:
            self.text = 'Press A to Continue!'
            self.set_timer(80, self.update_text)

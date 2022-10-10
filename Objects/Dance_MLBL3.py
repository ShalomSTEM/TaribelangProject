import os
import pygame
from random import randrange
from GameFrame import RoomObject, Globals, TextObject
import datetime
class Dance_MLBL3(RoomObject):
    def __init__(self, room, x, y, arrow):
        RoomObject.__init__(self, room, x, y)
        self.handle_key_events = True
        self.room.Dance = True
        # X values for all of the different types of arrows
        self.distance = [20, 148, 276, 404]
        
        # Arrow images
        self.arrows = ["leftArrow.png", "downArrow.png", "upArrow.png", "rightArrow.png"]
        
        # Setting image
        self.set_image(self.load_image(os.path.join("Overlays", self.arrows[arrow])), 128, 128)
        
        # Make sure new arrows are created, but preventing overlap at the same time
        if arrow == 0:
            self.set_timer(80, self.createNewArrows)
        
    def update(self):
        self.y_speed = self.y_speed + self.gravity
        self.x += self.x_speed
        self.y += self.y_speed
        self.rect.x = self.x
        self.rect.y = self.y
        if self.room.danceEnd:
            self.room.delete_object(self)
    def createNewArrows(self):
        rand = randrange(0, 4, 1)
        newArrow = DanceArrows_MLBL3(self.room, self.distance[rand], 600, rand)
        self.room.add_room_object(newArrow)
        self.math = 4*(self.room.y_speed*-1)
        self.set_timer(80-(self.math), self.createNewArrows)
        
class DanceArrows_MLBL3(RoomObject):
    def __init__(self, room, x, y, arrow):
        RoomObject.__init__(self, room, x, y)
        self.handle_key_events = True
        self.can_press = False
        self.arrowType = arrow
        
        # An array for point cards
        self.pointCards = []
        
        # All of the different points
        self.onTargetGood = False
        self.onTargetPerfect = False
        self.onTargetAmazing = False
        self.notOnTarget = False

        # Arrow names, points and PNGs in arrays
        self.arrowNames = ["left", "down", "up", "right"]
        self.pointValues = [2, 1, 0.75, -1]
        self.arrows = ["leftArrowFilled.png", "downArrowFilled.png", "upArrowFilled.png", "rightArrowFilled.png"]
        self.danceSprites = ["Player_dance1.png", 'Player_dance2.png', 'Player_dance3.png', 'Player_dance4.png']

        # Setting image and collision
        self.set_image(self.load_image(os.path.join("Overlays", self.arrows[arrow])), 128, 128)
        self.register_collision_object('Dance_MLBL3')
        
        # Enabling pressing keys
        self.set_timer(10, self.reset_press)
        
    def update(self):
        self.y_speed = self.room.y_speed
        self.y_speed = self.y_speed + self.gravity
        self.x += self.x_speed
        self.y += self.y_speed
        self.rect.x = self.x
        self.rect.y = self.y
        if self.y < -128:
            self.room.delete_object(self)
        if self.room.danceEnd:
            self.delete_object(self)
    
    def handle_collision(self,other, other_type):
        if other_type == 'Dance_MLBL3':
            if self.y == 0:
                self.onTargetPerfect = True
            elif self.y >=  -15 and self.y <= 15 and not self.y == 0:
               self.onTargetAmazing = True
            elif self.y >= -20 and not self.y >= -15 and not self.y == 0 and self.y <= 30:
                self.onTargetGood = True
            else:
                self.notOnTarget = True
                
    def key_pressed(self, key): 
        if self.can_press:
            if key[pygame.K_UP]:
                self.key_signal("up")
                self.pause_press()
            elif key[pygame.K_RIGHT]:
                self.key_signal("right")
                self.pause_press()
            elif key[pygame.K_LEFT]:
                self.key_signal("left")
                self.pause_press()
            elif key[pygame.K_DOWN]:
                self.key_signal("down")
                self.pause_press()
            elif key[pygame.K_1]:
                self.key_signal("perfect")
                self.pause_press()
            elif key[pygame.K_2]:
                self.key_signal("amazing")
                self.pause_press()
            elif key[pygame.K_3]:
                self.key_signal("good")
                self.pause_press()
    def joy_pad_signal(self, p1_buttons, p2_buttons):
        if self.can_press:
            if p1_buttons[11] < -0.5:
                self.key_signal("left")
                self.pause_press()
            elif p1_buttons[11] > 0.5:
                self.key_signal("right")
                self.pause_press()
            elif p1_buttons[10] < -0.5:
                self.key_signal("up")
                self.pause_press()
            elif p1_buttons[10] > 0.5:
                self.key_signal("down")
                self.pause_press()
    
    def key_signal(self, button):
        if button == self.arrowNames[self.arrowType]:
            if self.onTargetPerfect:
                self.newPoints(0, 'PERFECT')
            elif self.onTargetGood:
                self.newPoints(2, 'GOOD')
            elif self.onTargetAmazing:
                self.newPoints(1, 'AMAZING')
            # elif not self.notOnTarget:
            #     self.newPoints(3, 'BAD')
        if button == "amazing":
            self.newPoints(1, 'AMAZING')
        if button == "perfect":
            self.newPoints(0, 'PERFECT')
        if button == "good":
            self.newPoints(2, 'GOOD')

    def newPoints(self, typeInt, typeString):
        for i in self.room.CObj:
            i.updatePos(i.pos-1)
        newCard = scoreCards_MLBL3(self.room, 1100, 630, typeInt, 7, self)
        self.room.CObj.append(newCard)
        self.room.player.set_image(os.path.join("Images", "MilbiL2", self.danceSprites[self.arrowType]), 50, 50)
        self.room.y_speed -= 0.25
        self.room.points = round((self.room.points + (self.pointValues[typeInt]*(self.room.y_speed*-1))), 1)
        self.room.add_room_object(newCard)
        self.room.delete_object(self)
        
    def pause_press(self):
        self.can_press = False
        self.set_timer(5, self.reset_press)

    def reset_press(self):
        self.can_press = True
class scoreText_MLBL3(TextObject):
    def __init__(self, room, x, y, text, size, font, colour, bold, score, timer, speed):
        TextObject.__init__(self, room, x, y, text, size, font, colour, bold)
        self.ran = False
        self.score = score
        self.timer = timer
        self.speed = speed
        self.index = 10
        if self.timer:
            self.time = datetime.datetime.now() + datetime.timedelta(seconds=self.index)
            self.updTimer()
    def updTimer(self):
        self.index -= 1
        now = datetime.datetime.now()
        self.text = f'Time: {int(self.time.timestamp() - now.timestamp())}s'
        self.set_timer(30, self.updTimer)
        self.update_text()
        if self.text == 'Time: 0s':
            self.room.danceEnd = True
            self.ran = False
    def update(self):
        self.y_speed = self.y_speed + self.gravity
        self.x += self.x_speed
        self.y += self.y_speed
        self.rect.x = self.x
        self.rect.y = self.y
        if self.room.danceEnd:
            self.room.delete_object(self)
        if self.score:
            self.text = f'Score: {self.room.points}'
            self.update_text()
        if self.speed:
            self.text = f'Speed: {round(self.room.y_speed, 2)*-1}'
            self.update_text()
class DanceBG_MLBL3(RoomObject):
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)
        self.set_image(self.load_image("listener.png"), 1, 1)

class scoreCards_MLBL3(RoomObject):
    def __init__(self, room, x, y, type, pos, parent):
        RoomObject.__init__(self, room, x, y)
        self.pos = pos
        self.type = type
        self.parent = parent
        if self.type == 0:
            self.set_image(self.load_image(os.path.join("MilbiL2", "perfect_card.png")), 180, 90)
        elif self.type == 1:
            self.set_image(self.load_image(os.path.join("MilbiL2", "amazing_card.png")), 180, 90)
        elif self.type == 2:
            self.set_image(self.load_image(os.path.join("MilbiL2", "good_card.png")), 180, 90)
    def updatePos(self, pos):
        if pos == -1:
            self.room.CObj.remove(self)
            self.room.delete_object(self)
        else:
            self.y = 0+(90*pos)
            self.pos = pos
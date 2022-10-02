import os
from random import randrange

from GameFrame import RoomObject, Globals, TextObject
import pygame

class Dance_MLBL3(RoomObject):
    def __init__(self, room, x, y, arrow):
        RoomObject.__init__(self, room, x, y)
        self.handle_key_events = True
        
        # X values for all of the different types of arrows
        self.distance = [20, 148, 276, 404]
        
        # Arrow images
        self.arrows = ["leftArrow.png", "downArrow.png", "upArrow.png", "rightArrow.png"]
        
        # Setting image
        self.set_image(self.load_image(os.path.join("Overlays", self.arrows[arrow])), 128, 128)
        
        # Make sure new arrows are created, but preventing overlap at the same time
        if arrow == 0:
            self.set_timer(80, self.createNewArrows)
        
    def createNewArrows(self):
        rand = randrange(0, 3, 1)
        newArrow = DanceArrows_MLBL3(self.room, self.distance[rand], 600, rand)
        self.room.add_room_object(newArrow)
        self.set_timer(80, self.createNewArrows)
        
class DanceArrows_MLBL3(RoomObject):
    def __init__(self, room, x, y, arrow):
        RoomObject.__init__(self, room, x, y)
        self.handle_key_events = True
        self.can_press = False
        self.arrowType = arrow
        
        # All of the different points
        self.onTargetGood = False
        self.onTargetPerfect = False
        self.onTargetAmazing = False
        
        # Arrow names and PNGs in arrays
        self.arrowNames = ["left", "down", "up", "right"]
        self.arrows = ["leftArrowFilled.png", "downArrowFilled.png", "upArrowFilled.png", "rightArrowFilled.png"]
        
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
    

    def handle_collision(self,other, other_type):
        if other_type == 'Dance_MLBL3':
            if self.y == 0:
                self.onTargetPerfect = True
            elif self.y >=  -4 and self.y <= 5 and not self.y == 0:
                self.onTargetAmazing = True
            else:
                self.onTargetGood = False
                self.onTargetPerfect = False
                self.onTargetAmazing = False
                
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
    
    def key_signal(self, button):
        if button == self.arrowNames[self.arrowType]:
            if self.onTargetPerfect:
                print("PERFECT")
                self.room.y_speed -= 0.25
                self.room.points = round((self.room.points + (2*(self.room.y_speed*-1))), 1)
                self.room.delete_object(self)
            elif self.onTargetGood:
                print("GOOD")
                self.room.y_speed -= 0.25
                self.room.points = round((self.room.points + (0.75*(self.room.y_speed*-1))), 1)
                self.room.delete_object(self)
            elif self.onTargetAmazing:
                print("AMAZING")
                self.room.y_speed -= 0.25
                self.room.points = round((self.room.points + (1*(self.room.y_speed*-1))), 1)
                self.room.delete_object(self)
        

    def pause_press(self):
        self.can_press = False
        self.set_timer(5, self.reset_press)

    def reset_press(self):
        self.can_press = True

class scoreText_MLBL3(TextObject):
    def __init__(self, room, x, y, text, size, font, colour, bold, score):
        TextObject.__init__(self, room, x, y, text, size, font, colour, bold)
        self.score = score
    
    def update(self):
        self.y_speed = self.y_speed + self.gravity
        self.x += self.x_speed
        self.y += self.y_speed
        self.rect.x = self.x
        self.rect.y = self.y
        if self.score:
            self.text = f'Score: {self.room.points}'
            self.update_text()
        else:
            self.text = f'Speed: {round(self.room.y_speed, 2)*-1}'
            self.update_text()
class DanceBG_MLBL3(RoomObject):
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)
        self.set_image(self.load_image("listener.png"), 1, 1)
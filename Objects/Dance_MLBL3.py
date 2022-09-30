import os

from GameFrame import RoomObject, Globals, TextObject
import pygame

class Dance_MLBL3(RoomObject):
    def __init__(self, room, x, y, arrow):
        RoomObject.__init__(self, room, x, y)
        self.arrows = ["leftArrow.png", "downArrow.png", "upArrow.png", "rightArrow.png"]
        self.handle_key_events = True
        self.set_image(self.load_image(os.path.join("Overlays", self.arrows[arrow])), 64, 64)
        
class DanceArrows_MLBL3(RoomObject):
    def __init__(self, room, x, y, arrow):
        RoomObject.__init__(self, room, x, y)
        self.handle_key_events = True
        self.can_press = False
        # All of the different points
        self.arrowType = ''

        self.onTargetGood = False
        self.onTargetPerfect = False
        self.onTargetAmazing = False
        self.arrows = ["leftArrowFilled.png", "downArrowFilled.png", "upArrowFilled.png", "rightArrowFilled.png"]
        self.set_image(self.load_image(os.path.join("Overlays", self.arrows[arrow])), 64, 64)
        print(arrow)
        if arrow == 0:
            self.arrowType = 'left'
        elif arrow == 1: 
            self.arrowType = 'down'
        elif arrow == 2: 
            self.arrowType = 'up'
        elif arrow == 3: 
            self.arrowType = 'right'
        self.register_collision_object('Dance_MLBL3')
        self.set_timer(10, self.reset_press)
        
    def update(self):
        self.y_speed = self.room.y_speed
        self.y_speed = self.y_speed + self.gravity
        self.x += self.x_speed
        self.y += self.y_speed
        self.rect.x = self.x
        self.rect.y = self.y
        if self.y < 95:
            self.room.delete_object(self)
    
    def handle_collision(self,other, other_type):
        if other_type == 'Dance_MLBL3':
            if self.y == 100:
                self.onTargetPerfect = True
            elif self.y >=  96 and self.y <= 105 and not self.y == 100:
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
        if button == self.arrowType:
            if self.onTargetPerfect:
                print("PERFECT")
                self.room.points = round((self.room.points + (2*(self.room.y_speed*-1))), 1)
                self.room.delete_object(self)
            elif self.onTargetGood:
                print("GOOD")
                self.room.points = round((self.room.points + (0.75*(self.room.y_speed*-1))), 1)
                self.room.delete_object(self)
            elif self.onTargetAmazing:
                print("AMAZING")
                self.room.points = round((self.room.points + (1*(self.room.y_speed*-1))), 1)
                self.room.delete_object(self)
        

    def pause_press(self):
        self.can_press = False
        self.set_timer(5, self.reset_press)

    def reset_press(self):
        self.can_press = True

class scoreText_MLBL3(TextObject):
    def __init__(self, room, x, y, text, size, font, colour, bold):
        TextObject.__init__(self, room, x, y, text, size, font, colour, bold)
    
    def update(self):
        self.y_speed = self.y_speed + self.gravity
        self.x += self.x_speed
        self.y += self.y_speed
        self.rect.x = self.x
        self.rect.y = self.y
        self.text = f'Score: {self.room.points}'
        self.update_text()

class DanceBG_MLBL3(RoomObject):
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)
        self.set_image(self.load_image(os.path.join("Overlays", "DanceBG.png")), 274, 70)
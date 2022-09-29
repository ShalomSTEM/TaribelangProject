import os

from GameFrame import RoomObject, Globals
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
        self.onTarget = False
        self.arrows = ["leftArrowFilled.png", "downArrowFilled.png", "upArrowFilled.png", "rightArrowFilled.png"]
        self.set_image(self.load_image(os.path.join("Overlays", self.arrows[arrow])), 64, 64)
        self.register_collision_object('Dance_MLBL3')
        self.y_speed = -1
        self.set_timer(10, self.reset_press)
        
    def update(self):
        self.y_speed = self.y_speed + self.gravity
        self.x += self.x_speed
        self.y += self.y_speed
        self.rect.x = self.x
        self.rect.y = self.y
        if self.y < 290:
            self.room.delete_object(self)
    
    def handle_collision(self,other, other_type):
        if other_type == 'Dance_MLBL3':
            if self.y == 300:
                self.onTarget = True
            else:
                self.onTarget = False
                
    def key_pressed(self, key):
        if self.can_press:
            if key[pygame.K_UP]:
                    self.key_signal("up")
                    self.pause_press()
    
    def key_signal(self, button):
        if button == "up":
            if self.onTarget:
                    print("SUCCESS")
    
    def pause_press(self):
        self.can_press = False
        self.set_timer(10, self.reset_press)

    def reset_press(self):
        self.can_press = True

        

class DanceBG_MLBL3(RoomObject):
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)
        self.set_image(self.load_image(os.path.join("Overlays", "DanceBG.png")), 274, 70)
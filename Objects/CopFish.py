from GameFrame import RoomObject
import os


class CopFish(RoomObject):
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)

        #self.roll_over_set = False
        self.standard_image = self.load_image(os.path.join('CopG3', 'CopFish.png'))
        self.set_image(self.standard_image, 65, 36)

        #self.depth = 100

        #self.x_speed = 0
        #self.y_speed = -4

        #self.handle_mouse_events = True


    #def step(self):
        #if self.rect.bottom >= Globals.SCREEN_HEIGHT or self.y <= 56:
            #self.y_speed *= -1

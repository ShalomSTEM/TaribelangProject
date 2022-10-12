import os
from GameFrame import RoomObject, Globals


class CopG1_kangaroo(RoomObject):
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)

        self.image1 = self.load_image(os.path.join("CoppleL1",'kanga1.png' ))
        self.image2 = self.load_image(os.path.join("CoppleL1", "kanga2.png"))
        self.set_image(self.image1, 64, 64)
        self.curr_img = 1
        self.set_timer(10, self.update_image)

        self.depth = 100

        self.y_speed = -1

        self.can_collide = True

        self.register_collision_object('CopG1_Tree')

    def handle_collision(self, other, other_type):
        if self.can_collide:
            self.can_collide = False
            self.set_timer(60, self.reset_collide)
            self.y_speed += 1

    def reset_collide(self):
        self.can_collide = True

    def update_image(self):
        self.curr_img += 1
        if self.curr_img > 1:
            self.curr_img = 0
        if self.curr_img == 0:
            self.set_image(self.image1, 64, 64)
        elif self.curr_img == 1:
            self.set_image(self.image2, 64, 64)

        if self.y > Globals.SCREEN_HEIGHT:
            self.delete_object(self)
        else:
            self.set_timer(5, self.update_image)

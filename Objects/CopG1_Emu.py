import os
from GameFrame import RoomObject, Globals

class CopG1_Emu(RoomObject):
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)

        self.image = self.load_image(os.path.join('CoppleL1', 'kanga1.png'))
        self.image2 = self.load_image(os.path.join('CoppleL1', 'kanga1.png'))
        self.set_image(self.image, 64, 64)

        self.depth = 100

        self.y_speed = -0.5

        self.register_collision_object("CopG1_Tree")

    def handle_collision(self, other, other_type):
        if other_type == "CopG1_Tree":
            self.y_speed *= -2
            self.y = Globals.SCREEN_HEIGHT - 90
        elif other_type == 'Copple1_Player':
            self.blocked()
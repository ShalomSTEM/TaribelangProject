from GameFrame import RoomObject, Globals
import random, os


class BossMLBL3(RoomObject):
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)



        boss = self.load_image(os.path.join("MilbiL3", "front_1.png"))
        self.set_image(boss, 256, 256)

        # Load player animation images
        self.down = []
        self.down.append(self.load_image(os.path.join("MilbiL3", "front_1.png")))
        self.down.append(self.load_image(os.path.join("MilbiL3", "front_2.png")))
        self.down.append(self.load_image(os.path.join("MilbiL3", "front_3.png")))
        self.down.append(self.load_image(os.path.join("MilbiL3", "front_4.png")))
        self.up = []
        self.up.append(self.load_image(os.path.join("MilbiL3", "back_1.png")))
        self.up.append(self.load_image(os.path.join("MilbiL3", "back_2.png")))
        self.up.append(self.load_image(os.path.join("MilbiL3", "back_3.png")))
        self.up.append(self.load_image(os.path.join("MilbiL3", "back_4.png")))
        self.left = []
        self.left.append(self.load_image(os.path.join("MilbiL3", "left_1.png")))
        self.left.append(self.load_image(os.path.join("MilbiL3", "left_2.png")))
        self.left.append(self.load_image(os.path.join("MilbiL3", "left_3.png")))
        self.left.append(self.load_image(os.path.join("MilbiL3", "left_4.png")))
        self.right = []
        self.right.append(self.load_image(os.path.join("MilbiL3", "right_1.png")))
        self.right.append(self.load_image(os.path.join("MilbiL3", "right_2.png")))
        self.right.append(self.load_image(os.path.join("MilbiL3", "right_3.png")))
        self.right.append(self.load_image(os.path.join("MilbiL3", "right_4.png")))

        self.img_index = 0



#        self.animate()

'''
    def animate(self):
        self.img_index += 1
        self.img_index %= 4
        if self.facing == self.LEFT:
            self.set_image(self.left[self.img_index], 16, 24)
        elif self.facing == self.RIGHT:
            self.set_image(self.right[self.img_index], 16, 24)
        elif self.facing == self.UP:
            self.set_image(self.up[self.img_index], 16, 24)
        elif self.facing == self.DOWN:
            self.set_image(self.down[self.img_index], 16, 24)
        else:
            self.set_image(self.down[0], 16, 24)

        self.set_timer(3, self.animate)

'''

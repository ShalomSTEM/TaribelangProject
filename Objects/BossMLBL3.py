from GameFrame import RoomObject, Globals
import random, os


class BossMLBL3(RoomObject):
    def __init__(self, room, x, y, player):
        RoomObject.__init__(self, room, x, y)

        self.player = player

        boss = self.load_image(os.path.join("MilbiL3", "front_1.png"))
        self.set_image(boss, 16, 24)

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

        self.LEFT = 0
        self.RIGHT = 1
        self.UP = 2
        self.DOWN = 3

        self.facing = 4



        self.move_to_player_count = 0

        self.block_right = False
        self.block_left = False
        self.block_up = False
        self.block_down = False

        self.moving = False
        self.animate()

    def move(self):
        self.move_to_player_count += 1
        if self.move_to_player_count == 3 or \
                abs(self.player.x - self.x) > 400 or \
                abs(self.player.y - self.y) > 400:
            self.move_towards_player()
            self.move_to_player_count = 0
        else:
            randomwalk = random.randint(0, 3)
            if randomwalk == self.LEFT:
                self.move_left()
            elif randomwalk == self.RIGHT:
                self.move_right()
            elif randomwalk == self.UP:
                self.move_up()
            elif randomwalk == self.DOWN:
                self.move_down()
        self.set_timer(10, self.move)


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

    def move_right(self):
        self.facing = self.RIGHT
        self.x_speed += Globals.NPCmove_speed


    def move_left(self):
        self.facing = self.LEFT
        self.x_speed -= Globals.NPCmove_speed


    def move_up(self):
        self.facing = self.UP
        self.y_speed -= Globals.NPCmove_speed


    def move_down(self):
        self.facing = self.DOWN
        self.y_speed += Globals.NPCmove_speed


    def stop(self):
        self.facing = 4
        self.x_speed = 0
        self.y_speed = 0



    def attacks(self):
        self.set_timer(60)

    def move_towards_player(self):
        x = self.player.x - self.x
        y = self.player.y - self.y
        if abs(x) < abs(y):
            if y > 0:
                self.move_down()
            else:
                self.move_up()
        else:
            if x > 0:
                self.move_right()
            else:
                self.move_left()



import pygame, os
from GameFrame import RoomObject, Globals


class Splayer(RoomObject):
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)

        self.down = []
        self.down.append(self.load_image(os.path.join('Museum', 'front_1.png')))
        self.down.append(self.load_image(os.path.join('Museum', 'front_2.png')))
        self.down.append(self.load_image(os.path.join('Museum', 'front_3.png')))
        self.down.append(self.load_image(os.path.join('Museum', 'front_4.png')))
        self.up = []
        self.up.append(self.load_image(os.path.join('Museum', 'back_1.png')))
        self.up.append(self.load_image(os.path.join('Museum', 'back_2.png')))
        self.up.append(self.load_image(os.path.join('Museum', 'back_3.png')))
        self.up.append(self.load_image(os.path.join('Museum', 'back_4.png')))
        self.left = []
        self.left.append(self.load_image(os.path.join('Museum', 'left_1.png')))
        self.left.append(self.load_image(os.path.join('Museum', 'left_2.png')))
        self.left.append(self.load_image(os.path.join('Museum', 'left_3.png')))
        self.left.append(self.load_image(os.path.join('Museum', 'left_4.png')))
        self.right = []
        self.right.append(self.load_image(os.path.join('Museum', 'right_1.png')))
        self.right.append(self.load_image(os.path.join('Museum', 'right_2.png')))
        self.right.append(self.load_image(os.path.join('Museum', 'right_3.png')))
        self.right.append(self.load_image(os.path.join('Museum', 'right_4.png')))

        self.img_index = 0

        self.set_image(self.down[0], 64, 64)

        self.LEFT = 0
        self.RIGHT = 1
        self.UP = 2
        self.DOWN = 3

        self.facing = 4

        self.move_speed = 6

        self.handle_key_events = True


        self.playerUp = self.load_image(os.path.join('Museum', 'Splayer.png'))
        self.playerDown = self.load_image(os.path.join('Museum', 'Splayer.png'))
        self.playerLeft = self.load_image(os.path.join('Museum', 'Splayer.png'))
        self.playerRight = self.load_image(os.path.join('Museum', 'Splayer.png'))
        self.set_image(self.playerDown, 32, 32)

        self.depth = 5

        self.handle_key_events = True

        # -- Register the objects with which -- #

        # -- this object handles collisions  -- #
        self.register_collision_object('MBlock')
        self.register_collision_object('MBlockDoor')

        self.animate()

    def prestep(self):
        self.facing = 4


    def handle_collision(self, other, other_type):
        if other_type == 'MBlock':
            self.blocked()
        elif other_type == "MBlockDoor":
            self.room.complete()

    def key_pressed(self, key):

        if key[pygame.K_LEFT]:
            self.move_left()
        if key[pygame.K_RIGHT]:
            self.move_right()
        if key[pygame.K_UP]:
            self.move_up()
        if key[pygame.K_DOWN]:
            self.move_down()

    def joy_pad_signal(self, p1_buttons, p2_buttons):
        if p1_buttons[11] < -0.5:
            self.move_left()
        elif p1_buttons[11] > 0.5:
            self.move_right()
        if p1_buttons[10] < - 0.5:
            self.move_up()
        elif p1_buttons[10] > 0.5:
            self.move_down()

    def move_right(self):
        self.x += self.move_speed
        self.facing = self.RIGHT

    def move_left(self):
        self.x -= self.move_speed
        self.facing = self.LEFT

    def move_up(self):
        self.y -= self.move_speed
        self.facing = self.UP

    def move_down(self):
        self.y += Globals.move_speed
        self.facing = self.DOWN

    def animate(self):
        self.img_index += 1
        self.img_index %= 4
        if self.facing == self.LEFT:
            self.set_image(self.left[self.img_index], 50, 64)
        elif self.facing == self.RIGHT:
            self.set_image(self.right[self.img_index], 50, 64)
        elif self.facing == self.UP:
            self.set_image(self.up[self.img_index], 60, 64)
        elif self.facing == self.DOWN:
            self.set_image(self.down[self.img_index], 60, 64)
        else:
            self.set_image(self.down[0], 64, 64)

        self.set_timer(3, self.animate)


        if key[pygame.K_LEFT]:
            self.set_image(self.playerLeft, 32, 32)
            self.x -= 4
        elif key[pygame.K_RIGHT]:
            self.set_image(self.playerRight, 32, 32)
            self.x += 4
        elif key[pygame.K_UP]:
            self.set_image(self.playerUp, 32, 32)
            self.y -= 4
        elif key[pygame.K_DOWN]:
            self.set_image(self.playerDown, 32, 32)
            self.y += 4

    def joy_pad_signal(self, p1_buttons, p2_buttons):
        if p1_buttons[11] < -0.5:
            self.set_image(self.playerLeft, 32, 32)
            self.x -= 4
        if p1_buttons[11] > 0.5:
            self.set_image(self.playerRight, 32, 32)
            self.x += 4
        if p1_buttons[10] < -0.5:
            self.set_image(self.playerUp, 32, 32)
            self.y -= 4
        if p1_buttons[10] > 0.5:
            self.set_image(self.playerDown, 32, 32)
            self.y += 4


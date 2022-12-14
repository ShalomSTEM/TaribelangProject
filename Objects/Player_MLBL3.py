import pygame
from GameFrame import RoomObject, Globals
import os
from Objects.SpearProjectile import SpearProjectile


class Player_MLBL3(RoomObject):
    def __init__(self, room, x, y, size, boss_milbi):
        RoomObject.__init__(self, room, x, y)

        self.size = size

        self.boss_milbi = boss_milbi

        self.down = []
        self.down.append(self.load_image(os.path.join("CopG2", "front_1.png")))
        self.down.append(self.load_image(os.path.join("CopG2", "front_2.png")))
        self.down.append(self.load_image(os.path.join("CopG2", "front_3.png")))
        self.down.append(self.load_image(os.path.join("CopG2", "front_4.png")))

        self.up = []
        self.up.append(self.load_image(os.path.join("CopG2", "back_1.png")))
        self.up.append(self.load_image(os.path.join("CopG2", "back_2.png")))
        self.up.append(self.load_image(os.path.join("CopG2", "back_3.png")))
        self.up.append(self.load_image(os.path.join("CopG2", "back_4.png")))

        self.left = []
        self.left.append(self.load_image(os.path.join("CopG2", "left_1.png")))
        self.left.append(self.load_image(os.path.join("CopG2", "left_2.png")))
        self.left.append(self.load_image(os.path.join("CopG2", "left_3.png")))
        self.left.append(self.load_image(os.path.join("CopG2", "left_4.png")))

        self.right = []
        self.right.append(self.load_image(os.path.join("CopG2", "right_1.png")))
        self.right.append(self.load_image(os.path.join("CopG2", "right_2.png")))
        self.right.append(self.load_image(os.path.join("CopG2", "right_3.png")))
        self.right.append(self.load_image(os.path.join("CopG2", "right_4.png")))

        self.img_index = 0

        self.LEFT = 0
        self.RIGHT = 1
        self.UP = 2
        self.DOWN = 3

        self.facing = 4

        self.handle_key_events = True

        self.register_collision_object("Stne_MLBL3")
        self.register_collision_object("Dirt_MLBL3")
        self.register_collision_object("Spear_MLBL3")

        self.can_shoot = True

        self.block_right = False
        self.block_left = False
        self.block_up = False
        self.block_down = False

        self.moving = False
        self.animate()

    def prestep(self):
        self.block_right = False
        self.block_left = False
        self.block_up = False
        self.block_down = False
        self.facing = 6

    def handle_collision(self, other, other_type):
        if other_type == "Stne_MLBL3":

            if self.collides_at(self, 4, 0, "Stne_MLBL3") and not self.block_right:
                self.block_right = True
                if self.x < 596:
                    self.x = self.prev_x
                else:
                    self.move_left()

            if self.collides_at(self, -4, 0, "Stne_MLBL3") and not self.block_left:
                self.block_left = True
                if self.x >= 206:
                    self.x = self.prev_x
                else:
                    self.move_right()

            if self.collides_at(self, 0, 4, "Stne_MLBL3"):
                self.block_down = True
                if self.y <= 446:
                    self.y = self.prev_y
                else:
                    self.move_up()

            if self.collides_at(self, 0, -4, "Stne_MLBL3") and not self.block_up:
                self.block_up = True
                if self.y >= 154:
                    self.y = self.prev_y
                else:
                    self.move_down()

        if other_type == "Spear_MLBL3":

            if self.collides_at(self, 4, 0, "Spear_MLBL3") and not self.block_right:
                self.block_right = True
                if self.x < 596:
                    player = self.load_image(os.path.join("MilbiL3", "Player_MLBL3wSpear.png"))
                    self.set_image(player, 16, 24)


            if self.collides_at(self, -4, 0, "Spear_MLBL3") and not self.block_left:
                self.block_left = True
                if self.x >= 206:
                    player = self.load_image(os.path.join("MilbiL3", "Player_MLBL3wSpear.png"))
                    self.set_image(player, 16, 24)


            if self.collides_at(self, 0, 4, "Spear_MLBL3"):
                self.block_down = True
                if self.y <= 446:
                    player = self.load_image(os.path.join("MilbiL3", "Player_MLBL3wSpear.png"))
                    self.set_image(player, 16, 24)


            if self.collides_at(self, 0, -4, "Spear_MLBL3") and not self.block_up:
                self.block_up = True
                if self.y >= 154:
                    player = self.load_image(os.path.join("MilbiL3", "Player_MLBL3wSpear.png"))
                    self.set_image(player, 16, 24)

            if self.collides_at(self, 4, 0, "Spear_MLBL3") and not self.block_right:
                self.block_right = True
                if self.x < 596:
                    player = self.load_image(os.path.join("MilbiL3", "Player_MLBL3wSpear.png"))
                    self.set_image(player, 16, 24)
                    self.remove_object("Spear_MLBL3")

            if self.collides_at(self, -4, 0, "Spear_MLBL3") and not self.block_left:
                self.block_left = True
                if self.x >= 206:
                    player = self.load_image(os.path.join("MilbiL3", "Player_MLBL3wSpear.png"))
                    self.set_image(player, 16, 24)
                    self.remove_object("Spear_MLBL3")

            if self.collides_at(self, 0, 4, "Spear_MLBL3"):
                self.block_down = True
                if self.y <= 446:
                    player = self.load_image(os.path.join("MilbiL3", "Player_MLBL3wSpear.png"))
                    self.set_image(player, 16, 24)
                    self.remove_object("Spear_MLBL3")

            if self.collides_at(self, 0, -4, "Spear_MLBL3") and not self.block_up:
                self.block_up = True
                if self.y >= 154:
                    player = self.load_image(os.path.join("MilbiL3", "Player_MLBL3wSpear.png"))
                    self.set_image(player, 16, 24)
                    self.remove_object("Spear_MLBL3")

    def key_pressed(self, key):
        if key[pygame.K_LEFT]:
            self.move_left()
            self.facing = self.LEFT
        elif key[pygame.K_RIGHT]:
            self.move_right()
            self.facing = self.RIGHT
        elif key[pygame.K_UP]:
            self.move_up()
            self.facing = self.UP
        elif key[pygame.K_DOWN]:
            self.move_down()
            self.facing = self.DOWN
        elif key[pygame.K_SPACE]:
            self.fire_bullet()

    def joy_pad_signal(self, p1_buttons, p2_buttons):
        if p1_buttons[11] < -0.5:
            self.move_left()
            self.facing = self.LEFT
        elif p1_buttons[11] > 0.5:
            self.move_right()
            self.facing = self.RIGHT
        if p1_buttons[10] < - 0.5:
            self.move_up()
            self.facing = self.UP
        elif p1_buttons[10] > 0.5:
            self.move_down()
            self.facing = self.DOWN
        elif p1_buttons[0]:
            self.fire_bullet()

    def move_right(self):
        if self.x < 600:
            self.x += Globals.move_speed
        else:
            self.room.shift_room_left()
        Globals.player_x += 1

    def move_left(self):
        if self.x > 200:
            self.x -= Globals.move_speed
        else:
            self.room.shift_room_right()
        Globals.player_x -= 1

    def move_up(self):
        if self.y > 150:
            self.y -= Globals.move_speed
        else:
            self.room.shift_room_down()
            Globals.player_y -= 1

    def move_down(self):
        if self.y < 450:
            self.y += Globals.move_speed
        else:
            self.room.shift_room_up()
        Globals.player_y += 1

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

    def fire_bullet(self):
        if self.can_shoot:
            new_bullet = SpearProjectile(self.room, self.rect.centerx, self.y, self.boss_milbi)
            new_bullet.x -= 4
            self.room.add_room_object(new_bullet)
            self.room.room_items.append(new_bullet)
            self.room.set_timer(60, self.reset_shooting)
            self.can_shoot = False

    def reset_shooting(self):
        self.can_shoot = True

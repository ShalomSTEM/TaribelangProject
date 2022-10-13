import os

from GameFrame import RoomObject, Globals


class ORB_MLBL3(RoomObject):
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)
        image = self.load_image(os.path.join("MilbiL3", "Orb_MLBL3.png"))
        self.set_image(image, 32, 32)
        self.countToDestory = 3
        self.imgIndex = 0
        self.register_collision_object("Player_MLBL3")
        self.register_collision_object("Stne_MLBL3")
        self.register_collision_object("BossMLML3")
        self.animate()

    def animate(self):
        self.imgIndex += 1
        if self.imgIndex == 5:
            self.imgIndex = 1
        self.set_image(os.path.join("Images", "MilbiL3", f'orb_{self.imgIndex}.png'), 32, 32)
        self.set_timer(5, self.animate)

    def handle_collision(self, other, other_type):
        if other_type == "Player_MLBL3":
            Globals.destroyed_count += 1
            if Globals.destroyed_count >= self.countToDestory:
                Globals.total_count = 0
                Globals.destroyed_count = 0
                self.room.delete_object(other)
                self.room.complete_loss()
            print((self.countToDestory - Globals.destroyed_count)/3, '%')
            self.room.delete_object(self)

        elif other_type == "Stne_MLBL3":
            self.x_speed = self.x_speed * -1
            self.y_speed = self.y_speed * -1

        elif other_type == "BossMLML3":
            self.delete_object(self)

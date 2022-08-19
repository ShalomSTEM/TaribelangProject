from GameFrame import RoomObject


class Dirt(RoomObject):
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)

        image = self.load_image('dirt.png')
        self.set_image(image, 32, 32)

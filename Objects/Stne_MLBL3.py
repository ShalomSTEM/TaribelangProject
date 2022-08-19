from GameFrame import RoomObject


class Stne_MLBL3(RoomObject):
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)

        image = self.load_image('Images/MilbiL3/Stone_MLBL3.png')
        self.set_image(image, 32, 32)


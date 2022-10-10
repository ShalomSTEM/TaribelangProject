from GameFrame import RoomObject


class StoryFish(RoomObject):
    def __innit__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)

        storyfish_image = self.load_image('CopFish.png')
        self.set_image(storyfish_image, 64, 64)

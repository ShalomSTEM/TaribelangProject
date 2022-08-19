from GameFrame import RoomObject, Globals


class ML2_People(RoomObject):
    def __init__(
        self,
        room,
        x,
        y,
    ):
        RoomObject.__init__(
            self,
            room,
            x,
            y,
        )

        self.set_image("MilbiL2/ML2_people.png", height=50, width=25)

from GameFrame import RoomObject, Globals


class WaterIcon(RoomObject):
    def __init__(self,room,x,y):
        RoomObject.__init__(self,room,x,y)
        self.water_level=16
        self.set_image('Images/Water_Bar_16.png',50,300)
        self.zeroWater=False
        self.Thirst()
        self.UpdateWaterLevel()



    def Thirst(self):
        self.set_timer(15, self.Thirst)
        if self.water_level>0:
            self.water_level-=1
        else:
            self.zeroWater=True
        if self.water_level<5:
            Globals.lowWater=True

    def UpdateWaterLevel(self):
        self.set_timer(3,self.UpdateWaterLevel)
        if (self.water_level>9):
            self.set_image(f'Images/Water_Bar_{self.water_level}.png',50,300)
        else:
            self.set_image(f'Images/Water_Bar_0{self.water_level}.png',50,300)

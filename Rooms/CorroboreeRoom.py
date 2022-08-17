import math

from GameFrame import Level, Globals
from Objects import ML2_People, ML2_Elders


class CorroboreeRoom(Level):
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)

        self.set_background_image('ML2_background.jpg')
        peopleList=[]
        for i in range(30):
            peopleList.append(ML2_People(self, math.cos(i*15)*200+Globals.SCREEN_WIDTH/2, Globals.SCREEN_HEIGHT/2-math.sin(i*15)*200))
            self.add_room_object(peopleList[i])

        elder = ML2_Elders(self, 100, 100)
        self.add_room_object(elder)

        elderList=[]
        for i in range(20):
            #elderList.append(ML2_Elders(self, 100+(i*30), 100))
            #self.add_room_object(elderList[i])
            #elderList.append(ML2_Elders(self, 100+(i*30), 150))
            #self.add_room_object(elderList[i])
            elderList.append(ML2_Elders(self, math.cos(i*15)*100, math.sin(i*1)+100))
            self.add_room_object(elderList[i])





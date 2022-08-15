import pygame

from GameFrame import RoomObject, Globals

class Player(RoomObject):
    def __init__(self,room,x,y,size):
        RoomObject.__init__(self,room,x,y)
        self.size=size
        self.set_image('Images/sprite_0.png',size,size)
        self.depth=5
        self.handle_key_events=True

    def key_pressed(self, key):
        if key[pygame.K_RIGHT]:
            self.set_image('Images/sprite_3.png',self.size,self.size)
            Globals.player_x+=1
        elif key[pygame.K_LEFT]:
            self.set_image('Images/sprite_1.png',self.size,self.size)
            Globals.player_x-=1
        elif key[pygame.K_DOWN]:
            self.set_image('Images/sprite_0.png',self.size,self.size)
            Globals.player_y+=1
        elif key[pygame.K_UP]:
            self.set_image('Images/sprite_2.png',self.size,self.size)
            Globals.player_y-=1



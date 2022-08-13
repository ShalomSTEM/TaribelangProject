import pygame

from GameFrame import RoomObject, Globals

class Player(RoomObject):
    def __init__(self,room,x,y,size):
        RoomObject.__init__(self,room,x,y)
        self.set_image('Images/Player.png',size,size)
        self.depth=5
        self.handle_key_events=True

    def key_pressed(self, key):
        if key[pygame.K_RIGHT]:
            Globals.player_x+=1
        elif key[pygame.K_LEFT]:
            Globals.player_x-=1
        elif key[pygame.K_DOWN]:
            Globals.player_y+=1
        elif key[pygame.K_UP]:
            Globals.player_y-=1



from GameFrame import Level, Globals
import random, math

from Objects import Grass,Dirt, Player


class MilbiL1(Level):
    def __init__(self, screen, joysticks):
        Level.__init__(self,screen,joysticks)
        self.TileSize=100
        self.map=[]
        self.mapsize=100
        self.InitializeTileMap()
        self.Width_TileNum=int(Globals.SCREEN_WIDTH/self.TileSize)
        self.Height_TileNum=int(Globals.SCREEN_HEIGHT/self.TileSize)
        self.player_x=0
        self.player_y=0
        self.fovTileMap=[]
        self.VisTileMap=[]
        self.DisplayTilemap()
        player =Player(self,Globals.SCREEN_HEIGHT/2,Globals.SCREEN_WIDTH/2,self.TileSize)


    def ChangeVisTileMap(self):
        for i in range(self.Width_TileNum):
            row=[]
            for j in range(self.Height_TileNum):
                row.append(self.map[i+self.player_x][j+self.player_y])
            self.VisTileMap.append(row)

    def InitializeTileMap(self):
        for i in range(self.mapsize):
            row =[]
            for j in range(self.mapsize):
                if (random.randint(0,1)):
                    row.append(0)
                else:
                    row.append(1)
            self.map.append(row)
    def DisplayTilemap(self):
        for i in range(self.Width_TileNum):
            for j in range(self.Height_TileNum):
                print(self.map[i + self.player_x][j + self.player_y])
                if self.map[i + self.player_x][j + self.player_y]:
                    self.add_room_object(Grass(self,i*self.TileSize,j*self.TileSize,self.TileSize))
                else:
                    self.add_room_object(Dirt(self,i*self.TileSize,j*self.TileSize,self.TileSize))



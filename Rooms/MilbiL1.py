import time

from GameFrame import Level, Globals
import random, math

from Objects import Grass, Dirt, Player, WaterIcon
from Objects.WaterIcon_Flash import WaterIcon_Flash


class MilbiL1(Level):
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)
        self.TileSize = 100
        self.map = []
        self.Tilemap = []
        self.mapsize = 100
        self.Width_TileNum = int(Globals.SCREEN_WIDTH / self.TileSize)
        self.Height_TileNum = int(Globals.SCREEN_HEIGHT / self.TileSize)
        self.VisTileMap = []
        self.prev_player_x = Globals.player_x
        self.prev_player_y = Globals.player_y
        self.InitializeTileMap()
        self.ChangeVisTileMap()
        self.add_room_object(
            Player(
                self,
                Globals.SCREEN_WIDTH / 2 - self.TileSize / 2,
                Globals.SCREEN_HEIGHT / 2 - self.TileSize / 2,
                self.TileSize,
            )
        )
        self.Eaten = False
        self.watericon = WaterIcon(self, Globals.SCREEN_WIDTH - 50, 20)
        self.add_room_object(self.watericon)
        # self.waterFlash=WaterIcon_Flash(self,Globals.SCREEN_WIDTH-50,20)
        # self.add_room_object(self.waterFlash)
        self.UpdateWorld()
        # self.AnimalMove()

    def UpdateWorld(self):
        self.set_timer(2, self.UpdateWorld)
        print("Ran")
        if (
            self.prev_player_x != Globals.player_x
            or self.prev_player_y != Globals.player_y
        ):
            print("changed")
            if Globals.player_x > self.prev_player_x:
                self.prev_player_x += 1
            elif Globals.player_x < self.prev_player_x:
                self.prev_player_x -= 1
            if Globals.player_y > self.prev_player_y:
                self.prev_player_y += 1
            elif Globals.player_y < self.prev_player_y:
                self.prev_player_y -= 1
            Globals.player_x = self.prev_player_x
            Globals.player_y = self.prev_player_y
            self.ChangeVisTileMap()
            self.DisplayTilemap()
            print(Globals.player_x)
        """
        if (Globals.lowWater):
            self.waterFlash.flash()
            self.delete_object(self.waterFlash)
            self.waterFlash=WaterIcon_Flash(self,Globals.SCREEN_WIDTH-50,20)
        """

    def ChangeVisTileMap(self):
        self.VisTileMap = []
        for i in range(self.Width_TileNum):
            row = []
            for j in range(self.Height_TileNum):
                row.append(self.Tilemap[i + Globals.player_x][j + Globals.player_y])
            self.VisTileMap.append(row)
        print(self.VisTileMap)
        # self.Center=self.VisTileMap[]
        if self.VisTileMap[int(self.Width_TileNum / 2)][int(self.Height_TileNum / 2)]:
            self.Eaten = True
            self.watericon.water_level = min(self.watericon.water_level + 1, 16)
        self.VisTileMap[int(self.Width_TileNum / 2)][int(self.Height_TileNum / 2)] = 0
        self.Tilemap[int(self.Width_TileNum / 2) + Globals.player_x][
            int(self.Height_TileNum / 2) + Globals.player_y
        ] = 0

    def InitializeTileMap(self):
        # Map Gen Algorithm
        for i in range(self.mapsize):
            row = []
            for j in range(self.mapsize):
                if random.randint(0, 3) < 3:
                    row.append(0)
                else:
                    row.append(1)
            self.Tilemap.append(row)
        # Object Add
        for i in range(self.Width_TileNum):
            row = []
            for j in range(self.Height_TileNum):
                if self.Tilemap[i + Globals.player_x][j + Globals.player_y]:
                    row.append(
                        Grass(self, i * self.TileSize, j * self.TileSize, self.TileSize)
                    )

                else:
                    row.append(
                        Dirt(self, i * self.TileSize, j * self.TileSize, self.TileSize)
                    )
                self.add_room_object(row[j])
            self.map.append(row)

    def DisplayTilemap(self):
        # Display Tiles
        for i in range(self.Width_TileNum):
            row = []
            for j in range(self.Height_TileNum):
                if self.VisTileMap[i][j]:
                    row.append(
                        Grass(self, i * self.TileSize, j * self.TileSize, self.TileSize)
                    )
                else:
                    row.append(
                        Dirt(self, i * self.TileSize, j * self.TileSize, self.TileSize)
                    )
                self.add_room_object(row[j])
                # print(row[j])
            self.map.append(row)
        # Delete Tiles
        for i in range(self.Width_TileNum):
            for j in range(self.Height_TileNum):
                self.delete_object(self.map[i][j])
        # Delete from array
        for i in range(self.Width_TileNum):
            self.map.pop(0)

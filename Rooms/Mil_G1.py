from GameFrame import Level, TextObject, Globals, EnumLevels
import random, math, time

from Objects import Grass, Dirt, Player, WaterIcon, Black
from Objects.TitleMilbiButton import TitleMilbiButton
from Objects.WaterIcon_Flash import WaterIcon_Flash


class Mil_G1(Level):
    def __init__(self, screen, joysticks, direct=False):
        Level.__init__(self, screen, joysticks)
        # - Information for Controller Overlay
        self.roomNum = EnumLevels.Mil_G1
        # Important Variables
        self.direct = direct
        self.dead = False
        self.LengthOfStage = 15
        self.finishStage = 10
        self.Time = self.LengthOfStage
        self.timer = TextObject(
            self,
            1210,
            650,
            str(self.Time),
            colour=(255, 255, 255),
            size=50,
            font="Roboto",
        )
        self.stageCaption = TextObject(
            self, 1200, 580, "Stage: 1", colour=(255, 255, 255), size=30, font="Roboto"
        )
        self.stage = 1
        self.TileSize = 100
        self.map = []
        self.Tilemap = []
        self.mapsize = 100
        self.Width_TileNum = int(Globals.SCREEN_WIDTH / self.TileSize)
        self.Height_TileNum = int(Globals.SCREEN_HEIGHT / self.TileSize)
        self.VisTileMap = []
        self.prev_player_x = Globals.player_x
        self.prev_player_y = Globals.player_y
        self.player = Player(
            self,
            Globals.SCREEN_WIDTH / 2 - self.TileSize / 2,
            Globals.SCREEN_HEIGHT / 2 - self.TileSize / 2,
            self.TileSize,
        )
        self.Eaten = False

        # Show Instructions

        self.slideNum=0
        self.Instructions=[]
        self.InstructionSlide()

        # Start Game

        self.set_timer(320,self.startGame)

    def InstructionSlide(self):

        # delete Instruction Text + imgs

        for obj in self.Instructions:
            self.delete_object(obj)
            self.Instructions.pop(0)

        # set timer to add next Instruction

        if self.slideNum < 4:
            self.set_timer(80,self.InstructionSlide)

        # load text based on the slide

        if self.slideNum == 0:
            self.Instructions.append(TextObject(self,160,250,"Use the arrow keys or joystick to move", colour=(255,255,255),size=60,font="Roboto"))
        elif self.slideNum == 1:
            self.Instructions.append(TextObject(self,160,250,"Collect Grass tiles to increase water counter", colour=(255,255,255),size=60,font="Roboto"))
        elif self.slideNum == 2:
            self.Instructions.append(TextObject(self,160,250,"Each stage has less grass", colour=(255,255,255),size=60,font="Roboto"))
        elif self.slideNum == 3:
            self.Instructions.append(TextObject(self,160,250,f"Reach Stage {self.finishStage} without running out of water to win", colour=(255,255,255),size=60,font="Roboto"))

        # add text to the level

        for obj in self.Instructions:
            self.add_room_object(obj)

        self.slideNum += 1


    def startGame(self):

        # Defined watericon outside of init due to not wanting the thirst mechanic whilst Instructions are being shown as this could lead to early death

        self.watericon = WaterIcon(self, Globals.SCREEN_WIDTH - 50, 20)

        # Added simple sidebar Objects

        self.add_room_object(self.watericon)
        self.add_room_object(self.stageCaption)
        self.add_room_object(self.timer)

        # Start timer and stage mechanics

        self.timerIncrease()

        # Create Entire array map of Grass/Dirt using 1s and 0s, then load the initial map of tile objects

        self.InitializeTileMap()

        # Isolate the visible subsection of the entire map to reduce compute time

        self.ChangeVisTileMap()

        # Start the Game

        self.add_room_object(self.player)
        self.UpdateWorld()

    def complete(self):
        if Globals.direct_select:
            Globals.direct_select = False
            Globals.next_level = EnumLevels.Home
        self.running = False

    def timerIncrease(self):
        if not self.dead:
            self.set_timer(20,self.timerIncrease)
            if self.Time-1<0:
                self.stage+=1
                for row in self.map:
                    for obj in row:
                        self.delete_object(obj)
                self.map = []
                self.Tilemap = []
                self.VisTileMap = []
                self.InitializeTileMap()
                self.ChangeVisTileMap()
                self.Time = self.LengthOfStage
                self.stageCaption.text = f"Stage: {self.stage}"
                self.stageCaption.update_text()
            else:
                self.Time -= 1
            self.timer.text = str(self.Time)
            self.timer.update_text()

    def UpdateWorld(self):
        if self.stage==self.finishStage:
            self.complete()
        if not self.dead:
            self.set_timer(1, self.UpdateWorld)

            # If the player has no water left, they die

            if self.watericon.zeroWater:
                self.die()

            # Check if Player moved to reduce redundant compute

            if (
                self.prev_player_x != Globals.player_x
                or self.prev_player_y != Globals.player_y
            ):

                # "normalize" position to prevent player moving many tiles in a short time

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

                # Change the visible map array to agree with current coordinates

                self.ChangeVisTileMap()

                # Add Tiles to screen then delete old ones

                self.DisplayTilemap()

    def ChangeVisTileMap(self):

        # Reset Array, this is fine because it doesn't contain any objects

        self.VisTileMap = []

        # Change visible map array

        for i in range(self.Width_TileNum):
            row = []
            for j in range(self.Height_TileNum):
                row.append(self.Tilemap[i + Globals.player_x][j + Globals.player_y])
            self.VisTileMap.append(row)

        # Check if player on top of grass tile, add to water bar if so

        if self.VisTileMap[int(self.Width_TileNum / 2)][int(self.Height_TileNum / 2)]:
            self.Eaten = True

            # prevent water level from being arbitrarily large by using min function

            self.watericon.water_level = min(self.watericon.water_level + 1, 16)

        # Change tile on top of to dirt, Both on visible and full map array

        self.VisTileMap[int(self.Width_TileNum / 2)][int(self.Height_TileNum / 2)] = 0
        self.Tilemap[int(self.Width_TileNum / 2) + Globals.player_x][
            int(self.Height_TileNum / 2) + Globals.player_y
        ] = 0

    def InitializeTileMap(self):

        # Map Gen Algorithm

        for i in range(self.mapsize):
            row = []
            for j in range(self.mapsize):

                # Use stage num for chance of grass tiles being generated on a tile by tile basis

                if random.randint(0, self.stage) == self.stage:
                    row.append(1)
                else:
                    row.append(0)
            self.Tilemap.append(row)

        # Initialize objects to screen even before accepting user input

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

        # Delete Tiles From Screen

        for i in range(self.Width_TileNum):
            for j in range(self.Height_TileNum):
                self.delete_object(self.map[i][j])

        # Delete from array

        for i in range(self.Width_TileNum):
            self.map.pop(0)

    def die(self):
        self.dead=True
        for row in self.map:
            for obj in row:
                self.delete_object(obj)
        self.delete_object(self.watericon)
        self.delete_object(self.stageCaption)
        self.delete_object(self.timer)
        self.delete_object(self.player)
        self.add_room_object(TextObject(self, 400,100,"Nice Try!",colour=(255,255,255),size=75))
        self.add_room_object(TextObject(self, 300,200,f"You made it to Stage: {self.stage}",colour=(255,255,255),size=75))
        self.set_timer(50,self.restartMilbiL1)

    def restartMilbiL1(self):
        Globals.next_level = 4
        self.running = False

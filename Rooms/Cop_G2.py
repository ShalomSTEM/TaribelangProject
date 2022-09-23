from GameFrame import Level, Globals, EnumLevels, Globals
from Objects import CopG2_Player, CopG2_Block, CopG2_Goal, CopG2_Dirt, CopG2_Water, CopG2_NPC


class Cop_G2(Level):
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)

        self.background_colour = (51, 43, 0)
        self.room_items = []

        # - Information for Controller Overlay
        self.roomNum = EnumLevels.Cop_G2

        # - Set up maze, objects 32x32 - #
        room_objects = [
            'DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD',
            'DBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBD',
            'DB                                              BD',
            'DB                                              BD',
            'DB                                              BD',
            'DB                                              BD',
            'DB                        B                     BD',
            'DB       B  BBBBBBBB      B                     BD',
            'DB       B         B      B                     BD',
            'DB       B         B      B                     BD',
            'DB       B         B      B                     BD',
            'DB       BBBBBBB   B      B                     BD',
            'DB                                              BD',
            'DB                                              BD',
            'DB           BBBBBB  BBBBBBB                    BD',
            'DB           B     N   N   B                    BD',
            'DB           B  N     P    B                    BD',
            'DB           B    N        B                    BD',
            'DB           B   N    N    B                    BD',
            'DB           BBBBBBBBBBBB  B                    BD',
            'DB                             BBBBB   BBBBBB   BD',
            'DB                                              BD',
            'DB       BB   BBBBBBBBBBB                       BD',
            'DB       B              B   BBBBBBBBBBBBBBBBB   BD',
            'DB       B              B   B                   BD',
            'DB       B    BBBBBBB   B                       BD',
            'DB       B   BBBBB     BBBBBBBBBBBBBBBBBBBBB    BD',
            'DB       B   B                             B    BD',
            'DB       B   B                             B    BD',
            'DBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB  BBBBBBD',
            'WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW'
        ]

        self.player = CopG2_Player(self, 0, 0)
        for i, row in enumerate(room_objects):
            for j, obj in enumerate(row):
                if obj == 'B':
                    new_block = CopG2_Block(self, j * 32 - 200, i * 32 - 200)
                    self.add_room_object(new_block)
                    self.room_items.append(new_block)
                elif obj == 'P':
                    self.player.x = j * 32 - 200
                    self.player.y = i * 32 - 200
                    self.add_room_object(self.player)
                elif obj == 'G':
                    new_goal = CopG2_Goal(self, j * 32 - 200, i * 32 - 200)
                    self.add_room_object(new_goal)
                    self.room_items.append(new_goal)
                elif obj == 'D':
                    new_dirt = CopG2_Dirt(self, j * 32 - 200, i * 32 - 200)
                    self.add_room_object(new_dirt)
                    self.room_items.append(new_dirt)
                elif obj == 'W':
                    new_water = CopG2_Water(self, j * 32 - 200, i * 32 - 200)
                    self.add_room_object(new_water)
                    self.room_items.append(new_water)
                elif obj == 'N':
                    new_npc = CopG2_NPC(self, j * 32 - 200, i * 32 - 200, self.player)
                    self.add_room_object(new_npc)
                    self.room_items.append(new_npc)

    def shift_room_left(self):
        for item in self.room_items:
            item.x -= Globals.move_speed

    def shift_room_right(self):
        for item in self.room_items:
            item.x += Globals.move_speed

    def shift_room_up(self):
        for item in self.room_items:
            item.y -= Globals.move_speed

    def shift_room_down(self):
        for item in self.room_items:
            item.y += Globals.move_speed

    def complete(self):
        if Globals.direct_select:
            Globals.direct_select = False
            Globals.next_level = EnumLevels.Home
        self.running = False


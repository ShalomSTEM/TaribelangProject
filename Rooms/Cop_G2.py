from GameFrame import Level, EnumLevels, Globals
from Objects import CopG2_Player, CopG2_Block, CopG2_Dirt, CopG2_Water, CopG2_NPC, CopG2_GF_Water


class Cop_G2(Level):
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)

        self.background_color = (90, 77, 43)

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
            'DB                 B       B                    BD',
            'DB              N  B  N    B       N            BD',
            'DB        N        B       B                    BD',
            'DB                 B       B               N    BD',
            'DB                 B       B                    BD',
            'DB       B N        B     B                     BD',
            'DB                  B     B       BB            BD',
            'DB                  B     B         BB     N    BD',
            'DB                  B     B                     BD',
            'DB                  B N  B                      BD',
            'DB                  B    B  BB     N            BD',
            'DB  P    N          B    B B  B                 BD',
            'DB                  B    BB    BBB              BD',
            'DB                  B    B        B             BD',
            'DB                 B               B N          BD',
            'DB                  B       N       B           BD',
            'DB        N        B                 BBBBBBBBBBBBD',
            'DB                  B                    DDDDDDDBD',
            'DB                 B                     DWWWWWDBD',
            'DB                B                      DWGWWWDBD',
            'DB                 B                     DWWWGWDBD',
            'DB                  B                    DWGWWWDBD',
            'DB                   B                   DWWWWWDBD',
            'DB                  B                    DDDDDDDBD',
            'DBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBD',
            'DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD'
        ]

        x_shift = - 50
        self.player = CopG2_Player(self, 0, 0)
        for i, row in enumerate(room_objects):
            for j, obj in enumerate(row):
                if obj == 'B':
                    new_block = CopG2_Block(self, j * 32 - x_shift, i * 32 - 200)
                    self.add_room_object(new_block)
                    self.room_items.append(new_block)
                elif obj == 'P':
                    self.player.x = j * 32 - x_shift
                    self.player.y = i * 32 - 200
                    self.add_room_object(self.player)
                elif obj == 'D':
                    new_dirt = CopG2_Dirt(self, j * 32 - x_shift, i * 32 - 200)
                    self.add_room_object(new_dirt)
                    self.room_items.append(new_dirt)
                elif obj == 'W':
                    new_water = CopG2_Water(self, j * 32 - x_shift, i * 32 - 200)
                    self.add_room_object(new_water)
                    self.room_items.append(new_water)
                elif obj == 'G':
                    new_water = CopG2_GF_Water(self, j * 32 - x_shift, i * 32 - 200)
                    self.add_room_object(new_water)
                    self.room_items.append(new_water)
                elif obj == 'N':
                    new_npc = CopG2_NPC(self, j * 32 - x_shift, i * 32 - 200, self.player)
                    self.add_room_object(new_npc)
                    self.room_items.append(new_npc)
        self.bush_sounds = self.load_sound("bush_sounds.ogg")
        self.bush_sounds.set_volume(0.4)
        self.bush_sounds.play(-1)

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
        self.bush_sounds.stop()
        self.running = False


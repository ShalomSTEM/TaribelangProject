from GameFrame import Bot, Globals


class RedBot(Bot):
    def __init__(self, x, y):
        Bot.__init__(self, x, y)
        red_bot_image = self.load_image('bot_red.png')
        self.set_image(red_bot_image, 25, 25)

        self.rotate(90)

        self.register_collision_object('Player_MLBL3')

    def tick(self):
        pass

    def handle_collision(self, other):
        if isinstance(other):
            self.has_flag = True
            for bot in Globals.red_bots:
                if bot.has_flag and bot is not self:
                    self.has_flag = False
                    break
        elif isinstance(other):
            if self.x < Globals.SCREEN_WIDTH / 2 and not other.jailed:
                self.has_flag = False
                self.curr_rotation = 0
                self.rotate(90)
                self.x = Globals.SCREEN_WIDTH - 36
                self.y = Globals.SCREEN_HEIGHT - 40
                self.jailed = True
        elif isinstance(other, RedBot):
            if not other.jailed:
                self.jailed = False

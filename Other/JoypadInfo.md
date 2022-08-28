def joy_pad_signal(self, p1_buttons, p2_buttons):
        if p1_buttons[11] > 0.5:
            print("11 positive")
            self.set_image(
                os.path.join(Globals.milbiL1_path, "sprite_3.png"), self.size, self.size
            )
            Globals.player_x += 1
        if p1_buttons[11] < -0.5:
            print("11 neg")
            self.set_image(
                os.path.join(Globals.milbiL1_path, "sprite_1.png"), self.size, self.size
            )
            Globals.player_x -= 1
        if p1_buttons[10] < -0.5:
            print("10 neg")
            self.set_image(
                os.path.join(Globals.milbiL1_path, "sprite_2.png"), self.size, self.size
            )
            Globals.player_y -= 1
        if p1_buttons[10] > 0.5:
            print("10 pos")
            self.set_image(
                os.path.join(Globals.milbiL1_path, "sprite_0.png"), self.size, self.size
            )
            Globals.player_y += 1

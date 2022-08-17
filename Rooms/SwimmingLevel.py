from GameFrame import Level, Globals, TextObject
from Objects import Sparrow, Ground, ColumnTop, ColumnBottom, GameOverBackground, Surface
import random
import pygame
from GameFrame.Globals import Globals


class SwimmingLevel(Level):
    def __init__(self, room, joysticks):
        Level.__init__(self, room, joysticks)

        self.heights = [180, 430, 400, 180, 150, 370, 250, 339, 150, 420, 300, 180]
        self.timings = [160, 150, 140, 130, 120, 110, 90, 80, 100, 120, 130, 140]
        self.timings_index = 0

        self.main_sound = self.load_sound('music.wav')
        self.main_sound.play(-1)

        self.over = self.load_sound('game_over.wav')

        self.set_background_image('background.png')

        # Add Ground and set scrolling to the left
        ground_1 = Ground(self, 0, 499)
        ground_2 = Ground(self, 800, 499)
        self.add_room_object(ground_1)
        self.add_room_object(ground_2)

        # Add surface and set scrolling to the left
        surface = Surface(self, 0, -101)
        self.add_room_object(surface)

        bird = Sparrow(self, Globals.sparrow_x, 300)
        self.add_room_object(bird)

        lives_text = "LIVES: {}".format(Globals.LIVES)
        self.lives_text = TextObject(self, 500, 10, 'Lives: %i' % Globals.LIVES)
        self.add_room_object(self.lives_text)
        self.lives_text.depth = 2000
        self.lives_text.colour = (255, 255, 255)

        score_text = "SCORE: {}".format(Globals.SCORE)
        self.score_text = TextObject(self, 50, 10, 'Score: %i' % Globals.SCORE)
        self.add_room_object(self.score_text)
        self.score_text.depth = 2000
        self.score_text.colour = (255, 255, 255)

        self.set_timer(150, self.add_column)

    def add_column(self):
        height = self.heights[self.timings_index]
        bottom_column = ColumnBottom(self, 800, height)
        top_column = ColumnTop(self, 800, height - 700)
        self.add_room_object(top_column)
        self.add_room_object(bottom_column)

        self.timings_index += 1
        if self.timings_index == len(self.timings):
            self.timings_index = 0
            self.set_timer(90, self.add_column)
        else:
            self.set_timer(self.timings[self.timings_index], self.add_column)

    def update_score(self):
        self.score_text.text = "SCORE: {}".format(Globals.SCORE)
        self.score_text.update_text()
        pass

    def update_lives(self, value):
        Globals.LIVES += value
        if Globals.LIVES == 0:
            self.running = False
            self.quitting = True
        self.lives_text.text = 'Lives: %i' % Globals.LIVES
        self.lives_text.update_text()
        Globals.LIVES = Globals.LIVES - 1

    def game_over(self):
        Globals.LIVES = Globals.LIVES - 1

        if Globals.LIVES <= 0:
            self.running = False
            self.quitting = True
        Globals.scroll_speed = 0
        Globals.delay_short = 80
        Globals.delay_long = 120

        go_bg = GameOverBackground(self, 110, 90)
        go_bg.depth = 100
        self.add_room_object(go_bg)

        game_over_text = TextObject(self, 250, 140, 'GAME OVER', 60)
        game_over_text.depth = 500
        self.add_room_object(game_over_text)

        final_score_text = "SCORE: {} HIGH SCORE: {}".format(Globals.SCORE, Globals.high_score)
        final_score_text_obj = TextObject(self, 150, 220, final_score_text, 40)
        final_score_text_obj.depth = 200
        self.add_room_object(final_score_text_obj)

        self.delete_object(self.score_text)

        press_enter_text = TextObject(self, 150, 300, "Press 'Enter' or 'Select' to play again", 30)
        press_enter_text.depth = 500
        self.add_room_object(press_enter_text)

        self.main_sound.stop()
        self.over.play()

from GameFrame import RoomObject, Globals
import pygame
class ButtonForPlaceholder(RoomObject):
    def __init__(self, room, x, y):
        RoomObject.__init__(room, x, y)
        self.set_image(
            "Images/Title/PlaceHolder.png",
            height=Globals.SCREEN_HEIGHT - Globals.SCREEN_HEIGHT / 4,
            width=Globals.SCREEN_WIDTH - Globals.SCREEN_WIDTH / 4,
        )
    def key_pressed(self, key):
        if key[pygame.K_q]:
            Globals.next_level = Globals.EnumLevels.Quiz
        elif key[pygame.KEY_M]:
            Globals.next_level = Globals.EnumLevels.MilbiSelect
        elif key[pygame.K_c]:
            Globals.next_level = Globals.EnumLevels.Copple
        elif key[pygame.K_o]:
            Globals.next_level = Globals.EnumLevels.Museum
        elif key[pygame.K_i]:
            Globals.next_level = Globals.EnumLevels.Intro

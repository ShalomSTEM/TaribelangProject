from enum import Enum
import pygame
import pygame.freetype
from pygame.sprite import Sprite
from pygame.sprite import RenderUpdates

BLUE = (106, 159, 181)
WHITE = (255, 255, 255)
game = "invalid"


def create_surface_with_text(text, font_size, text_rgb, bg_rgb):
    """Returns surface with text written on"""
    font = pygame.freetype.SysFont("Courier", font_size, bold=True)
    surface, _ = font.render(text=text, fgcolor=text_rgb, bgcolor=bg_rgb)
    return surface.convert_alpha()


class UIElement(Sprite):
    """An user interface element that can be added to a surface"""

    def __init__(self, center_position, text, font_size, bg_rgb, text_rgb, action=None):
        """
        Args:
            center_position - tuple (x, y)
            text - string of text to write
            font_size - int
            bg_rgb (background colour) - tuple (r, g, b)
            text_rgb (text colour) - tuple (r, g, b)
            action - the gamestate change associated with this button
        """
        self.mouse_over = False

        default_image = create_surface_with_text(
            text=text, font_size=font_size, text_rgb=text_rgb, bg_rgb=bg_rgb
        )

        highlighted_image = create_surface_with_text(
            text=text, font_size=font_size * 1.2, text_rgb=text_rgb, bg_rgb=bg_rgb
        )

        self.images = [default_image, highlighted_image]

        self.rects = [
            default_image.get_rect(center=center_position),
            highlighted_image.get_rect(center=center_position),
        ]

        self.action = action

        super().__init__()

    @property
    def image(self):
        return self.images[1] if self.mouse_over else self.images[0]

    @property
    def rect(self):
        return self.rects[1] if self.mouse_over else self.rects[0]

    def update(self, mouse_pos, mouse_up):
        """Updates the mouse_over variable and returns the button's
        action value when clicked.
        """
        if self.rect.collidepoint(mouse_pos):
            self.mouse_over = True
            if mouse_up:
                return self.action
        else:
            self.mouse_over = False

    def draw(self, surface):
        """Draws element onto a surface"""
        surface.blit(self.image, self.rect)


class Player:
    """Stores information about a player"""

    def __init__(self, score=0, lives=3, current_level=1):
        self.score = score
        self.lives = lives
        self.current_level = current_level


def main():
    pygame.init()
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    game_state = GameState.TITLE
    screen_size = screen.get_size()

    while True:
        if game_state == GameState.TITLE:
            game_state = title_screen(screen, screen_size)

        if game_state == GameState.NEWGAMEMILBI:
            player = Player()
            game_state = play_carpet(screen, player, screen_size)

        if game_state == GameState.NEWGAMECARPET:
            player = Player()
            game_state = play_milbi(screen, player, screen_size)

        if game_state == GameState.NEXT_LEVEL and game == "carpet":
            player.current_level += 1
            if game == "carpet":
                game_state = play_carpet(screen, player, screen_size)
            else:
                game_state = play_milbi(screen, player, screen_size)
        if game_state == GameState.QUIT:
            pygame.quit()
            return


def title_screen(screen, screen_size):
    """_summary_

    Args:
        screen (Any): the screen
        screen_size (Tuple): the screen size

    Returns:
        game_loop(screen, buttons): repeats until an action is performed from a sprite or button
    """
    start_btn_milbi = UIElement(
        center_position=(
            (screen_size[0] / 4) + (screen_size[0] / 2),
            (screen_size[1] / 2) - 100,
        ),
        font_size=50,
        bg_rgb=BLUE,
        text_rgb=WHITE,
        text="Milbi",
        action=GameState.NEWGAMEMILBI,
    )
    start_btn_carpet = UIElement(
        center_position=(screen_size[0] / 4, (screen_size[1] / 2) - 100),
        font_size=50,
        bg_rgb=BLUE,
        text_rgb=WHITE,
        text="Carpet",
        action=GameState.NEWGAMECARPET,
    )
    quit_btn = UIElement(
        center_position=(screen_size[0] / 2, screen_size[1] / 2),
        font_size=50,
        bg_rgb=BLUE,
        text_rgb=WHITE,
        text="Quit",
        action=GameState.QUIT,
    )

    buttons = RenderUpdates(start_btn_milbi, start_btn_carpet, quit_btn)

    return game_loop(screen, buttons)


def play_milbi(screen, player, screen_size):
    """_summary_

    Args:
        screen (Any): the screen
        player (Any): the player
        screen_size (Tuple): the screen size

    Returns:
        game_loop(screen, buttons): repeats until an action is performed from a sprite or button
    """
    global game
    game = "milbi"
    return_btn = UIElement(
        center_position=(
            screen_size[0] / 6 + 20,
            screen_size[1] - (screen_size[1] * 4 / 100),
        ),
        font_size=50,
        bg_rgb=BLUE,
        text_rgb=WHITE,
        text="Return to main menu",
        action=GameState.TITLE,
    )
    nextlevel_btn = UIElement(
        center_position=(screen_size[0] / 2, screen_size[1] / 2),
        font_size=50,
        bg_rgb=BLUE,
        text_rgb=WHITE,
        text=f"Next level ({player.current_level + 1})",
        action=GameState.NEXT_LEVEL,
    )
    buttons = RenderUpdates(return_btn, nextlevel_btn)

    return game_loop(screen, buttons)


def play_carpet(screen, player, screen_size):
    """_summary_

    Args:
        screen (Any): the screen
        player (Any): the player
        screen_size (Tuple): the screen size

    Returns:
        game_loop(screen, buttons): repeats until an action is performed from a sprite or button
    """
    global game
    game = "carpet"
    return_btn = UIElement(
        center_position=(
            screen_size[0] / 6 + 20,
            screen_size[1] - (screen_size[1] * 4 / 100),
        ),
        font_size=50,
        bg_rgb=BLUE,
        text_rgb=WHITE,
        text="Return to main menu",
        action=GameState.TITLE,
    )

    nextlevel_btn = UIElement(
        center_position=(screen_size[0] / 2, screen_size[1] / 2),
        font_size=50,
        bg_rgb=BLUE,
        text_rgb=WHITE,
        text=f"Next level ({player.current_level + 1})",
        action=GameState.NEXT_LEVEL,
    )

    buttons = RenderUpdates(return_btn, nextlevel_btn)

    return game_loop(screen, buttons)


def game_loop(screen, buttons):
    """Handles game loop until an action is return by a button in the
    buttons sprite renderer.
    """
    while True:
        mouse_up = False
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_up = True
        screen.fill(BLUE)

        for button in buttons:
            ui_action = button.update(pygame.mouse.get_pos(), mouse_up)
            if ui_action is not None:
                return ui_action

        buttons.draw(screen)
        pygame.display.flip()


class GameState(Enum):
    QUIT = -1
    TITLE = 0
    NEWGAMECARPET = 1
    NEWGAMEMILBI = 2
    NEXT_LEVEL = 3


if __name__ == "__main__":
    main()

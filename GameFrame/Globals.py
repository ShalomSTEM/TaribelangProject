from enum import IntEnum
class Globals:
    class EnumLevels(IntEnum):
        Intro = 0
        Home = 1
        MilbiSelect = 2
        Mil_S1 = 3
        Mil_G1 = 4
        Mil_S2 = 5
        Mil_G2 = 6
        Mil_S3 = 7
        Mil_G3 = 8
        Mil_S4 = 9
        Museum = 10
        Quiz = 11
        Copple = 12

    running = True
    FRAMES_PER_SECOND = 30

    SCREEN_WIDTH = 1280
    SCREEN_HEIGHT = 720

    SCORE = 0

    # - Set the starting number of lives - #
    LIVES = 3

    # - Set the Window display name - #
    window_name = "Game"

    # - Set the order of the rooms - #
    levels = [
        "Intro",
        "Home",
        "MilbiSelect",
        "Mil_S1",
        "Mil_G1",
        "Mil_S2",
        "Mil_G2",
        "Mil_S3",
        "Mil_G3",
        "Mil_S4",
        "Museum",
        "Quiz",
        "Copple",
    ]

    # - Set the starting level - #
    start_level = EnumLevels.Copple

    # - Set this number to the level you want to jump to when the game ends - #
    end_game_level = 0

    # - This variable keeps track of the room that will follow the current room - #
    # - Change this value to move through rooms in a non-sequential manner - #
    next_level = 0

    # - Change variable to True to exit the program - #
    exiting = False

    # ############################################################# #
    # ###### User Defined Global Variables below this line ######## #
    # ############################################################# #
    move_speed = 4
    SLOW = 1
    MEDIUM = 2
    FAST = 3
    mlb3_move_speed = 4
    total_count = 0
    destroyed_count = 0
    player_x = 0
    player_y = 0
    lowWater = False
    path = "Images/"
    milbiL1_path = "Images/MilbiL1"
    milbiL1_alt_path = "MilbiL1/"
    milbiL2_path = "Images/MilbiL2"
    milbiL2_alt_path = "MilbiL2/"
    milbiL3_path = "Images/MilbiL3"
    milbiL3_alt_path = "MilbiL3/"
    storyOverlay_path = "Images/StoryOverlay"
    storyOverlay_alt_path = "Images/StoryOverlay"
    WTC_path = "Images/WTC"
    WTC_alt_path = "Images/WTC"

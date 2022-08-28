import string


class Globals:
    # Levels
    # Accessed via Globals.Enum(levelname)
    EnumTitleRoom = 4
    EnumMilbiL1 = 1
    EnumMilbiL2 = 3
    EnumMilbiL3 = 2
    EnumWTC_Taribelang = 0
    EnumMilbiTransition = 5

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
        "WTC_Taribalang",
        "MilbiL1",
        "MilbiL3",
        "CorroboreeRoom",
        "TitleScreen",
        "MilbiTransition",
    ]

    # - Set the starting level - #
    start_level = 5

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

    total_count = 0
    title_Level = 0
    destroyed_count = 0
    title_selection = 0
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
    WTC_path = "WTC/"
    WTC_alt_path = "Images/WTC"
    title_path = "Images/Title"
    title_alt_path = "Title/"
    TransitionLeft = False
    TransitionRight = False
    currentSelectedTransition = 2
    Transition = string

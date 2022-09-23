from enum import IntEnum


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
    Mil_S_Only = 10
    Mil_G_Only_Select = 11
    CoppleSelect = 12
    Cop_S1 = 13
    Cop_G1 = 14
    Cop_S2 = 15
    Cop_G2 = 16
    Cop_S3 = 17
    Cop_G3 = 18
    Cop_S4 = 19
    Cop_S_Only = 20
    Cop_G_Only_Select = 21
    Museum = 22
    ControllerOverlay = 23


class Globals:
    running = True
    FRAMES_PER_SECOND = 30

    SCREEN_WIDTH = 1280
    SCREEN_HEIGHT = 720

    SCORE = 0

    # - Set the starting number of lives - #
    LIVES = 3

    # - Set the Window display name - #
    window_name = "Taribelang Time"

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
        "Mil_S_Only",
        "Mil_G_Only_Select",
        "CoppleSelect",
        "Cop_S1",
        "Cop_G1",
        "Cop_S2",
        "Cop_G2",
        "Cop_S3",
        "Cop_G3",
        "Cop_S4",
        "Cop_S_Only",
        "Cop_G_Only_Select",
        "Museum",
        "ControllerOverlay"
    ]

    # - Set the starting level - #
    start_level = EnumLevels.Intro

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

    # - Indicates that the room is to return to the menu - #
    # -      rather than the next part of the story      - #
    direct_select = False
    
    # MilbiL3
    move_speed = 5     
    ORB_move_speed = 6
    
    total_count = 0
    destroyed_count = 0
    player_x = 0
    player_y = 0
    lowWater = False

    # Move speed for Copple Game 2 & Milbi Boss
    NPCmove_speed = 4
    
    #ControllerOverlay
    oldRoom = 0
    OverlayButtons = ""
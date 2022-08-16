from enum import IntEnum


class EnumLevels(IntEnum):
    TitleRoom = 0
    InfoPage = 1
    Controls = 2
    About = 3
    WurrumbuPage = 4
    ManjalPage = 5
    KubirriPage = 6
    QuizPage = 7
    FinishQuiz = 8
    KubirriAndWurrumbuPage = 9
    StoryIntro = 10
    StoryMid = 11
    StoryWurrumbu = 12
    StoryEnd = 13
    ForagingRoom = 14
    EscapeLevelIntro = 15
    EscapeLevelInstructions = 16
    EscapeLevel = 17
    EscapeLevelOutro = 18
    FightRoom = 19
    StoryClimb = 20
    DonkeyKong_Controls = 21
    DonkeyKong = 22
    LevelSelect = 23

class Globals:

    running = True
    FRAMES_PER_SECOND = 30
    
    SCREEN_WIDTH = 1280
    SCREEN_HEIGHT = 720


    SCORE = 0

    # - Set the starting number of lives - #
    LIVES = 3

    # - Set the Window display name - #

    window_name = 'Game'

    # - Set the order of the rooms - #
    levels = ["CorroboreeRoom"]

    window_name = "MilbiL1"

    # - Set the order of the rooms - #
    levels = ["MilbiL1", "MilbiL3", "CorroboreeRoom"]

    # - Set the starting level - #
    start_level = 0

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
    destroyed_count = 0
    player_x = 0
    player_y = 0
    lowWater = False


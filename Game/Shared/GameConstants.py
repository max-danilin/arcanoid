import os

class GameConstants:
    '''Class, containing various constants.'''

    SCREEN_SIZE = [800, 600]
    BRICK_SIZE = [100, 30]
    BALL_SIZE = [16, 16]
    PAD_SIZE = [139, 13]
    
    SPRITE_BALL = os.path.join("Assets", "ball.png")
    SPRITE_PAD = os.path.join("Assets", "pad.png")
    SPRITE_BRICK = os.path.join("Assets", "standard.png")
    SPRITE_SPEED_BRICK = os.path.join("Assets", "speed.png")
    SPRITE_LIFE_BRICK = os.path.join("Assets", "life.png")
    SPRITE_HIGHSCORE = os.path.join("Assets", "highscore.png")
    SPRITE_MENU = os.path.join("Assets", "menu.png")
    
    SOUND_FILE_BRICK_HIT = os.path.join("Assets", "BrickHit.wav")
    SOUND_FILE_PAD_BOUNCE = os.path.join("Assets", "PadBounce.wav")
    SOUND_FILE_WALL_BOUNCE = os.path.join("Assets", "WallBounce.wav")
    SOUND_FILE_SPEED_UP = os.path.join("Assets", "SpeedUp.wav")
    SOUND_FILE_EXTRA_LIFE = os.path.join("Assets", "ExtraLife.wav")
    SOUND_FILE_GAMEOVER = os.path.join("Assets", "GameOver.wav")

    SOUND_BRICK_HIT = 0
    SOUND_PAD_BOUNCE = 1
    SOUND_WALL_BOUNCE = 2
    SOUND_SPEED_UP = 3
    SOUND_EXTRA_LIFE = 4
    SOUND_GAMEOVER = 5
    
    PLAYING_SCENE = 0
    GAMOVER_SCENE = 1
    HIGHSCORE_SCENE = 2
    MENU_SCENE = 3
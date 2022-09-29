import pygame
from Game import *
from Game.Scenes import *
from Game.Shared import GameConstants
from Game.Ball import Ball
from Game.Level import Level
from Game.Pad import Pad
from typing import Tuple, List


class Breakout:
    """Class, creating an instance of a breakout game."""

    def __init__(self):
        """
        Initializing a game instance
        lives: number of lives at the beginning
        score: initial score
        level: initial level
        scenes: tuple of available scenes
        sounds: tuple of available sounds
        """

        self.__lives : int = 1
        self.__score : int = 0
        self.__level : Level = Level(self)
        self.__pad : Pad = Pad((0, 0), pygame.image.load(GameConstants.SPRITE_PAD))
        self.__balls : List[Ball] = [
            Ball(positions = (100, 100), sprite = pygame.image.load(GameConstants.SPRITE_BALL), game = self)
        ]

        #Initializing pygame, setting up screen, making mouse invisible inside our screen
        pygame.init()
        pygame.mixer.init()
        pygame.display.set_caption("Incredible Game")

        self.__clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(GameConstants.SCREEN_SIZE, pygame.DOUBLEBUF, 32) #| pygame.FULLSCREEN, 32)
        pygame.mouse.set_visible(0)
        
        self.__scenes : Tuple[Scene, ...] = (
            PlayingGameScene(self),
            GameOverScene(self),
            HighscoreScene(self),
            MenuScene(self)
        )

        self.__currentScene : int = 3

        self.__sounds = (
            pygame.mixer.Sound(GameConstants.SOUND_FILE_BRICK_HIT),
            pygame.mixer.Sound(GameConstants.SOUND_FILE_PAD_BOUNCE),
            pygame.mixer.Sound(GameConstants.SOUND_FILE_WALL_BOUNCE),
            pygame.mixer.Sound(GameConstants.SOUND_FILE_SPEED_UP),
            pygame.mixer.Sound(GameConstants.SOUND_FILE_EXTRA_LIFE),
            pygame.mixer.Sound(GameConstants.SOUND_FILE_GAMEOVER)
        )

    def start(self) -> None:
        """
        Setting up scene, waiting for events and constantly rendering it.
        """
        while True:
            self.__clock.tick(100)
            self.screen.fill((0, 0, 0))

            currentScene = self.__scenes[self.__currentScene]
            currentScene.handleEvents(pygame.event.get())
            currentScene.render()
            
            pygame.display.update()

    def changeScene(self, scene: int) -> None:
        """
        Changing the current scene.
        :param scene: number of scene to set up
        """
        self.__currentScene = scene

    @property
    def getLevel(self) -> Level:
        return self.__level

    @property
    def getScore(self) -> int:
        return self.__score
    
    def increaseScore(self, score: int):
        self.__score += score

    @property
    def getLives(self) -> int:
        return self.__lives

    @property
    def getBalls(self) -> List[Ball]:
        return self.__balls

    @property
    def getPad(self) -> Pad:
        return self.__pad
    
    def playSound(self, soundClip: int) -> None:
        """
        Function for playing specified sound from a tuple of sounds.
        :param soundClip: number of sound to play
        """
        sound = self.__sounds[soundClip]
        sound.stop()
        sound.play()
    
    def increaseLives(self) -> None:
        self.__lives += 1
    
    def reduceLives(self) -> None:
        self.__lives -= 1
    
    def reset(self) -> None:
        """
        Resetting our game with specified number of lives and score.
        """
        self.__lives = 5
        self.__score = 0
        self.__level.load(0)


game = Breakout()
game.start()
import os
import fileinput
import pygame
import random
from Game.Shared import GameConstants
from Game.Bricks import *
from typing import List


class Level:
    """Class, constructing levels in our game"""

    def __init__(self, game: 'Breakout'):
        self.__game: 'Breakout' = game
        self.__bricks: List['Brick'] = []
        self.__amountOfBricksLeft: int = 0
        self.__currentLevel: int = 0

    @property
    def getBricks(self) -> List['Brick']:
        return self.__bricks

    @property
    def getAmountOfBricksLeft(self) -> int:
        return self.__amountOfBricksLeft

    def brickHit(self) -> None:
        """
        Method decreasing amount of bricks in case of brick being hit
        """
        self.__amountOfBricksLeft -= 1

    def loadNextLevel(self) -> None:
        """
        Method trying to load pre-created levels or random ones otherwise
        """
        self.__currentLevel += 1

        if not os.path.exists(os.path.join("Assets", "Levels", "level" + str(self.__currentLevel) + ".dat")):
            self.loadRandom()
        else:
            self.load(self.__currentLevel)

    def load(self, level: int) -> None:
        """
        Main method filling level with various bricks from .dat file with description
        :param level: level, we are trying to load
        """
        self.__currentLevel = level
        self.__bricks = []
        x, y = 0, 0

        # Filling X axis with bricks layer by layer
        for line in fileinput.input(os.path.join("Assets", "Levels", "level" + str(level) + ".dat")):
            for currentBrick in line:
                if currentBrick == "1":
                    brick = Brick(positions=(x, y), sprite=pygame.image.load(GameConstants.SPRITE_BRICK),
                                  game=self.__game)
                    self.__bricks.append(brick)
                    self.__amountOfBricksLeft += 1
                elif currentBrick == "2":
                    brick = SpeedBrick(positions=(x, y), sprite=pygame.image.load(GameConstants.SPRITE_SPEED_BRICK),
                                       game=self.__game)
                    self.__bricks.append(brick)
                    self.__amountOfBricksLeft += 1
                elif currentBrick == "3":
                    brick = LifeBrick(positions=(x, y), sprite=pygame.image.load(GameConstants.SPRITE_LIFE_BRICK),
                                      game=self.__game)
                    self.__bricks.append(brick)
                    self.__amountOfBricksLeft += 1
                x += GameConstants.BRICK_SIZE[0]
            # Getting to the next Y layer
            x = 0
            y += GameConstants.BRICK_SIZE[1]

    def loadRandom(self) -> None:
        """
        Method for loading random levels.
        maxBricks: maximum amount of bricks that can fit in X axis
        rows: random number between 2 and 7
        amountOfSuperBricks: no more than 4 super bricks per level
        """
        self.__bricks = []
        x, y = 0, 0

        maxBricks = int(GameConstants.SCREEN_SIZE[0] / GameConstants.BRICK_SIZE[0])
        rows = random.randint(2, 7)

        amountOfSuperBricks = 0
        # Filling X axis with bricks layer by layer
        for row in range(0, rows):
            for brick in range(0, maxBricks):
                brickType = random.randint(0, 3)
                if brickType == 1 or amountOfSuperBricks > 3:
                    brick = Brick(positions=(x, y), sprite=pygame.image.load(GameConstants.SPRITE_BRICK),
                                  game=self.__game)
                    self.__bricks.append(brick)
                    self.__amountOfBricksLeft += 1
                elif brickType == 2:
                    brick = SpeedBrick(positions=(x, y), sprite=pygame.image.load(GameConstants.SPRITE_SPEED_BRICK),
                                       game=self.__game)
                    self.__bricks.append(brick)
                    self.__amountOfBricksLeft += 1
                    amountOfSuperBricks += 1
                elif brickType == 3:
                    brick = LifeBrick(positions=(x, y), sprite=pygame.image.load(GameConstants.SPRITE_LIFE_BRICK),
                                      game=self.__game)
                    self.__bricks.append(brick)
                    self.__amountOfBricksLeft += 1
                    amountOfSuperBricks += 1
                x += GameConstants.BRICK_SIZE[0]
            # Getting to the next Y layer
            x = 0
            y += GameConstants.BRICK_SIZE[1]

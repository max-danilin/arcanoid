from Game.Shared import *
from dataclasses import dataclass, field
import pygame
from typing import List, Union, Tuple, Optional


@dataclass
class _GameBase:
    """Class needed to keep MRO, because game parameter is not-default"""
    game: 'Breakout'


@dataclass
class Ball(GameObject, _GameBase):
    """
    Class, defining ball object.
    size: size of the ball
    speedInternal: speed of the ball
    increment: the amount we increment ball position each time while it is in motion
    direction: direction of the ball
    inMotion: checks if the ball is in motion
    """

    size: List[int] = field(default_factory = lambda: GameConstants.BALL_SIZE)
    speedInternal: int = 3
    increment: List[int] = field(default_factory = lambda: [2, 2])
    direction: List[int] = field(default_factory = lambda: [1, 1])
    inMotion: bool = False

    def resetSpeed(self) -> None:
        self.speed = 3

    @property
    def speed(self) -> int:
        return self.speedInternal

    @speed.setter
    def speed(self, newSpeed: int) -> None:
        self.speedInternal = newSpeed

    def isInMotion(self) -> bool:
        return self.inMotion

    def setMotion(self, isMoving: bool) -> None:
        """
        Method for resetting speed and setting ball in motion
        :param isMoving: whether to move a ball or make it still
        """
        self.inMotion = isMoving
        self.resetSpeed()

    def changeDirection(self, gameObject: Union['Pad', 'Brick', 'Ball']) -> None:
        """
        Method for changing ball's movement direction in case of hitting something
        :param gameObject: object the ball hit
        """
        objectPosition = gameObject.position
        objectSize = gameObject.getSize
        position = self.position
        size = self.getSize

        if (position[0] + size[0]) >= objectPosition[0] and position[0] <= objectPosition[0] + objectSize[0] and (
                objectPosition[1] + objectSize[1] >= position[1] > objectPosition[1]
        ):
            self.position = (position[0], objectPosition[1] + objectSize[1])
            self.direction[1] *= -1

        if (position[0] + size[0]) >= objectPosition[0] and position[0] <= objectPosition[0] + objectSize[0] and (
                objectPosition[1] <= position[1] + size[1] < objectPosition[1] + objectSize[1]
        ):
            self.position = (position[0], objectPosition[1] - size[1])
            self.direction[1] *= -1

        if position[1] <= objectPosition[1] + objectSize[1] and position[1] + size[1] >= objectPosition[1] and (
                position[0] + size[0] >= objectPosition[0] > position[0]
        ):
            self.position = (objectPosition[0] - size[0], position[1])
            self.direction[0] *= -1

        if position[1] <= objectPosition[1] + objectSize[1] and position[1] + size[1] >= objectPosition[1] and (
                position[0] <= objectPosition[0] + objectSize[0] < position[0] + size[0]
        ):
            self.position = (objectPosition[0] + objectSize[0], position[1])
            self.direction[0] *= -1

    def updatePosition(self) -> Optional[Tuple[int, int]]:
        """
        Method for updating ball position in accordance with its speed and direction.
        Although it checks if the ball hit walls, and change it direction accordingly,
        and we place the ball in the middle of the pad if the ball is not in motion.
        :return: new position of the ball
        """
        if not self.isInMotion():
            padPositon = self.game.getPad.position
            self.position = (padPositon[0] + (GameConstants.PAD_SIZE[0] - GameConstants.BALL_SIZE[0]) / 2, GameConstants.SCREEN_SIZE[1] - GameConstants.PAD_SIZE[1] - GameConstants.BALL_SIZE[1])
            return

        position = self.position
        size = self.getSize

        newPosition = [position[0] + (self.increment[0] * self.speed) * self.direction[0],
                       position[1] + (self.increment[1] * self.speed) * self.direction[1]]

        if newPosition[0] + size[0] >= GameConstants.SCREEN_SIZE[0]:
            self.direction[0] *= -1
            newPosition[0] = GameConstants.SCREEN_SIZE[0] - size[0]
            self.game.playSound(GameConstants.SOUND_WALL_BOUNCE)
        if newPosition[0] <= 0:
            self.direction[0] *= -1
            newPosition[0] = 0
            self.game.playSound(GameConstants.SOUND_WALL_BOUNCE)
        if newPosition[1] + size[1] >= GameConstants.SCREEN_SIZE[1]:
            self.direction[1] *= -1
            newPosition[1] = GameConstants.SCREEN_SIZE[1] - size[1]
        if newPosition[1] <= 0:
            self.direction[1] *= -1
            newPosition[1] = 0
            self.game.playSound(GameConstants.SOUND_WALL_BOUNCE)

        self.position = newPosition

    @property
    def isDead(self) -> bool:
        """
        Checks if the ball reachs the bottom wothout touching the pad
        :return: bool
        """
        if self.position[1] + self.getSize[1] >= GameConstants.SCREEN_SIZE[1]:
            return True
        return False
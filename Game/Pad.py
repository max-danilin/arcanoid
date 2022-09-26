import pygame
from Game.Shared import *
from typing import Tuple

class Pad(GameObject):
    '''Class, defining a pad object'''

    def __init__(self, position: Tuple[int, int], sprite: object):
        super().__init__(positions=position, size=GameConstants.PAD_SIZE, sprite=sprite)

    @GameObject.position.setter
    def position(self, position: Tuple[int, int]) -> None:
        """
        Redefining setter method for specifics of pad movement
        :param position: position of an object
        """
        newPosition = [position[0], position[1]]
        size = self.getSize
        if newPosition[0] + size[0] > GameConstants.SCREEN_SIZE[0]:
            newPosition[0] = GameConstants.SCREEN_SIZE[0] - size[0]
        if newPosition[0] < 0:
            newPosition[0] = 0
        self.positions = newPosition
        #super().position = newPosition

    def updatePosition(self) -> None:
        """
        Updating pad position in accordance of mouse movement
        """
        mousePosition = pygame.mouse.get_pos()
        self.position = (mousePosition[0], GameConstants.SCREEN_SIZE[1] - GameConstants.PAD_SIZE[1])

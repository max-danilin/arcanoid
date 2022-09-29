import pygame
from typing import List
import sys


class Scene:
    """Abstract class, containing methods for other scenes."""

    def __init__(self, game):
        """
        Initialising scene and creating a tests list for displaying on the screen.
        :param game: object of our game
        """
        self.__game = game
        self.__texts: List = []

    def render(self) -> None:
        """
        Rendering texts.
        """
        for text in self.__texts:
            self.__game.screen.blit(text[0], text[1])

    @property
    def getGame(self):
        return self.__game

    def handleEvents(self, events) -> None:
        """
        Method for handling occuring events.
        :param events: various pygame events
        """
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def clearText(self) -> None:
        self.__texts = []
        
    def addText(self, string: str, x: int = 0, y: int = 0, color: List[int] = None, background: List[int] = None, size:int = 17) -> None:
        """
        Method for adding text.
        :param string: text string
        :param x: x position
        :param y: y position 
        :param color: color of the text
        :param background: color of the background
        :param size: size of the text
        """
        if not color:
            color = [255, 255, 255]
        if not background:
            background = [0, 0, 0]
        font = pygame.font.Font(None, size)
        self.__texts.append([font.render(string, True, color, background), (x, y)])
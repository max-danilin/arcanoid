import pygame
from typing import List

class Scene:
    '''Abstract class, containing methods for other scenes.'''

    def __init__(self, game: 'Breakout'):
        """
        Initialising scene and creating a tests list for displaying on the screen.
        :param game: object of our game
        """
        self.__game = game
        self.__texts : List[str, ...] = []

    def render(self) -> None:
        """
        Rendering texts.
        """
        for text in self.__texts:
            self.__game.screen.blit(text[0], text[1])

    @property
    def getGame(self) -> 'Breakout':
        return self.__game

    def handleEvents(self, events) -> None:
        """
        Method for handling occuring events.
        :param events: various pygame events
        """
        for event in events:
            if event.type == pygame.QUIT:
                exit()

    def clearText(self) -> None:
        self.__texts = []
        
    def addText(self, string: str, x: int = 0, y: int = 0, color: List[int] = [255, 255, 255], background: List[int] = [0, 0, 0], size:int = 17) -> None:
        """
        Method for adding text.
        :param string: text string
        :param x: x position
        :param y: y position 
        :param color: color of the text
        :param background: color of the background
        :param size: size of the text
        """
        font = pygame.font.Font(None, size)
        self.__texts.append([font.render(string, True, color, background), (x, y)])
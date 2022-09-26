import pygame
from Game.Scenes.Scene import Scene
from Game.Shared import GameConstants
from Game import HighScore

class GameOverScene(Scene):
    '''Game over scene.'''

    def __init__(self, game: 'Breakout'):
        super().__init__(game)

        self.__playerName : str = ""
        self.__highscoreSprite = pygame.image.load(GameConstants.SPRITE_HIGHSCORE)

    def render(self) -> None:
        """
        Rendering player's name and result
        """
        self.getGame.screen.blit(self.__highscoreSprite, (50, 50))

        self.clearText()
        self.addText("Your name: ", 300, 200, size=30)
        self.addText(self.__playerName, 420, 200, size=30)
    
        super().render()

    def handleEvents(self, events) -> None:
        """
        Inserting player's result into high scores and resetting the game.
        :param events: various pygame events
        """
        super().handleEvents(events)

        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    game = self.getGame
                    HighScore().add(self.__playerName, game.getScore)
                    game.reset()
                    game.changeScene(GameConstants.HIGHSCORE_SCENE)
                elif event.key >= 65 and event.key <= 122:
                    self.__playerName += chr(event.key)
                
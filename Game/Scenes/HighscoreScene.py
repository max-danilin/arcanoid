import pygame
from Game.Scenes.Scene import Scene
from Game import HighScore
from Game.Shared import GameConstants

class HighscoreScene(Scene):
    '''Scene with high scores.'''

    def __init__(self, game: 'Breakout'):
        super().__init__(game)
        self.__highscoreSprite = pygame.image.load(GameConstants.SPRITE_HIGHSCORE)

    def render(self) -> None:
        """
        Rendering high scores
        """
        self.getGame.screen.blit(self.__highscoreSprite, (50, 50))

        self.clearText()
        highscore = HighScore()

        x = 350
        y = 100
        for score in highscore.getScores:
            self.addText(score[0], x, y, size = 30)
            self.addText(str(score[1]), x + 200, y, size=30)
            y += 30
        self.addText("Press F1 to restart game", x, y + 60, size=30)
        super().render()

    def handleEvents(self, events) -> None:
        """
        Resetting the game
        :param events: various pygame events
        """
        super().handleEvents(events)

        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F1:
                    self.getGame.reset()
                    self.getGame.changeScene(GameConstants.PLAYING_SCENE)
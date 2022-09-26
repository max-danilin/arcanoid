from Game.Bricks import Brick
from Game.Shared import GameConstants
from typing import Tuple

class SpeedBrick(Brick):
    '''Class, defining speed bricks'''

    def __init__(self, positions: Tuple[int, int], sprite: object, game: 'Breakout'):
        super().__init__(positions = positions, sprite = sprite, game = game)

    def hit(self) -> None:
        """
        Increasing speed of the ball in case of hitting this brick
        """
        game = self.getGame
        
        for ball in game.getBalls:
            ball.speed = ball.speed + 1

        super().hit()

    @property
    def getHitSound(self) -> object:
        return GameConstants.SOUND_SPEED_UP
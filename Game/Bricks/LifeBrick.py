from Game.Bricks import Brick
from Game.Shared import GameConstants
from typing import Tuple

class LifeBrick(Brick):
    '''Class, defining life bricks'''

    def __init__(self, positions: Tuple[int, int], sprite: object, game: 'Breakout'):
        super().__init__(positions = positions, sprite = sprite, game = game)
        
    def hit(self) -> None:
        """
        Increasing lives in case of hitting this brick
        """
        game = self.getGame
        game.increaseLives()
        super().hit()

    @property
    def getHitSound(self) -> object:
        return GameConstants.SOUND_EXTRA_LIFE
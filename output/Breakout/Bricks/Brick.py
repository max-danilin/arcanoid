from Game.Shared import GameObject
from Game.Shared import GameConstants
from dataclasses import dataclass, field
from typing import List


@dataclass
class _GameBase:
    """Class needed to keep MRO, because game parameter is not-default"""
    game: 'Breakout'


@dataclass
class Brick(GameObject, _GameBase):
    """Class, defining a brick object."""

    size: List[int] = field(default_factory=lambda: GameConstants.BRICK_SIZE)
    hitpoints: int = 100
    lives: int = 1

    @property
    def getGame(self) -> 'Breakout':
        return self.game

    def isDestroyed(self) -> bool:
        return self.lives <= 0

    @property
    def getHitPoints(self) -> int:
        return self.hitpoints

    def hit(self) -> None:
        self.lives -= 1

    @property
    def getHitSound(self) -> object:
        return GameConstants.SOUND_BRICK_HIT
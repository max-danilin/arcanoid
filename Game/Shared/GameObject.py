from dataclasses import dataclass
from typing import Tuple, List, Union

@dataclass
class GameObject:
    '''Abstract class, containing methods for various game object.'''

    sprite: object
    positions: Tuple[int, int]
    size: List[int]

    @property
    def position(self) -> Tuple[int, int]:
        return self.positions

    @position.setter
    def position(self, position: Tuple[int, int]) -> None:
        self.positions = position

    @property
    def getSize(self) -> List[int]:
        return self.size

    @property
    def getSprite(self) -> object:
        return self.sprite

    def _intersectsX(self, other: Union['Ball', 'Pad', 'Brick']) -> bool:
        """
        Method for checking intersections on X axis
        :param other: object to check intersections with
        :return: if there is an intersection
        """

        otherPosition = other.position
        otherSize = other.getSize

        if self.positions[0] >= otherPosition[0] and self.positions[0] <= (otherPosition[0] + otherSize[0]):
            return True
        if self.positions[0] + self.size[0] <= otherPosition[0] + otherSize[0] and (self.positions[0] + self.size[0]) >= otherPosition[0]:
            return True
        return False

    def _intersectsY(self, other: Union['Ball', 'Pad', 'Brick']) -> bool:
        """
        Method for checking intersections on Y axis
        :param other: object to check intersections with
        :return: if there is an intersection
        """

        otherPosition = other.position
        otherSize = other.getSize

        if self.positions[1] >= otherPosition[1] and self.positions[1] <= (otherPosition[1] + otherSize[1]):
            return True
        if self.positions[1] + self.size[1] > otherPosition[1] and (self.positions[1] + self.size[1]) < otherPosition[1] + otherSize[1]:
            return True
        return False

    def intersects(self, other: Union['Ball', 'Pad', 'Brick']) -> bool:
        """
        Method for checking intersections
        :param other: object to check intersections with
        :return: if there is an intersection
        """
        if self._intersectsX(other) and self._intersectsY(other):
            return True
        return False
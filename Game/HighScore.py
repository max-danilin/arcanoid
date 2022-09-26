import hashlib
import fileinput
from typing import List

class HighScore:
    '''Class, implementing high score encoding, storing and displaying'''

    def __init__(self):
        self.__highscore = self.load()

    @property
    def getScores(self) -> int:
        return self.__highscore

    @staticmethod
    def load() -> List[list]:
        """
        Method for loading list of high scores.
        First, we get name, score and hash from highscore.dat file,
        then encode it and return in a list
        :return: list of highscore data
        """
        highscore: List[list] = []
        for line in fileinput.input("highscore.dat"):
            name, score, md5 = line.split("[::]")
            md5 = md5.replace('\n', '')

            if str(hashlib.md5(str.encode(str(name + score + "pygame"))).hexdigest()) == str(md5):
                highscore.append([str(name), int(score), str(md5)])

        highscore.sort(key = lambda x: x[1], reverse=True)
        highscore = highscore[0:11]
        return highscore
    
    def add(self, name: str, score: int) -> None:
        """
        Method for adding new high score
        :param name: name of the player
        :param score: score of the player
        """
        hash = hashlib.md5((str(name + str(score) + "pygame")).encode('utf-8'))
        self.__highscore.append([name, str(score), hash.hexdigest()])

        with open("highscore.dat", "w") as f:
            for name, score, md5 in self.__highscore:
                f.write(str(name) + "[::]" + str(score) + "[::]" + str(md5) + "\n")
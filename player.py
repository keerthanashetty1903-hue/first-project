import random
import math

class Player:
    def __init__(self,letter):
        self.letter=letter
    
    def getmove(self,game):
        pass

class randomcomp(Player):
    def __init__(self, letter):
        super().__init__(letter)
    def getmove(self, game):
        pass

class humanplayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def getmove(self, game):
        pass
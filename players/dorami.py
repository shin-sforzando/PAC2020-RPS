from random import choice

from hand import Hand
from player import Player


class Dorami(Player):
    def next_hand(self):
        return choice([Hand.G, Hand.G, Hand.C, Hand.P])

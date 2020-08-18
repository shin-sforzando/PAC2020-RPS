from random import choice

from hand import Hand
from player import Player


class Suneo(Player):
    def next_hand(self):
        return choice([Hand.C, Hand.P])

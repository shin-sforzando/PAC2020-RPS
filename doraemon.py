from hand import Hand
from player import Player


class Doraemon(Player):
    def next_hand(self):
        return Hand.G

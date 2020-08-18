from hand import Hand
from player import Player


class Nobita(Player):
    current_hand = Hand.G

    def next_hand(self):
        if not self.is_won:
            self.current_hand = super(Nobita, self).next_hand()
        return self.current_hand

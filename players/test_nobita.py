#!/usr/bin/env python3

from hand import Hand
from players.nobita import Nobita


def test_hands(trials: int = 1000):
    nobita = Nobita()

    nobita.is_won = False
    for _ in range(trials):
        assert nobita.next_hand() in [Hand.G, Hand.C, Hand.P]

    last_hand: Hand = nobita.next_hand()
    nobita.is_won = True
    for _ in range(trials):
        next_hand = nobita.next_hand()
        assert last_hand is next_hand
        last_hand = next_hand


if __name__ == "__main__":
    test_hands(trials=1000)

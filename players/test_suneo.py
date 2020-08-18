#!/usr/bin/env python3

from hand import Hand
from players.suneo import Suneo


def test_hands(trials: int = 1000):
    suneo = Suneo()
    for _ in range(trials):
        assert suneo.next_hand() in [Hand.C, Hand.P]


if __name__ == "__main__":
    test_hands(trials=1000)

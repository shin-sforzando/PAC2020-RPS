#!/usr/bin/env python3

from hand import Hand
from players.doraemon import Doraemon


def test_hands(trials: int = 1000):
    doraemon_first = Doraemon(is_first=True)
    for _ in range(trials):
        assert doraemon_first.next_hand() is Hand.G
    doraemon_second = Doraemon(is_first=False)
    for _ in range(trials):
        assert doraemon_second.next_hand() is Hand.G


if __name__ == "__main__":
    test_hands(trials=1000)

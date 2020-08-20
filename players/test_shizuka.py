#!/usr/bin/env python3

from math import isclose

from hand import Hand
from players.shizuka import Shizuka


def test_hands(trials: int = 10000, tolerance: float = 0.1):
    shizuka = Shizuka()
    history = []
    for _ in range(trials):
        history.append(shizuka.next_hand())
    num_g = len([h for h in history if h is Hand.G])
    num_c = len([h for h in history if h is Hand.C])
    num_p = len([h for h in history if h is Hand.P])
    print(f"G: {num_g} → {num_g / trials * 100: .2f}%")
    print(f"C: {num_c} → {num_c / trials * 100: .2f}%")
    print(f"P: {num_p} → {num_p / trials * 100: .2f}%")
    assert isclose(trials / 3, num_g, rel_tol=tolerance)
    assert isclose(trials / 3, num_c, rel_tol=tolerance)
    assert isclose(trials / 3, num_p, rel_tol=tolerance)


if __name__ == "__main__":
    test_hands(trials=10000, tolerance=0.1)

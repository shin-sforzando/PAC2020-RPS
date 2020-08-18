#!/usr/bin/env python3

from manager import Manager
from hand import Hand


def main(first: str, second: str, trials: int = 100):
    manager = Manager(first, second)
    for _ in range(trials):
        print(manager.game())
    print(manager.history)


if __name__ == "__main__":
    main("源静香", "源静香")

#!/usr/bin/env python3

from tqdm import tqdm

from manager import Manager
from manager import player_dictionary


def main(first: str, second: str, trials: int = 100):
    if 10000 < trials:
        raise ValueError("The number of attempts is too many.")

    players = player_dictionary.keys()
    if first not in players or second not in players:
        raise ValueError("A player who isn't registered.")

    manager = Manager(first, second)
    for _ in tqdm(range(trials)):
        manager.game()
    print(f"{manager.get_converted_history()} {manager.get_result() * 100: .2f} %")


if __name__ == "__main__":
    main("野比のび太", "ドラえもん", 1000)

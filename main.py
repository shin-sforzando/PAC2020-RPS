#!/usr/bin/env python3

from random import choice

from tqdm import tqdm

from manager import Manager
from manager import player_dictionary

players = list(player_dictionary.keys())


def main(first: str, second: str, trials: int = 100):
    if 10000 < trials:
        raise ValueError("The number of attempts is too many.")

    if first not in players or second not in players:
        raise ValueError("A player who isn't registered.")

    manager = Manager(first, second)
    for _ in tqdm(range(trials)):
        manager.game()
    print(f"{manager.get_converted_history()} {manager.get_result() * 100: .2f} %")


if __name__ == "__main__":
    first_player_name = choice(players)
    second_player_name = choice(players)
    print(f"{first_player_name} vs {second_player_name}")
    for _ in range(1):
        main(first_player_name, second_player_name, 1000)

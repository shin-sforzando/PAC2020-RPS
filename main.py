#!/usr/bin/env python3

from tqdm import tqdm

from manager import Manager


def main(first: str, second: str, trials: int = 100):
    manager = Manager(first, second)
    for _ in tqdm(range(trials)):
        manager.game()
    print(f"{manager.get_converted_history()} {manager.get_result() * 100: .2f} %")


if __name__ == "__main__":
    main("ドラえもん", "源静香", 1000)

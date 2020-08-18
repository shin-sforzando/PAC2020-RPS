#!/usr/bin/env python3

from itertools import product
from timeit import timeit

import pytest
from tqdm import tqdm

from judge import player_dictionary
from main import main


@pytest.mark.skip()
def measure_time(stmt: str, trials: int = 100) -> float:
    t = timeit(stmt, globals=globals(), number=trials)
    print(f"{stmt} took {t} seconds for {trials} attempts.")
    return t


def test_main():
    assert dir(main)
    matches = list(product(player_dictionary, repeat=2))
    for first, second in tqdm(matches):
        assert measure_time(f"main('{first}', '{second}', 1000)", 16) < 3.0


if __name__ == "__main__":
    test_main()

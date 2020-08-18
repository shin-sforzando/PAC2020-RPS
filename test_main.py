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


def test_main_normal(trials: int = 100):
    assert dir(main)
    matches = list(product(player_dictionary, repeat=2))
    for first, second in tqdm(matches):
        assert measure_time(f"main('{first}', '{second}', {trials})", 16) < 3.0


def test_main_abnormal():
    with pytest.raises(ValueError) as ve:
        main("源静香", "源静香", 10001)
    assert "too many" in str(ve)
    with pytest.raises(ValueError) as ve:
        main("源静香", "クリスチーネ剛田", 100)
    assert "who isn't registered" in str(ve)


if __name__ == "__main__":
    test_main_normal(trials=100)
    test_main_abnormal()

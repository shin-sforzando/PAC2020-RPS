#!/usr/bin/env python3

from itertools import product
from timeit import timeit

import pytest
from tqdm import tqdm

from judge import player_dictionary
from main import main

allowed_time_per_match = 1.0


@pytest.mark.skip()
def measure_time(stmt: str, attempts: int = 100) -> float:
    t = timeit(stmt, globals=globals(), number=attempts)
    print(f"{stmt} took {t} seconds for {attempts} attempts.")
    return t


def test_main_normal(trials: int = 100):
    matches = list(product(player_dictionary, repeat=2))
    for first, second in tqdm(matches):
        assert measure_time(f"main('{first}', '{second}', {trials})", 1) < allowed_time_per_match


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

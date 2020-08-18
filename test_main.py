#!/usr/bin/env python3

from timeit import timeit

import pytest

import main


@pytest.mark.skip()
def measure_time(stmt: str, trials: int = 10000) -> float:
    t = timeit(stmt, globals=globals(), number=trials)
    print(f"{stmt} took {t} seconds for {trials} attempts.")
    return t


def test_main():
    dir(main)
    assert 1 != 2

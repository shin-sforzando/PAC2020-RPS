#!/usr/bin/env python3

from timeit import timeit

import pytest

from main import main


@pytest.mark.skip()
def measure_time(stmt: str, trials: int = 100) -> float:
    t = timeit(stmt, globals=globals(), number=trials)
    print(f"{stmt} took {t} seconds for {trials} attempts.")
    return t


def test_main():
    assert dir(main)
    assert measure_time("main('源静香', '源静香', 1000)", 16) < 1.0
    assert measure_time("main('源静香', 'ドラえもん', 1000)", 16) < 1.0
    assert measure_time("main('ドラえもん', '源静香', 1000)", 16) < 1.0
    assert measure_time("main('ドラえもん', 'ドラえもん', 1000)", 16) < 1.0

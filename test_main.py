#!/usr/bin/env python3

import main
from timeit import timeit

trials = 10000
if "main" in dir(main):
    t = timeit("main.main()", globals=globals(), number=trials)
    print(f"It took {t} seconds for {trials} attempts.")

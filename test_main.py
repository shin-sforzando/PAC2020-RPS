from main import main

import timeit

trials = 10000
t = timeit.timeit("main()", globals=globals(), number=trials)
print(f"It took {t} seconds for {trials} attempts.")

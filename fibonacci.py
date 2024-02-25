import timeit
from functools import cache

@cache
def fibonacci(n):
	if n<2:
		return n
	else:
		return fibonacci(n-1) + fibonacci(n-2)

timer = timeit.Timer("fibonacci(35)", "from __main__ import fibonacci")
print(f"{timer.timeit(1):.10f}")
print(fibonacci(8))

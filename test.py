import time
import timeit

start = time.perf_counter()
print("hello")
print("The difference of time is :", time.perf_counter() - start)

start = timeit.default_timer()
print("hello")
print("The difference of time is :", timeit.default_timer() - start)


a = b = 5
b = 4
print(a,b)
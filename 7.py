import random
import time


def get_res(m, n, a):
    a.sort()
    sum = 0
    i = 0
    while i < n and a[i] + sum <= m:
        sum += a[i]
        i += 1
    print(i)


m_in, n_in = map(int, input().split())
a_in = list(map(int, input().split()))

time_start = time.perf_counter()
get_res(m_in, n_in, a_in)
print(time.perf_counter() - time_start)


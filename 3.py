import random
import time

n = int(input())#кол-во объявлений
a = list(map(int, input().split()))#массив прибылей за клик
b = list(map(int, input().split()))#массив среднего кол-во кликов
time_start = time.perf_counter()
a.sort()
b.sort()
res = 0
for i in range(n):
    res += a[i] * b[i]
print(res)
print(time.perf_counter() - time_start)


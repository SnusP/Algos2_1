import random
import time


def MinRefills(x, n, L):
    numRefills = 0
    currentRefill = 0
    while currentRefill <= n:
        lastRefill = currentRefill
        while currentRefill <= n and x[currentRefill + 1] - x[lastRefill] <= L: #считаем, сколько заправок можем проехать на одном баке
            currentRefill = currentRefill + 1
        if currentRefill == lastRefill:
            return -1
        if currentRefill <= n:
            numRefills = numRefills + 1
    return numRefills


d = int(input())
m = int(input())
n = int(input())
stops = [0] + list(map(int, input().split())) + [d] #создаем массив, со всеми остановками на пути от 0 до конечнго пункта
time_start = time.perf_counter()
print(MinRefills(stops, n, m))
print(time.perf_counter() - time_start)


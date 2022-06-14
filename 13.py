import random
import time


def three_partition_bu(arr):
    n = len(arr)
    s = sum(arr)

    if s % 3 != 0:
        return False

    D = [[[None for l in range(s + 1)] for j in range(s + 1)] for i in range(n + 1)]
    for i in range(n + 1):
        D[i][0][0] = True

    for s1 in range(s + 1):
        for s2 in range(s + 1):
            D[0][s1][s2] = (s1 == 0) and (s2 == 0)

    for i in range(1, n + 1):
        for s1 in range(0, s + 1):
            for s2 in range(0, s + 1):
                D[i][s1][s2] = D[i - 1][s1][s2] or D[i - 1][s1 - arr[i - 1]][s2] or D[i - 1][s1][s2 - arr[i - 1]]

    return D[n][s // 3][s // 3]


n = int(input())
arr = [int(i) for i in input().split()]
result = three_partition_bu(arr)
print(1 if result else 0)


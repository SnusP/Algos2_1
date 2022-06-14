import random
import time

K, n = map(int, input().split())
A = list(map(int, input().split()))

F = [0] * (K + 1)
F[0] = 1
Prev = [0] * (K + 1)
for i in range(len(A)):
    for k in range(K, A[i] - 1, -1):
        if F[k - A[i]] == 1:
            F[k] = 1
            Prev[k] = A[i]

i = K
while F[i] == 0:
    i -= 1
Ans = 0
while i > 0:
    Ans += Prev[i]
    i -= Prev[i]
print(Ans)

# test
K, n = 10 ** 4, 300
A = [random.randint(0, 10 ** 5) for i in range(n)]
time_start = time.perf_counter()

F = [0] * (K + 1)
F[0] = 1
Prev = [0] * (K + 1)
for i in range(len(A)):
    for k in range(K, A[i] - 1, -1):
        if F[k - A[i]] == 1:
            F[k] = 1
            Prev[k] = A[i]
i = K
while F[i] == 0:
    i -= 1
Ans = []
k = i
while k > 0:
    Ans.append(Prev[k])
    k -= Prev[k]

print(sum(Ans))
print(time.perf_counter() - time_start)

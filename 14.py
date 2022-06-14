import random


def getVal(v1, v2, op):
    if op == '+':
        return v1 + v2
    if op == '-':
        return v1 - v2
    if op == '*':
        return v1 * v2


def MinAndMax(i, j, m, M, op):
    minimum = float("+inf")
    maximum = float("-inf")
    for k in range(i, j):
        a = getVal(M[i][k], M[k + 1][j], op[k])
        b = getVal(M[i][k], m[k + 1][j], op[k])
        c = getVal(m[i][k], M[k + 1][j], op[k])
        d = getVal(m[i][k], m[k + 1][j], op[k])
        minimum = min(minimum, a, b, c, d)
        maximum = max(maximum, a, b, c, d)
    return minimum, maximum


def maxValue(d, op):
    n = len(d)
    for i in range(n):
        m[i][i] = d[i]
        M[i][i] = d[i]
    for s in range(1, n):
        for i in range(n - s):
            j = i + s
            m[i][j], M[i][j] = MinAndMax(i, j, m, M, op)
    return M[0][n - 1]


dd = input()
n = len(dd) // 2 + 1
m = [[None] * n for j in range(n)]
M = [[None] * n for o in range(n)]
op = [None] * (n - 1)
z = 0
df = []
opf = []
while z < len(dd):
    if z % 2 == 0:
        df.append(int(dd[z]))
    else:
        opf.append(dd[z])
    z += 1
print(maxValue(df, opf))

# test
strr = '+-*'
dd = [random.randint(0, 9) if i % 2 == 0 else strr[random.randint(0, 2)] for i in range(29)]
print(*dd)

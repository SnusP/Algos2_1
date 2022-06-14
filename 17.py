def hodnanari(x,lvl):
    global n

    if lvl == n-1:
        if (x == 4 or x == 6):
            return 3
        else:
            return 2
    if x == 1:
        return hodnanari(8,lvl+1)+hodnanari(6,lvl+1)
    if x == 2:
        return hodnanari(7,lvl+1)+hodnanari(9,lvl+1)
    if x == 3:
        return hodnanari(4,lvl+1)+hodnanari(8,lvl+1)
    if x == 4:
        return hodnanari(3,lvl+1)+hodnanari(9,lvl+1)+hodnanari(0,lvl+1)
    if x == 6:
        return hodnanari(1,lvl+1)+hodnanari(7,lvl+1)+hodnanari(0,lvl+1)
    if x == 7:
        return hodnanari(2,lvl+1)+hodnanari(6,lvl+1)
    if x == 8:
        return hodnanari(1,lvl+1)+hodnanari(3,lvl+1)
    if x == 9:
        return hodnanari(4,lvl+1)+hodnanari(2,lvl+1)
    if x == 0:
        return hodnanari(4,lvl+1)+hodnanari(6,lvl+1)
a = [1,2,3,4,6,7,9]
k=0
n = int(input(f"Введите n"))
if n == 1:
    print(f"8 номеров можно составить")
else:
    for i in a:
        k += hodnanari(i, 1)
    print(f"{k} номеров можно составить")

import time


def apples(h, x):
    res = []
    while len(x) > 0: #пока в массиве есть элементы
        for i in range(len(x)):
            if h - x[i][0] > 0: #если рост отстанется больше 0 после этого яблока
                h += x[i][1] #изменяем рост
                res.append(x[i][2]) #записываем яблоко в результат
                del x[i] # удаляем это яблоко из списка
                break
            elif i == len(x) - 1: #если яблоко нам не подходит, выводим -1
                return [-1]
    return res


n, s = map(int, input().split())
apples_arr = []
for i in range(n):
    apples_arr.append(list(map(int, input().split())))
    apples_arr[i][1] = apples_arr[i][1] - apples_arr[i][0]
    apples_arr[i].append(i + 1)
apples_arr = sorted(apples_arr, key=lambda apple: apple[1])#сортируется массив яблок по ключу суммарного итогового изменения роста
apples_arr.reverse() #переворачиваем массив

time_start = time.perf_counter()
print(*apples(s, apples_arr))
print(time.perf_counter() - time_start)

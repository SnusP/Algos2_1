import time


def get_sum(num):
    res = 0 # место
    i = 1
    while res + i <= num:#пока сумма последнего числа с подрядидущими числами меньше кол-ва конфет
        res += i
        i += 1
    res_array = [j for j in range(1, i - 1)]#записываем в массив подрядидущие числа
    res_array.append(i - 1 + num - res)#вписываем последнее число(самое большое кол-во конфет
    return res_array


n = int(input())#кол-во конфет
time_start = time.perf_counter()
res_for_n = get_sum(n)
print(len(res_for_n)) #выводим кол-во мест
print(*res_for_n)#выводим кол-во конфет за места
print(time.perf_counter() - time_start)

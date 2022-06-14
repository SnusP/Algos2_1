import time


def dots(segments):
    resulting_segments = []
    while len(segments) > 0:
        if len(segments) < 2:
            seg = segments.pop()
            resulting_segments.append(seg)
        else:
            a, b = segments[0], segments[1]
            if b[0] <= a[1]:#если у двух сегментов есть зона пересечения
                left, right = b[0], b[1] if b[1] <= a[1] else a[1]#левая часть - начальное время второго, правая - наименьшее время из конечных
                overlapping = (left, right)
                segments = segments[2:]
                segments = [overlapping] + segments
            else:
                resulting_segments.append(segments[0])#если у сегментов нет пересечений - в результат вписываем первый сегмент и проверяем дальше без него
                segments = segments[1:]
    return [x[1] for x in resulting_segments]#выводим первые элементы кортежей из массива результатов


n = int(input()) #кол-во жильцов
segments_input = []
for i in range(n):
    segments_input.append(tuple(map(int, input().split()))) #вводятся сегменты(кто восколько дома)
print(segments_input)
time_start = time.perf_counter()
segments_input.sort(key=lambda x: (x[0], x[1]))#сортировка по двум ключам
result = dots(segments_input)
print(len(result))
print(' '.join(map(str, result)))
print(time.perf_counter() - time_start)


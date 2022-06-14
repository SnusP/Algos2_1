import time

def LargestNumber(Digits):
    answer = ''
    while Digits: #пока в массиве есть числа
        max_digit = '.' #максимальное число
        for digit in Digits: #идеи по числам
            i = 0
            min_len = min(len(digit), len(max_digit)) #смотрим, какое число состоит из меньшего кол-ва цифр
            while i < min_len-1 and digit[i] == max_digit[i]: #выбираем цифру числа, которая различается в максимальном и текущем числе
                i += 1
            if i == min_len-1: #выбираем максимальное число из массива
                if len(digit) > len(max_digit):
                    max_digit = max_digit if digit[i] < max_digit[0] else digit
                else:
                    max_digit = digit if max_digit[i] < digit[0] else max_digit
            elif digit[i] > max_digit[i]:
                max_digit = digit
        answer += max_digit #добавляем к итоговой строке максимальное число
        Digits.remove(max_digit) # убираем из массива рассмотренное число
    return answer

n = int(input())
a = list(map(str,input().split()))
time_start = time.perf_counter()
print(LargestNumber(a))
print(time.perf_counter() - time_start)

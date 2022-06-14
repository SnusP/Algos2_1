with open("input.txt") as file:
    a = []
    ceni = []
    zakaz = int(file.readline())
    for i in range(7):
        a.append(file.readline().split("\n"))
        ceni = []
        for i in range(len(a)):
            ceni.append(int(a[i][0]))
b = {}
def slovar(a):
    c = 1
    for i in range(7):
        b[c] = a[i]
        c *= 10

slovar(ceni)
def schet(b,zakaz):
    vigodnoe = 1000000000000000000000 #переменные для подсчета итогов
    itogo = 0
    for i in b.keys(): # проходим по ключам словаря
        if zakaz // i == 0: # если в этом тарифе листов печатают больше, чем нам нужно
            if vigodnoe > b[i]: # если дешевле, чем до этого
                vigodnoe = b[i] # ответ, если это дешевле, чем дальнейшие тарифы
        else:
            itogo = (zakaz // i)*b[i]
            mod = zakaz % i
            itogo += schet(b,mod)
    if vigodnoe < itogo:
        return vigodnoe
    else:
        return itogo
print(ceni)
print(b)
print(schet(b,zakaz))
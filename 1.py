import random
import math

while True:
    mat = 0
    mat1 = 0
    m = int(input("Введите  m "))
    vib = int(input("Введите  количество выборки "))
    print()
    myD = []
    myF = []
    myV = []
    p = random.random()
    for k in range(1, m - 1):
        # s = (math.log(k + 1, m) - math.log(k, m))
        s = - ((1 - p) ** k) * math.log(p, 2.71)
        s = round(s, 3)
        myD.append(s)
        mat = k * s + mat
        mat1 = k * k * s + mat
    mat = round(mat, 3)
    disp = round(mat1 - (mat * mat), 3)
    matv = 0
    sumvib = 0
    for j in range(vib):
        n = random.random()
        n = round(n, 3)
        myV.append(n)
        j1 = 0
        him = myD[j1]
        g = False
        l = 1
        while g is False:
            if n <= him:
                myF.append(l)
                g = True
            else:
                j1 += 1
                him += myD[j1]
                l += 1
        sumvib = sumvib + l
    matv = sumvib / vib
    dispv = 0
    for d in range(vib):
        diz = myV[d]
        dispv += (diz - matv) * (diz - matv)
    dispv = round(dispv, 3)

    print('Теоретическое Мат ожидание -  ', mat)
    print('Теоретическая Дисперсия -  ', disp)
    print('Массив теоретических вероятностей - ', myD, '\n')
    print('Массив вероятностей выборок - ', myV)
    print('Массив выборок - ', myF)
    print('Мат ожидание выборок - ', matv)
    print('Дисперсия выборок - ', dispv)

    ans = input("Exit?")
    if ans == "y":
        break

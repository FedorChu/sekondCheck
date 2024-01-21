import random

from map_ship_PC import PC_ship, mapPC
from map_ship_user import User_ship, map_User



class Ship:
    def __init__(self, MAP_PC, MAP_User):
        self.MAP_PC = MAP_PC
        self.MAP_USER = MAP_User
MAP_PC = mapPC
MAP_User = map_User

print('Изначальное распределение кораблей компьютра:')
for i in MAP_PC:
    for j in i:
        print(j, end=' ')
    print()
print('Изначальное распределение кораблей человека:')
for i in MAP_User:
    for j in i:
        print(j, end=' ')
    print()

k = 0
l = 0
h = 0
while k < 3 or l < 3:
    h = h+1

    print(f' {h} Ход компьютера')
    def PC_step(X1, X2, k)-> None:
        print(X1, X2)

        if MAP_PC[X1][X2] == 'x':
            while MAP_PC[X1][X2] == 0:
                X1 = random.randrange(1, 7, 1)
                X2 = random.randrange(2, 14, 2)



        if  MAP_PC[X1][X2] == 0:

            MAP_PC[X1][X2] = 'x'
            print(k, 'не попал')

        if MAP_PC[X1][X2] == '■':
            k = k + 1
            print(k)
            MAP_PC[X1][X2] = 'x'


    k = k + 0
    PC_step(random.randrange(1, 6, 1), random.randrange(2, 14, 2), k)
    print(f"Ситуция после {h} хода компьютера")
    for i in MAP_PC:
        for j in i:
            print(j, end=' ')
        print()




    print(f'Ход {h} User')

    def User_step(Y1, Y2, l)-> None:
        print(f'выбранная позиции {Y1} и {Y2}')


        if MAP_User[Y1][Y2] == 'x':
            while MAP_User[Y1][Y2] == 'x':
                print(f'необходимо выбрать другое значение строки {Y1} и столбца {Y2} ')
                Y1 = int(input("выберите строку от 1 до 6: "))
                Y2 = int(input("выберите столбец от 2 до 12 только четные числа: "))


        if MAP_User[Y1][Y2] == 0:
            MAP_User[Y1][Y2] = 'x'
            print('User не попал')
        if MAP_User[Y1][Y2] == '■':
            MAP_User[Y1][Y2] = 'x'
            print('User попал')
            l = l + 1
            print(f'{l} подпитых корбалей')


    o = int(input("выберите строку от 1 до 6: "))
    p = int(input("выберите столбец от 2 до 12 только четные числа: "))
    User_step(o, p, l)


    print(f"Ситуция после {h} хода User")

    for y in MAP_User:
        for t in y:
            print(t, end=' ')
        print()





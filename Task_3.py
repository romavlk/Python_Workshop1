# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, 
# в которой находится эта точка (или на какой оси она находится). 

def inputСoordinate(x):
    a = [0] * x
    for i in range(x):
        is_OK = False
        while not is_OK:
            try:
                number = float(input(f'Введите {i+1} координату: '))
                a[i] = number
                is_OK = True
                if a[i] == 0:
                    is_OK = False
                    print('Координата не должно быть равна 0 ')
            except ValueError:
                print('Вы ввели не число!')
    return a


def checkCoordinates(xy):
    quarter = 4
    if xy[0] > 0 and xy[1] > 0:
        quarter = 1
    elif xy[0] < 0 and xy[1] > 0:
        quarter = 2
    elif xy[0] < 0 and xy[1] < 0:
        quarter = 3
    print(f'Точка находится в {quarter} четверти плоскости')


coordinate = inputСoordinate(2)
checkCoordinates(coordinate)
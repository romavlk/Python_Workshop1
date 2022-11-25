# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y)

def getNumber(inputText):
    is_number = False
    while not is_number:
        try:
            number = int(input(f"{inputText}"))
            is_number = True
        except ValueError:
            print('Это НЕ ЧИСЛО!')
    return number


quarter = getNumber('Введите номер четверти: ')
if quarter == 1:
    print('x > 0, y > 0')
elif quarter == 2:
    print('x < 0, y > 0')
elif quarter == 3:
    print('x < 0, y < 0')
elif quarter == 4:
    print('x > 0, y < 0')
else:
    print('Координатная плоскость имеет только 4 четверти')